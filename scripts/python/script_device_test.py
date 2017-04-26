import Domoticz

import DomoticzEvents as DE

#import reloader
#reloader.auto_reload(__name__)

# similar to http://www.domoticz.com/wiki/Smart_Lua_Scripts
# name is PIR <options> <switch controlled>
# options can be day/night/all
# example names:
# Pir day-night Slaapkamer groot
# PIR all Slaapkamer groot
# PIR night Slaapkamer groot

#DomoticzEvents.log(0, "Test")

# Domoticz.Log(0, "Testing")

DE.Log("Python: Changed: " + DE.changed_device.Describe())

if DE.changed_device_name == "Test":
    if DE.Devices["Test_Target"].n_value_string == "On":
        DE.Command("Test_Target", "Off")

    if DE.Devices["Test_Target"].n_value_string == "Off":
        DE.Command("Test_Target", "On")

#changed_device = DE.Devices[DE.changed_device_name]

#DE.Log("Python: " + DE.changed_device.Describe())

#for aDeviceKey in DE.Devices:
#    DE.Log("Python: " + DE.Devices[aDeviceKey].Describe())
#test = DE.PDevice(name="Test")
#DE.Log("Python: " + DE.Devices["Test"].n_value_string)
