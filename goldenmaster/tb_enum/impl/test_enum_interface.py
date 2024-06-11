
from tb_enum.api import api
from tb_enum.impl import EnumInterface

class TestEnumInterface:

    def test_prop0(self):
        o = EnumInterface()
        self.called = False
        o.on_prop0_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop0(api.Enum0.VALUE0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop0() == api.Enum0.VALUE0

    def test_prop1(self):
        o = EnumInterface()
        self.called = False
        o.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop1(api.Enum1.VALUE1)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop1() == api.Enum1.VALUE1

    def test_prop2(self):
        o = EnumInterface()
        self.called = False
        o.on_prop2_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop2(api.Enum2.VALUE2)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop2() == api.Enum2.VALUE2

    def test_prop3(self):
        o = EnumInterface()
        self.called = False
        o.on_prop3_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop3(api.Enum3.VALUE3)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop3() == api.Enum3.VALUE3

    def test_func0(self):
        o = EnumInterface()
        o.func0(param0=api.Enum0.VALUE0)

    def test_func1(self):
        o = EnumInterface()
        o.func1(param1=api.Enum1.VALUE1)

    def test_func2(self):
        o = EnumInterface()
        o.func2(param2=api.Enum2.VALUE2)

    def test_func3(self):
        o = EnumInterface()
        o.func3(param3=api.Enum3.VALUE3)

    def test_sig0(self):
        o = EnumInterface()
        self.called = False
        o.on_sig0 += lambda *args: setattr(self, 'called', True)
        o._sig0(api.Enum0.VALUE0)
        assert self.called == True

    def test_sig1(self):
        o = EnumInterface()
        self.called = False
        o.on_sig1 += lambda *args: setattr(self, 'called', True)
        o._sig1(api.Enum1.VALUE1)
        assert self.called == True

    def test_sig2(self):
        o = EnumInterface()
        self.called = False
        o.on_sig2 += lambda *args: setattr(self, 'called', True)
        o._sig2(api.Enum2.VALUE2)
        assert self.called == True

    def test_sig3(self):
        o = EnumInterface()
        self.called = False
        o.on_sig3 += lambda *args: setattr(self, 'called', True)
        o._sig3(api.Enum3.VALUE3)
        assert self.called == True
