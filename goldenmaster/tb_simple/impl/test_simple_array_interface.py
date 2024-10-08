
from tb_simple.api import api
from tb_simple.impl import SimpleArrayInterface

class TestSimpleArrayInterface:

    def test_prop_bool(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_prop_bool_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_bool([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_bool() == []

    def test_prop_int(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_prop_int_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_int() == []

    def test_prop_int32(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_prop_int32_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int32([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_int32() == []

    def test_prop_int64(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_prop_int64_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_int64([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_int64() == []

    def test_prop_float(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_prop_float_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_float([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_float() == []

    def test_prop_float32(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_prop_float32_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_float32([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_float32() == []

    def test_prop_float64(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_prop_float64_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_float64([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_float64() == []

    def test_prop_string(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_prop_string_changed += lambda *args: setattr(self, 'called', True)
        o.set_prop_string([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_prop_string() == []

    def test_prop_read_only_string(self):
        o = SimpleArrayInterface()
        assert o.get_prop_read_only_string() == ""

    def test_func_bool(self):
        o = SimpleArrayInterface()
        o.func_bool(param_bool=[])

    def test_func_int(self):
        o = SimpleArrayInterface()
        o.func_int(param_int=[])

    def test_func_int32(self):
        o = SimpleArrayInterface()
        o.func_int32(param_int32=[])

    def test_func_int64(self):
        o = SimpleArrayInterface()
        o.func_int64(param_int64=[])

    def test_func_float(self):
        o = SimpleArrayInterface()
        o.func_float(param_float=[])

    def test_func_float32(self):
        o = SimpleArrayInterface()
        o.func_float32(param_float32=[])

    def test_func_float64(self):
        o = SimpleArrayInterface()
        o.func_float64(param_float=[])

    def test_func_string(self):
        o = SimpleArrayInterface()
        o.func_string(param_string=[])

    def test_sig_bool(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_sig_bool += lambda *args: setattr(self, 'called', True)
        o._sig_bool([])
        assert self.called == True

    def test_sig_int(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_sig_int += lambda *args: setattr(self, 'called', True)
        o._sig_int([])
        assert self.called == True

    def test_sig_int32(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_sig_int32 += lambda *args: setattr(self, 'called', True)
        o._sig_int32([])
        assert self.called == True

    def test_sig_int64(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_sig_int64 += lambda *args: setattr(self, 'called', True)
        o._sig_int64([])
        assert self.called == True

    def test_sig_float(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_sig_float += lambda *args: setattr(self, 'called', True)
        o._sig_float([])
        assert self.called == True

    def test_sig_float32(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_sig_float32 += lambda *args: setattr(self, 'called', True)
        o._sig_float32([])
        assert self.called == True

    def test_sig_float64(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_sig_float64 += lambda *args: setattr(self, 'called', True)
        o._sig_float64([])
        assert self.called == True

    def test_sig_string(self):
        o = SimpleArrayInterface()
        self.called = False
        o.on_sig_string += lambda *args: setattr(self, 'called', True)
        o._sig_string([])
        assert self.called == True
