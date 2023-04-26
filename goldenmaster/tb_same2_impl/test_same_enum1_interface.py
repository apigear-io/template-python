
from tb_same2_api import api
from tb_same2_impl import SameEnum1Interface

class TestSameEnum1Interface:

    def test_func1(self):
        o = SameEnum1Interface()
        o.func1(param1=api.Enum1.value1)

