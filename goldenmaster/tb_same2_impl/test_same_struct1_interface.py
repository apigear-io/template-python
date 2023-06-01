
from tb_same2_api import api
from tb_same2_impl import SameStruct1Interface

class TestSameStruct1Interface:

    def test_prop1(self):
        o = SameStruct1Interface()
        o.set_prop1(api.Struct1())
        assert o.get_prop1() == api.Struct1()

    def test_func1(self):
        o = SameStruct1Interface()
        o.func1(param1=api.Struct1())

