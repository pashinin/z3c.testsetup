from __future__ import print_function
import zope.interface

class IBar(zope.interface.Interface):
    def do_bar():
        pass

class BarUtility(object):
    zope.interface.implements(IBar)

    def do_bar(self):
        print("Bar!")
