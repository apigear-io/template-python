
from testbed1_api import api
from testbed1_impl import StructInterface

class TestStructInterface:

    def test_prop_bool(self):
        o = StructInterface()
        self.called = False
        o.on_prop_bool_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_bool(api.StructBool())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_bool() == api.StructBool()

    def test_prop_int(self):
        o = StructInterface()
        self.called = False
        o.on_prop_int_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int(api.StructInt())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_int() == api.StructInt()

    def test_prop_float(self):
        o = StructInterface()
        self.called = False
        o.on_prop_float_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_float(api.StructFloat())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_float() == api.StructFloat()

    def test_prop_string(self):
        o = StructInterface()
        self.called = False
        o.on_prop_string_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_string(api.StructString())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_string() == api.StructString()

    def test_func_bool(self):
        o = StructInterface()
        o.func_bool(param_bool=api.StructBool())

    def test_func_int(self):
        o = StructInterface()
        o.func_int(param_int=api.StructInt())

    def test_func_float(self):
        o = StructInterface()
        o.func_float(param_float=api.StructFloat())

    def test_func_string(self):
        o = StructInterface()
        o.func_string(param_string=api.StructString())

    def test_sig_bool(self):
        o = StructInterface()
        self.called = False
        o.on_sig_bool += lambda *args: setattr(self, 'called', True)
        o._sig_bool(api.StructBool())
        assert self.called == True

    def test_sig_int(self):
        o = StructInterface()
        self.called = False
        o.on_sig_int += lambda *args: setattr(self, 'called', True)
        o._sig_int(api.StructInt())
        assert self.called == True

    def test_sig_float(self):
        o = StructInterface()
        self.called = False
        o.on_sig_float += lambda *args: setattr(self, 'called', True)
        o._sig_float(api.StructFloat())
        assert self.called == True

    def test_sig_string(self):
        o = StructInterface()
        self.called = False
        o.on_sig_string += lambda *args: setattr(self, 'called', True)
        o._sig_string(api.StructString())
        assert self.called == True
