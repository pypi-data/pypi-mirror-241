from importlib.util import spec_from_file_location, module_from_spec
from importlib.abc import Loader
from zoneinfo import ZoneInfo
from difflib import SequenceMatcher
import os
from typing import List, Dict, Iterable, Generator, TypeVar, Generic, Callable
from pathlib import Path

__VALUE_PATH__ = os.path.dirname(os.path.abspath(__file__)) + '/_values'

T = TypeVar('T')

class CityValueFile:

    names: List[str]
    ascii_names: List[str]
    positions: List[List[float]]
    alternate_names: List[List[str]]
    positions: List[List[float]]
    timezones: List[str]
    populations: List[int]
    altitudes: List[int]
    parents: List[str]
    states: Dict[str, List[str]]
    districts: Dict[str, List[str]]

class CountryValueFile:

    names: List[str]
    alpha2_codes: List[str]
    alpha3_codes: List[str]
    fips_codes: List[int]
    continent_indexes: List[List[str | int]]

class NamedItem:

    def __init__(self, name, ascii_name=None, alternate_names=None) -> None:
        self.name = name
        self.ascii_name = ascii_name
        self.alternate_names = alternate_names


class Container(Generic[T]):
    
    def __init__(self, items: Iterable[T]=None) -> None:
        self.__items = items or []

    def __indexes_for(self, name):
        matches = [i for i, x in enumerate(self.items) if x.name == name or x.ascii_name == name or x.alternate_names and name in x.alternate_names]
        return matches

    @property
    def items(self) -> List[T]:
        return self.__items

    def append(self, obj: NamedItem):
        self.items.append(obj)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return self.items.__iter__()

    def __contains__(self, key: str) -> bool:
        matches = self.__indexes_for(key)
        return len(matches) > 0

    def __getitem__(self, key: str) -> T:
        matches = self.__indexes_for(key)
        if len(matches):
            return self.items[matches[0]]
        else:
            raise KeyError(key)

    def suggest(self, query, threshold=0.5) -> Generator[str, None, None]:
        for item in self.items:
            ratio = SequenceMatcher(a=query, b=item.name).quick_ratio()
            if ratio >= threshold:
                yield item.name

    def filter(self, func: Callable):
        items = filter(func, self.items)
        return items

class State(NamedItem):

    def __init__(self, name, ascii_name, alternate_names=[]) -> None:
        super().__init__(name, ascii_name, alternate_names)
        self.__disticts = Container()
        self.__cities = Container()

    @property
    def districts(self) -> Container["District"]:
        return self.__disticts

    @property
    def cities(self) -> Container["City"]:
        return self.__cities

class City(NamedItem):

    def __init__(self, name, ascii_name, alternate_names, latitude: float, longitude: float, timezone: ZoneInfo, population: int, altitude: int, state: State=None, district: "District"=None) -> None:
        super().__init__(name, ascii_name, alternate_names)
        self.latitude = latitude
        self.longitude = longitude
        self.state = state
        self.district = district
        self.timezone:ZoneInfo = timezone
        self.population = population
        self.altitude = altitude

class District(NamedItem):

    def __init__(self, name, ascii_name=None, alternate_names=None) -> None:
        super().__init__(name, ascii_name, alternate_names)
        self.__state = None
        self.__cities: Container[City] = Container()

    @property
    def state(self) -> State:
        return self.__state
    
    @state.setter
    def state(self, val):
        self.__state = val
    
    @property
    def cities(self) -> Container[City]:
        return self.__cities


def _load_value_file(name, path=None):
    path = path or __VALUE_PATH__
    spec = spec_from_file_location(name, f'{path}/{name}.py')
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def _load_constants():
    return _load_value_file('constants')

constants = _load_constants()

class Country(NamedItem, Container):

    def __init__(self, name, alpha2, alpha3, fips, continent) -> None:
        super().__init__(name)
        self.alpha2: str = alpha2
        self.alpha3: str = alpha3
        self.fips: int = fips
        self.continent: str = continent
        self.states: Container[State] = None
        self.districts: Container[District] = None
        self.cities: Container[City] = None

    def load_cities(self, language=None, path=None):
        language = language or constants.default_language
        timezone_names = constants.timezone_names
        if self.cities is None:
            self.cities = Container()
            values: CityValueFile = _load_value_file(f'{language}/{self.alpha2}_{language}', path)
            states = {}
            districts = {}
            for key, value in values.states.items():
                states[key] = State(value[0], value[1])
            for key, value in values.districts.items():
                districts[key] = District(value[0], value[1])
                state_code = key[0:key.rindex('.')]
                districts[key].state = states[state_code]
                states[state_code].districts.append(districts[key])
            for i, name in enumerate(values.names):
                parent_code = values.parents[i]
                state = states[parent_code] if parent_code in values.states else None
                district = districts[parent_code] if parent_code in values.districts else None
                city = City(name, values.ascii_names[i], values.alternate_names[i], values.positions[i][0], values.positions[i][1], ZoneInfo(timezone_names[values.timezones[i]]), values.populations[i], values.altitudes[i], state, district)
                self.cities.append(city)
                if state:
                    state.cities.append(city)
                if district:
                    district.cities.append(city)
            self.states = Container(list(states.values()))
            self.districts = Container(list(districts.values()))

    def __contains__(self, key: str):
        return key in self.states

class Countries(Container):
    
    def __init__(self, language=None, load_all=False, countries_to_load:Iterable[str]=None, continents_to_load:Iterable[str]=None, path:str=None) -> None:
        language = language or constants.default_language
        countries_to_load = countries_to_load or []
        continents_to_load = continents_to_load or []
        self.__instances: Dict[int, Country] = {}
        self.__values: CountryValueFile = None
        self.__path = path
        self.__load_countries(language, load_all, countries_to_load, continents_to_load)

    def __load_countries(self, language, load_all, countries_to_load, continents_to_load):
        if not self.__values:
            self.__values: CountryValueFile = _load_value_file(f'{language}/countries_{language}', self.__path)
            for i, name in enumerate(self.__values.names):
                country = Country(name, self.__values.alpha2_codes[i], self.__values.alpha3_codes[i], self.__values.fips_codes[i], self.__continent_for(i, self.__values.continent_indexes))
                self.__instances[i] = country
                if load_all or self.__values.alpha2_codes[i] in countries_to_load\
                    or country.continent in continents_to_load:
                    country.load_cities(path=self.__path)

    def __index_for(self, key: str | int) -> int | None:
        if isinstance(key, str):
            if len(key) > 3:
                return self.__values.names.index(key)
            if len(key) == 2:
                return self.__values.alpha2_codes.index(key)
            if len(key) == 3:
                return self.__values.alpha3_codes.index(key)
        if isinstance(key, int):
            return self.__values.fips_codes.index(key)

    def __contains__(self, key: str | int):
        try:
            self.__index_for(key)
            return True
        except IndexError:
            return False

    def __continent_for(self, index, continent_indexes):
        for n, s, e in continent_indexes:
            if index >= s and index < e:
                return n 

    def __getitem__(self, key: str | int) -> Country:
        try:
            index = self.__index_for(key)
            return self.__instances[index]
        except IndexError:
            raise KeyError(key)
