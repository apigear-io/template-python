
from counter.api import api
from counter.impl import Counter
import custom_types.api
import extern_types.api
import vector3d.vector

class TestCounter:

    def test_vector(self):
        o = Counter()
        self.called = False
        o.on_vector_changed += lambda *args: setattr(self, 'called', True)
        o.set_vector(custom_types.api.Vector3D())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_vector() == custom_types.api.Vector3D()

    def test_extern_vector(self):
        o = Counter()
        self.called = False
        o.on_extern_vector_changed += lambda *args: setattr(self, 'called', True)
        o.set_extern_vector(vector3d.vector.Vector())
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_extern_vector() == vector3d.vector.Vector()

    def test_vector_array(self):
        o = Counter()
        self.called = False
        o.on_vector_array_changed += lambda *args: setattr(self, 'called', True)
        o.set_vector_array([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_vector_array() == []

    def test_extern_vector_array(self):
        o = Counter()
        self.called = False
        o.on_extern_vector_array_changed += lambda *args: setattr(self, 'called', True)
        o.set_extern_vector_array([])
        # should not be true since we are not changing the default value
        assert self.called == False
        assert o.get_extern_vector_array() == []

    def test_increment(self):
        o = Counter()
        o.increment(vec=vector3d.vector.Vector())

    def test_increment_array(self):
        o = Counter()
        o.increment_array(vec=[])

    def test_decrement(self):
        o = Counter()
        o.decrement(vec=custom_types.api.Vector3D())

    def test_decrement_array(self):
        o = Counter()
        o.decrement_array(vec=[])

    def test_value_changed(self):
        o = Counter()
        self.called = False
        o.on_value_changed += lambda *args: setattr(self, 'called', True)
        o._value_changed(custom_types.api.Vector3D(), vector3d.vector.Vector(), [], [])
        assert self.called == True
