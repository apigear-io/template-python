
from tb_same2.api import api
from tb_same2.impl import SameStruct2Interface

class TestSameStruct2Interface:

    def test_prop1(self):
        o = SameStruct2Interface()
        self.called = False
        o.on_prop1_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop1(api.Struct2())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop1() == api.Struct2()

    def test_prop2(self):
        o = SameStruct2Interface()
        self.called = False
        o.on_prop2_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop2(api.Struct2())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop2() == api.Struct2()

    def test_func1(self):
        o = SameStruct2Interface()
        o.func1(param1=api.Struct1())

    def test_func2(self):
        o = SameStruct2Interface()
        o.func2(param1=api.Struct1(), param2=api.Struct2())

    def test_sig1(self):
        o = SameStruct2Interface()
        self.called = False
        o.on_sig1 += lambda *args: setattr(self, 'called', True)
        o._sig1(api.Struct1())
        assert self.called == True

    def test_sig2(self):
        o = SameStruct2Interface()
        self.called = False
        o.on_sig2 += lambda *args: setattr(self, 'called', True)
        o._sig2(api.Struct1(), api.Struct2())
        assert self.called == True
