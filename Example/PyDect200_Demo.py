#!/usr/bin/env python
# -- coding: utf-8 --
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

try:
        from PyDect200 import PyDect200
except:
        print('PyDect200 is not installed!')
        print('run: pip install PyDect200')
        exit()
import getpass

try:
    PyDect200.__version__
except:
    PyDect200 = PyDect200.PyDect200

print(("Welcome to PyDect200 v%s, the Python AVM-DECT200 API" % PyDect200.__version__))
fritzbox_pw = getpass.getpass(prompt='Please insert your fritzbox-password: ', stream=None)
print('Thank you, please wait few seconds...')
f = PyDect200(fritzbox_pw)
try:
        info = f.get_info()
        power = f.get_power_all()
        names = f.get_device_names()
except Exception:
    print('HTTP-Error, wrong password?')
    exit()

print('')
for dev_id in list(info.keys()):
        print(("Device ID:           %s" % dev_id))
        dev_name = names.get(dev_id)
        try:
            print(("Device Name:         %s" % dev_name))
        except:
            print(("Device Name:         %s" % dev_name.encode('utf-8').decode('utf-8', 'ignore')))


        print(("Device State:        %s" % ('ON' if info.get(dev_id) == '1' else 'OFF')))
        dev_power = power.get(dev_id)
        if dev_power.isdigit():
            dev_power = float(dev_power) / 1000
        print(("Device Power:        %sW" % dev_power))
        print(("Device Energy:       %sWh" % f.get_energy_single(dev_id)))
        print(("Device Temperature:  %s degree Celsius  " % (f.get_temperature_single(dev_id))))
        print('')
