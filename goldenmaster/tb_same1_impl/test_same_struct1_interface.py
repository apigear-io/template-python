
from tb_same1_api import api
from tb_same1_impl import SameStruct1Interface

class TestSameStruct1Interface:

    def test_func1(self):
        o = SameStruct1Interface()
        o.func1(param1={})
