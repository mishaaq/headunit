#!/usr/bin/env python

import dbus
import dbus.service
import dbus.mainloop.glib

import gobject

class Service(dbus.service.Object):
   def run(self):
      dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
      bus_name = dbus.service.BusName('com.jci.nativeguictrl', bus=dbus.bus.BusConnection("unix:path=/tmp/dbus_hmi_socket"))
      dbus.service.Object.__init__(self, bus_name, '/com/jci/nativeguictrl')

      self._loop = gobject.MainLoop()
      print("Service running...")
      self._loop.run()
      print("Service stopped")

   @dbus.service.method(dbus_interface='com.jci.nativeguictrl', in_signature='sn', out_signature='b')
   def SetRequiredSurfaces(self, surfaces, fade_opera):
      print("  surfaces method called")
      return True

   @dbus.service.method(dbus_interface='com.jci.nativeguictrl', in_signature='', out_signature='')
   def Quit(self):
      print("  shutting down")
      self._loop.quit()

if __name__ == "__main__":
   Service().run()

