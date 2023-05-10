
from tb_same2_api import api
from tb_same2_impl import SameEnum2Interface

class TestSameEnum2Interface:

    def test_func1(self):
        o = SameEnum2Interface()
        o.func1(param1=api.Enum1.VALUE1)

    def test_func2(self):
        o = SameEnum2Interface()
        o.func2(param1=api.Enum1.VALUE1, param2=api.Enum2.VALUE1)

