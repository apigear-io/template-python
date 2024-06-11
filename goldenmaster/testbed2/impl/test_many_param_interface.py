
from testbed2.api import api
from testbed2.impl import ManyParamInterface

class TestManyParamInterface:

    def test_prop1(self):
        o = ManyParamInterface()
        self.called = False
        o.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop1(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop1() == 0

    def test_prop2(self):
        o = ManyParamInterface()
        self.called = False
        o.on_prop2_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop2(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop2() == 0

    def test_prop3(self):
        o = ManyParamInterface()
        self.called = False
        o.on_prop3_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop3(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop3() == 0

    def test_prop4(self):
        o = ManyParamInterface()
        self.called = False
        o.on_prop4_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop4(0)
        # should not be true since we are not changing the default value
        assert self.called == False
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

    def test_sig1(self):
        o = ManyParamInterface()
        self.called = False
        o.on_sig1 += lambda *args: setattr(self, 'called', True)
        o._sig1(0)
        assert self.called == True

    def test_sig2(self):
        o = ManyParamInterface()
        self.called = False
        o.on_sig2 += lambda *args: setattr(self, 'called', True)
        o._sig2(0, 0)
        assert self.called == True

    def test_sig3(self):
        o = ManyParamInterface()
        self.called = False
        o.on_sig3 += lambda *args: setattr(self, 'called', True)
        o._sig3(0, 0, 0)
        assert self.called == True

    def test_sig4(self):
        o = ManyParamInterface()
        self.called = False
        o.on_sig4 += lambda *args: setattr(self, 'called', True)
        o._sig4(0, 0, 0, 0)
        assert self.called == True
