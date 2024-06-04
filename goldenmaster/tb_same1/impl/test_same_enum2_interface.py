
from tb_same1.api import api
from tb_same1.impl import SameEnum2Interface

class TestSameEnum2Interface:

    def test_prop1(self):
        o = SameEnum2Interface()
        self.called = False
        o.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop1(api.Enum1.VALUE1)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop1() == api.Enum1.VALUE1

    def test_prop2(self):
        o = SameEnum2Interface()
        self.called = False
        o.on_prop2_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop2(api.Enum2.VALUE1)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop2() == api.Enum2.VALUE1

    def test_func1(self):
        o = SameEnum2Interface()
        o.func1(param1=api.Enum1.VALUE1)

    def test_func2(self):
        o = SameEnum2Interface()
        o.func2(param1=api.Enum1.VALUE1, param2=api.Enum2.VALUE1)

    def test_sig1(self):
        o = SameEnum2Interface()
        self.called = False
        o.on_sig1 += lambda *args: setattr(self, 'called', True)
        o._sig1(api.Enum1.VALUE1)
        assert self.called == True

    def test_sig2(self):
        o = SameEnum2Interface()
        self.called = False
        o.on_sig2 += lambda *args: setattr(self, 'called', True)
        o._sig2(api.Enum1.VALUE1, api.Enum2.VALUE1)
        assert self.called == True
