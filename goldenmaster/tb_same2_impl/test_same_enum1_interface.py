
from tb_same2_api import api
from tb_same2_impl import SameEnum1Interface

class TestSameEnum1Interface:

    def test_prop1(self):
        o = SameEnum1Interface()
        o.set_prop1(api.Enum1.VALUE1)
        assert o.get_prop1() == api.Enum1.VALUE1

    def test_func1(self):
        o = SameEnum1Interface()
        o.func1(param1=api.Enum1.VALUE1)

