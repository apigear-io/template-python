
from testbed2_api import api
from testbed2_impl import ManyParamInterface

class TestManyParamInterface:

    def test_prop1(self):
        o = ManyParamInterface()
        o.set_prop1(0)
        assert o.get_prop1() == 0

    def test_prop2(self):
        o = ManyParamInterface()
        o.set_prop2(0)
        assert o.get_prop2() == 0

    def test_prop3(self):
        o = ManyParamInterface()
        o.set_prop3(0)
        assert o.get_prop3() == 0

    def test_prop4(self):
        o = ManyParamInterface()
        o.set_prop4(0)
        assert o.get_prop4() == 0

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

