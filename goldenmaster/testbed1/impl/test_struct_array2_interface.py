
from testbed1.api import api
from testbed1.impl import StructArray2Interface

class TestStructArray2Interface:

    def test_prop_bool(self):
        o = StructArray2Interface()
        self.called = False
        o.on_prop_bool_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_bool(api.StructBoolWithArray())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_bool() == api.StructBoolWithArray()

    def test_prop_int(self):
        o = StructArray2Interface()
        self.called = False
        o.on_prop_int_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int(api.StructIntWithArray())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_int() == api.StructIntWithArray()

    def test_prop_float(self):
        o = StructArray2Interface()
        self.called = False
        o.on_prop_float_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_float(api.StructFloatWithArray())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_float() == api.StructFloatWithArray()

    def test_prop_string(self):
        o = StructArray2Interface()
        self.called = False
        o.on_prop_string_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_string(api.StructStringWithArray())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_string() == api.StructStringWithArray()

    def test_prop_enum(self):
        o = StructArray2Interface()
        self.called = False
        o.on_prop_enum_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_enum(api.StructEnumWithArray())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_enum() == api.StructEnumWithArray()

    def test_func_bool(self):
        o = StructArray2Interface()
        o.func_bool(param_bool=api.StructBoolWithArray())

    def test_func_int(self):
        o = StructArray2Interface()
        o.func_int(param_int=api.StructIntWithArray())

    def test_func_float(self):
        o = StructArray2Interface()
        o.func_float(param_float=api.StructFloatWithArray())

    def test_func_string(self):
        o = StructArray2Interface()
        o.func_string(param_string=api.StructStringWithArray())

    def test_func_enum(self):
        o = StructArray2Interface()
        o.func_enum(param_enum=api.StructEnumWithArray())

    def test_sig_bool(self):
        o = StructArray2Interface()
        self.called = False
        o.on_sig_bool += lambda *args: setattr(self, 'called', True)
        o._sig_bool(api.StructBoolWithArray())
        assert self.called == True

    def test_sig_int(self):
        o = StructArray2Interface()
        self.called = False
        o.on_sig_int += lambda *args: setattr(self, 'called', True)
        o._sig_int(api.StructIntWithArray())
        assert self.called == True

    def test_sig_float(self):
        o = StructArray2Interface()
        self.called = False
        o.on_sig_float += lambda *args: setattr(self, 'called', True)
        o._sig_float(api.StructFloatWithArray())
        assert self.called == True

    def test_sig_string(self):
        o = StructArray2Interface()
        self.called = False
        o.on_sig_string += lambda *args: setattr(self, 'called', True)
        o._sig_string(api.StructStringWithArray())
        assert self.called == True
