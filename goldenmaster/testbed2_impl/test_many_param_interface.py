
from testbed2_api import api
from testbed2_impl import ManyParamInterface

class TestManyParamInterface:

    def test_func1(self):
        o = ManyParamInterface()
        o.func1(0,)

    def test_func2(self):
        o = ManyParamInterface()
        o.func2(0,0,)

    def test_func3(self):
        o = ManyParamInterface()
        o.func3(0,0,0,)

    def test_func4(self):
        o = ManyParamInterface()
        o.func4(0,0,0,0,)

