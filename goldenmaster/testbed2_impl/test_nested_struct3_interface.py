
from testbed2_api import api
from testbed2_impl import NestedStruct3Interface

class TestNestedStruct3Interface:

    def test_func1(self):
        o = NestedStruct3Interface()
        o.func1({},)

    def test_func2(self):
        o = NestedStruct3Interface()
        o.func2({},{},)

    def test_func3(self):
        o = NestedStruct3Interface()
        o.func3({},{},{},)

