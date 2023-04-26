
from testbed2_api import api
from testbed2_impl import ManyParamInterface

class TestManyParamInterface:

    def test_func1(self):
        o = ManyParamInterface()
        o.func1(param1=0)

    def test_func2(self):
        o = ManyParamInterface()
        o.func2(param1=0, param2=0)

    def test_func3(self):
        o = ManyParamInterface()
        o.func3(param1=0, param2=0, param3=0)

    def test_func4(self):
        o = ManyParamInterface()
        o.func4(param1=0, param2=0, param3=0, param4=0)

