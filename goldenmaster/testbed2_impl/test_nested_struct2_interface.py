
from testbed2_api import api
from testbed2_impl import NestedStruct2Interface

class TestNestedStruct2Interface:

    def test_func1(self):
        o = NestedStruct2Interface()
        o.func1(param1={})

    def test_func2(self):
        o = NestedStruct2Interface()
        o.func2(param1={}, param2={})

