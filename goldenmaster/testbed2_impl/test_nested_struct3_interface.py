
from testbed2_api import api
from testbed2_impl import NestedStruct3Interface

class TestNestedStruct3Interface:

    def test_prop1(self):
        o = NestedStruct3Interface()
        o.set_prop1(api.NestedStruct1())
        assert o.get_prop1() == api.NestedStruct1()

    def test_prop2(self):
        o = NestedStruct3Interface()
        o.set_prop2(api.NestedStruct2())
        assert o.get_prop2() == api.NestedStruct2()

    def test_prop3(self):
        o = NestedStruct3Interface()
        o.set_prop3(api.NestedStruct3())
        assert o.get_prop3() == api.NestedStruct3()

    def test_func1(self):
        o = NestedStruct3Interface()
        o.func1(param1=api.NestedStruct1())

    def test_func2(self):
        o = NestedStruct3Interface()
        o.func2(param1=api.NestedStruct1(), param2=api.NestedStruct2())

    def test_func3(self):
        o = NestedStruct3Interface()
        o.func3(param1=api.NestedStruct1(), param2=api.NestedStruct2(), param3=api.NestedStruct3())

