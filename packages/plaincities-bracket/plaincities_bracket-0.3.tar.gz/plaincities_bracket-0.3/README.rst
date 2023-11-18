
plaincities is a library of places in many languages. It is based on the geonames database.


Installation
------------

.. code-block:: text

    pip install plaincities


Usage
-----

All countries are loaded after initialization but city data has to be loaded explicitly for performance reasons: 

.. code-block:: python

    from plaincities import Countries
    countries = Countries(language='en')
    india = countries['IN']
    india.load_cities()
    kerala = india.states['Kerala']
    kochi = kerala.cities['Kochi']
    (kochi.latitude, kochi.longitude)

.. code-block:: text

   ('9.93988', '76.26022')

You can also load cities during initialization:

.. code-block:: python

    from plaincities import Countries
    countries = Countries(countries_to_load=['IN', 'MX'])
    mexico = countries['MX']
    mexico.load_cities()
    merida = mexico.cities['Mérida']
    merida.timezone.key

.. code-block:: text

   'America/Merida'


or load by continent:

.. code-block:: python

    from plaincities import Countries
    countries = Countries(continents_to_load=['AF'])

or load all the cities on the globe!

.. code-block:: python

    from plaincities import Countries
    countries = Countries(load_all=True)



Switching languages:
====================

.. code-block:: python

    from plaincities import Countries
    countries = Countries(language='zh', countries_to_load=['CN'])
    china = countries['CN']
    beijing = china.cities['北京']
    (china.name, beijing.name, beijing.ascii_name)

.. code-block:: text

   ('中国', '北京', 'Beijing')

Suggestions:

.. code-block:: python

    from plaincities import Countries
    countries = Countries(countries_to_load=['GR'])
    greece = countries['GR']
    list(greece.cities.suggest('Tesaloniki', threshold=0.7))


.. code-block:: text

   ['Heraklion', 'Thessaloniki']



Generating language files
-------------------------

Default installation supports English, Turkish, French, Spanish, Chinese, Russian and Arabic.
You can setup additional languages after the installation.


.. code-block:: python

    from plaincities import generator
    Generator('data', 'new_values').generate_values('cities15000.txt', ['ko'], 'ko')

.. code-block:: python

    from plaincities import Countries
    countries = Countries(countries_to_load=['TH'], path='new_values')
    thailand = countries['TH']
    thailand.name

.. code-block:: text

   '태국'


Contact:
--------

ufuk.kocolu@proton.me