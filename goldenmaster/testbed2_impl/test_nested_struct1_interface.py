
from testbed2_api import api
from testbed2_impl import NestedStruct1Interface

class TestNestedStruct1Interface:

    def test_prop1(self):
        o = NestedStruct1Interface()
        self.called = False
        o.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop1(api.NestedStruct1())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop1() == api.NestedStruct1()

    def test_func1(self):
        o = NestedStruct1Interface()
        o.func1(param1=api.NestedStruct1())

    def test_sig1(self):
        o = NestedStruct1Interface()
        self.called = False
        o.on_sig1 += lambda *args: setattr(self, 'called', True)
        o._sig1(api.NestedStruct1())
        assert self.called == True
