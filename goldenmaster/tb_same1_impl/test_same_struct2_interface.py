
from tb_same1_api import api
from tb_same1_impl import SameStruct2Interface

class TestSameStruct2Interface:

    def test_func1(self):
        o = SameStruct2Interface()
        o.func1({},)

    def test_func2(self):
        o = SameStruct2Interface()
        o.func2({},{},)

