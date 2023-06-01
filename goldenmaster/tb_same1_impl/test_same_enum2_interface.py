
from tb_same1_api import api
from tb_same1_impl import SameEnum2Interface

class TestSameEnum2Interface:

    def test_prop1(self):
        o = SameEnum2Interface()
        o.set_prop1(api.Enum1.VALUE1)
        assert o.get_prop1() == api.Enum1.VALUE1

    def test_prop2(self):
        o = SameEnum2Interface()
        o.set_prop2(api.Enum2.VALUE1)
        assert o.get_prop2() == api.Enum2.VALUE1

    def test_func1(self):
        o = SameEnum2Interface()
        o.func1(param1=api.Enum1.VALUE1)

    def test_func2(self):
        o = SameEnum2Interface()
        o.func2(param1=api.Enum1.VALUE1, param2=api.Enum2.VALUE1)

