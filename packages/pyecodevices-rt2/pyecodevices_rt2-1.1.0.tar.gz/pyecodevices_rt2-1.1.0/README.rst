===============================================
pyecodevices-rt2 - Python `GCE Ecodevices RT2`_
===============================================


.. image:: https://img.shields.io/pypi/v/pyecodevices_rt2.svg
        :target: https://pypi.python.org/pypi/pyecodevices_rt2

.. image:: https://img.shields.io/pypi/pyversions/pyecodevices_rt2.svg
        :target: https://pypi.python.org/pypi/pyecodevices_rt2

.. image:: https://img.shields.io/travis/pcourbin/pyecodevices_rt2.svg
        :target: https://travis-ci.com/pcourbin/pyecodevices_rt2

.. image:: https://readthedocs.org/projects/pyecodevices-rt2/badge/?version=latest
        :target: https://pyecodevices-rt2.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/pcourbin/pyecodevices_rt2/shield.svg
     :target: https://pyup.io/repos/github/pcourbin/pyecodevices_rt2/
     :alt: Updates

.. image:: https://codecov.io/github/pcourbin/pyecodevices_rt2/branch/master/graph/badge.svg
     :target: https://codecov.io/github/pcourbin/pyecodevices_rt2


| Get information from `GCE Ecodevices RT2`_.

This work is originally developed for use with `Home Assistant`_ and the *custom component* `ecodevices_rt2`_.

* Free software: MIT license
* Documentation: https://pyecodevices-rt2.readthedocs.io.


Features
--------

- Connect to the API (see `GCE Ecodevices RT2 API`_ (or `PDF`_)) and get any value::

        # Example with indexes
        from pyecodevices_rt2 import EcoDevicesRT2
        ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
        ecodevices.get('Index','All') # Get all indexes as JSON
        ecodevices.get('Index','All','Index_TI1') # Get specific value

- Define a simple object such as `Counter`, `DigitalInput`, `EnOcean Switch or Sensor`, `Post and Sub-Post`, `Relay`, `SupplierIndex`, `Toroid`, `VirtualOutput`, `X4FP (Heaters)`, `XTHL`::

        # Example with a Relay
        from pyecodevices_rt2 import EcoDevicesRT2, Relay
        ecodevices = EcoDevicesRT2('192.168.0.20','80',"mysuperapikey")
        # Relay number 1
        test = Relay(ecodevices, 1)
        print("Current status: %r" % test.status)
        test.off() # Change relay to off
        test.on() # Change relay to on
        test.toggle() # Invert relay status
        test.status = True # Change relay to on

Credits
-------

| This work is inspired by the work of `Aohzan`_.
| This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _`GCE Ecodevices RT2`: http://gce-electronics.com/fr/home/1345-suivi-consommation-ecodevices-rt2-3760309690049.html
.. _`GCE Ecodevices RT2 API`: https://gce.ovh/wiki/index.php?title=API_EDRT
.. _`PDF`: https://forum.gce-electronics.com/uploads/default/original/2X/1/1471f212a720581eb3a04c5ea632bb961783b9a0.pdf
.. _`Home Assistant`: https://www.home-assistant.io/
.. _`ecodevices_rt2`: https://github.com/pcourbin/ecodevices_rt2
.. _`Aohzan`: https://github.com/Aohzan/pyecodevices