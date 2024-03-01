
from tb_same2_api import api
from tb_same2_impl import SameEnum1Interface

class TestSameEnum1Interface:

    def test_prop1(self):
        o = SameEnum1Interface()
        self.called = False
        o.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop1(api.Enum1.VALUE1)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop1() == api.Enum1.VALUE1

    def test_func1(self):
        o = SameEnum1Interface()
        o.func1(param1=api.Enum1.VALUE1)

    def test_sig1(self):
        o = SameEnum1Interface()
        self.called = False
        o.on_sig1 += lambda *args: setattr(self, 'called', True)
        o._sig1(api.Enum1.VALUE1)
        assert self.called == True
