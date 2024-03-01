
from testbed2_api import api
from testbed2_impl import NestedStruct2Interface

class TestNestedStruct2Interface:

    def test_prop1(self):
        o = NestedStruct2Interface()
        o.set_prop1(api.NestedStruct1())
        assert o.get_prop1() == api.NestedStruct1()

    def test_prop2(self):
        o = NestedStruct2Interface()
        o.set_prop2(api.NestedStruct2())
        assert o.get_prop2() == api.NestedStruct2()

    def test_func1(self):
        o = NestedStruct2Interface()
        o.func1(param1=api.NestedStruct1())

    def test_func2(self):
        o = NestedStruct2Interface()
        o.func2(param1=api.NestedStruct1(), param2=api.NestedStruct2())

    def test_sig1(self):
        o = NestedStruct2Interface()
        self.called = False
        o.on_sig1 += lambda *args: setattr(self, 'called', True)
        o._sig1(api.NestedStruct1())
        assert self.called == True

    def test_sig2(self):
        o = NestedStruct2Interface()
        self.called = False
        o.on_sig2 += lambda *args: setattr(self, 'called', True)
        o._sig2(api.NestedStruct1(), api.NestedStruct2())
        assert self.called == True
