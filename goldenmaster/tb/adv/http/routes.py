from fastapi import APIRouter



from tb.adv import ManyParamInterface
from tb.adv import NestedStruct1Interface
from tb.adv import NestedStruct2Interface
from tb.adv import NestedStruct3Interface

from . import shared

router = APIRouter()


many_param_interface = ManyParamInterface()
nested_struct_1_interface = NestedStruct1Interface()
nested_struct_2_interface = NestedStruct2Interface()
nested_struct_3_interface = NestedStruct3Interface()










