
from testbed2_api import api
from testbed2_impl import NestedStruct1Interface

class TestNestedStruct1Interface:

    def test_func1(self):
        o = NestedStruct1Interface()
        o.func1(param1={})

