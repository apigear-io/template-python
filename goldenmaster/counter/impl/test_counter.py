
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

    def test_increment(self):
        o = Counter()
        o.increment(vec=vector3d.vector.Vector())

    def test_decrement(self):
        o = Counter()
        o.decrement(vec=custom_types.api.Vector3D())
    pass
