
from tb_simple.api import api
from tb_simple.impl import SimpleInterface

class TestSimpleInterface:

    def test_prop_bool(self):
        o = SimpleInterface()
        self.called = False
        o.on_prop_bool_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_bool(False)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_bool() == False

    def test_prop_int(self):
        o = SimpleInterface()
        self.called = False
        o.on_prop_int_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_int() == 0

    def test_prop_int32(self):
        o = SimpleInterface()
        self.called = False
        o.on_prop_int32_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int32(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_int32() == 0

    def test_prop_int64(self):
        o = SimpleInterface()
        self.called = False
        o.on_prop_int64_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int64(0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_int64() == 0

    def test_prop_float(self):
        o = SimpleInterface()
        self.called = False
        o.on_prop_float_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_float(0.0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_float() == 0.0

    def test_prop_float32(self):
        o = SimpleInterface()
        self.called = False
        o.on_prop_float32_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_float32(0.0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_float32() == 0.0

    def test_prop_float64(self):
        o = SimpleInterface()
        self.called = False
        o.on_prop_float64_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_float64(0.0)
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_float64() == 0.0

    def test_prop_string(self):
        o = SimpleInterface()
        self.called = False
        o.on_prop_string_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_string("")
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_string() == ""

    def test_prop_read_only_string(self):
        o = SimpleInterface()
        assert o.get_prop_read_only_string() == ""

    def test_func_void(self):
        o = SimpleInterface()
        o.func_void()

    def test_func_bool(self):
        o = SimpleInterface()
        o.func_bool(param_bool=False)

    def test_func_int(self):
        o = SimpleInterface()
        o.func_int(param_int=0)

    def test_func_int32(self):
        o = SimpleInterface()
        o.func_int32(param_int32=0)

    def test_func_int64(self):
        o = SimpleInterface()
        o.func_int64(param_int64=0)

    def test_func_float(self):
        o = SimpleInterface()
        o.func_float(param_float=0.0)

    def test_func_float32(self):
        o = SimpleInterface()
        o.func_float32(param_float32=0.0)

    def test_func_float64(self):
        o = SimpleInterface()
        o.func_float64(param_float=0.0)

    def test_func_string(self):
        o = SimpleInterface()
        o.func_string(param_string="")

    def test_sig_void(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_void += lambda *args: setattr(self, 'called', True)
        o._sig_void()
        assert self.called == True

    def test_sig_bool(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_bool += lambda *args: setattr(self, 'called', True)
        o._sig_bool(False)
        assert self.called == True

    def test_sig_int(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_int += lambda *args: setattr(self, 'called', True)
        o._sig_int(0)
        assert self.called == True

    def test_sig_int32(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_int32 += lambda *args: setattr(self, 'called', True)
        o._sig_int32(0)
        assert self.called == True

    def test_sig_int64(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_int64 += lambda *args: setattr(self, 'called', True)
        o._sig_int64(0)
        assert self.called == True

    def test_sig_float(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_float += lambda *args: setattr(self, 'called', True)
        o._sig_float(0.0)
        assert self.called == True

    def test_sig_float32(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_float32 += lambda *args: setattr(self, 'called', True)
        o._sig_float32(0.0)
        assert self.called == True

    def test_sig_float64(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_float64 += lambda *args: setattr(self, 'called', True)
        o._sig_float64(0.0)
        assert self.called == True

    def test_sig_string(self):
        o = SimpleInterface()
        self.called = False
        o.on_sig_string += lambda *args: setattr(self, 'called', True)
        o._sig_string("")
        assert self.called == True
