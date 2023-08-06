=====
Usage
=====

EcoDevicesRT2
-------------
For the API and parameters, see `GCE Ecodevices RT2 API`_ (or `PDF`_).

Parameters::

- `host`: ip or hostname
- `port`: (default: 80)
- `apikey`: if authentication enabled on Ecodevices RT2
- `timeout`: (default: 3)

Properties::

- `host`: return the host
- `apikey`: return the apikey
- `apiurl`: return the default apiurl

Methods::

- `ping`: return true if the Ecodevices answer
- `get`: return json or part of json.


Advanced/API usage
------------------
To use pyecodevices-rt2 in a project, you can directly use parameters from the `GCE Ecodevices RT2 API`_ (or `PDF`_)::

    from pyecodevices_rt2 import EcoDevicesRT2

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")

    print("# ping")
    print(ecodevices.ping())
    print("# Default API call")
    print(ecodevices.apiurl)

    # Indexes
    print("# All Indexes")
    print(ecodevices.get('Index','All'))
    print("# Only Index 'Index_TI1'")
    print(ecodevices.get('Index','All','Index_TI1'))

    # Powers
    print("# Actual power on 'POSTE5'")
    print(ecodevices.get('Get','P','INSTANT_POSTE5'))

    # EnOcean
    print("# All Enocean")
    print(ecodevices.get('Get','XENO'))
    print("# Set Enocean1 and get status")
    print(ecodevices.get('SetEnoPC','1','status'))
    print("# Clear Enocean2 and get status")
    print(ecodevices.get('ClearEnoPC','2','status'))

    # Heaters / FP Modules
    print("# Current state of all zones")
    print(ecodevices.get('Get','FP'))
    print("# Current state of First Zone of First FP module")
    print(ecodevices.get('Get','FP', 'FP1 Zone 1'))
    print("# Force First Zone of First FP module to be on 'Confort' mode and get status")
    print(ecodevices.get('SetFP01','0', 'status'))
    
Counter
-------
You can define a Counter (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, Counter

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # Counter number 1
    test = Counter(ecodevices, 1)
    print("Current value: %d" % test.value)
    print("Current price: %d" % test.price)

    test.value = 20 # Change the value of the counter to 20
    test.add(5) # Add 5 to the counter
    test.substrat(10) # Substract 10 to the counter

DigitalInput
------------
You can define a DigitalInput (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, DigitalInput

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # DigitalInput number 1
    test = DigitalInput(ecodevices, 1)
    print("Current status: %r" % test.status)

EnOcean Switch or Sensor
------------------------
You can define a EnOcean Switch or Sensor (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, EnOceanSensor, EnOceanSwitch

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # EnOceanSensor number 1
    test = EnOceanSensor(ecodevices, 1)
    print("Current value: %f" % test.value)

    # EnOceanSwitch number 1
    test = EnOceanSwitch(ecodevices, 1)
    print("Current status: %r" % test.status)
    test.off() # Change switch to off
    test.on() # Change switch to on
    test.toggle() # Invert switch status
    test.status = True # Change switch to on

Post and Sub-Post
-----------------
You can define a Post and Sub-post (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, Post

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # Post number 1
    test = Post(ecodevices, 1)
    print("Index: %f" % test.index)
    print("Price: %f" % test.price)
    print("Index of the day: %f" % test.index_day)
    print("Price of the day: %f" % test.price_day)
    print("Instant power: %f" % test.instant)

    # Sub-post number 2 of Post 1
    test = Post(ecodevices, 1, 2)
    print("Index: %f" % test.index)
    print("Price: %f" % test.price)
    print("Index of the day: %f" % test.index_day)
    print("Price of the day: %f" % test.price_day)
    print("Instant power: %f" % test.instant)


Relay
-----
You can define a Relay (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, Relay

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # Relay number 1
    test = Relay(ecodevices, 1)
    print("Current status: %r" % test.status)
    test.off() # Change relay to off
    test.on() # Change relay to on
    test.toggle() # Invert relay status
    test.status = True # Change relay to on

SupplierIndex
-------------
You can define a SupplierIndex (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, SupplierIndex

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # SupplierIndex number 1
    test = SupplierIndex(ecodevices, 1)
    print("Index: %f" % test.value)
    print("Price: %f" % test.price)


Toroid
------
You can define a Toroid (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, Toroid

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # Toroid number 1
    test = Toroid(ecodevices, 1)
    print("Value: %f" % test.value)
    print("Price: %f" % test.price)

    # Only for toroid 1 to 4:
    print("Consumption: %f" % test.consumption)
    print("Consumption Price: %f" % test.consumption_price)
    print("Production: %f" % test.production)
    print("Production Price: %f" % test.production_price)


VirtualOutput
-------------
You can define a VirtualOutput (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, VirtualOutput

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # VirtualOutput number 1
    test = VirtualOutput(ecodevices, 1)
    print("Current status: %r" % test.status)


X4FP (Heaters)
--------------
You can define a X4FP (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, X4FP

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # X4FP of Module 1, Zone 2
    test = X4FP(ecodevices, 1, 2)
    print("Current mode: %d" % test.mode)
    test.mode = 1 # Change mode to `Eco`

.. list-table:: List of Heater/X4FP mode values
   :widths: auto
   :header-rows: 1

   * - Mode
     - State (EN)
     - Etat (FR)
   * - `-1`
     - `UNKNOWN` (or module not present)
     - `UNKNOWN` (ou module non présent)
   * - `0`
     - `Confort`
     - `Confort`
   * - `1`
     - `Eco`
     - `Eco`
   * - `2`
     - `Frost free`
     - `Hors Gel`
   * - `3`
     - `Stop`
     - `Arret`
   * - `4`
     - `Confort -1`
     - `Confort -1`
   * - `5`
     - `Confort -2`
     - `Confort -2`

XTHL
----
You can define a XTHL (see from the `GCE Ecodevices RT2 API`_ (or `PDF`_))::

    from pyecodevices_rt2 import EcoDevicesRT2, XTHL

    ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
    print("# ping")
    print(ecodevices.ping())

    # XTHL number 1
    test = XTHL(ecodevices, 1)
    print("Temperature: %f" % test.temperature)
    print("Humidity: %f" % test.humidity)
    print("Luminosity: %f" % test.luminosity)

.. _`GCE Ecodevices RT2 API`: https://gce.ovh/wiki/index.php?title=API_EDRT
.. _`PDF`: https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf