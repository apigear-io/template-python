from fastapi import APIRouter



from testbed2 import ManyParamInterface
from testbed2 import NestedStruct1Interface
from testbed2 import NestedStruct2Interface
from testbed2 import NestedStruct3Interface

from . import shared

router = APIRouter()


many_param_interface = ManyParamInterface()
nested_struct1_interface = NestedStruct1Interface()
nested_struct2_interface = NestedStruct2Interface()
nested_struct3_interface = NestedStruct3Interface()



@router.post(
    "/many_param_interface/func1", 
    response_model=shared.ManyParamInterfaceFunc1Response
)
async def many_param_interface_func1(params: shared.ManyParamInterfaceFunc1Request):
    result = many_param_interface.func1(params.param1)
    state = shared.ManyParamInterfaceState(
        prop1 = many_param_interface.prop1,
        prop2 = many_param_interface.prop2,
        prop3 = many_param_interface.prop3,
        prop4 = many_param_interface.prop4,
    )
    response = shared.ManyParamInterfaceFunc1Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/many_param_interface/func2", 
    response_model=shared.ManyParamInterfaceFunc2Response
)
async def many_param_interface_func2(params: shared.ManyParamInterfaceFunc2Request):
    result = many_param_interface.func2(params.param1, params.param2)
    state = shared.ManyParamInterfaceState(
        prop1 = many_param_interface.prop1,
        prop2 = many_param_interface.prop2,
        prop3 = many_param_interface.prop3,
        prop4 = many_param_interface.prop4,
    )
    response = shared.ManyParamInterfaceFunc2Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/many_param_interface/func3", 
    response_model=shared.ManyParamInterfaceFunc3Response
)
async def many_param_interface_func3(params: shared.ManyParamInterfaceFunc3Request):
    result = many_param_interface.func3(params.param1, params.param2, params.param3)
    state = shared.ManyParamInterfaceState(
        prop1 = many_param_interface.prop1,
        prop2 = many_param_interface.prop2,
        prop3 = many_param_interface.prop3,
        prop4 = many_param_interface.prop4,
    )
    response = shared.ManyParamInterfaceFunc3Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/many_param_interface/func4", 
    response_model=shared.ManyParamInterfaceFunc4Response
)
async def many_param_interface_func4(params: shared.ManyParamInterfaceFunc4Request):
    result = many_param_interface.func4(params.param1, params.param2, params.param3, params.param4)
    state = shared.ManyParamInterfaceState(
        prop1 = many_param_interface.prop1,
        prop2 = many_param_interface.prop2,
        prop3 = many_param_interface.prop3,
        prop4 = many_param_interface.prop4,
    )
    response = shared.ManyParamInterfaceFunc4Response(
        result=result,
        state=state
    )
    return response



@router.post(
    "/nested_struct1_interface/func1", 
    response_model=shared.NestedStruct1InterfaceFunc1Response
)
async def nested_struct1_interface_func1(params: shared.NestedStruct1InterfaceFunc1Request):
    result = nested_struct1_interface.func1(params.param1)
    state = shared.NestedStruct1InterfaceState(
        prop1 = nested_struct1_interface.prop1,
    )
    response = shared.NestedStruct1InterfaceFunc1Response(
        result=result,
        state=state
    )
    return response



@router.post(
    "/nested_struct2_interface/func1", 
    response_model=shared.NestedStruct2InterfaceFunc1Response
)
async def nested_struct2_interface_func1(params: shared.NestedStruct2InterfaceFunc1Request):
    result = nested_struct2_interface.func1(params.param1)
    state = shared.NestedStruct2InterfaceState(
        prop1 = nested_struct2_interface.prop1,
        prop2 = nested_struct2_interface.prop2,
    )
    response = shared.NestedStruct2InterfaceFunc1Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/nested_struct2_interface/func2", 
    response_model=shared.NestedStruct2InterfaceFunc2Response
)
async def nested_struct2_interface_func2(params: shared.NestedStruct2InterfaceFunc2Request):
    result = nested_struct2_interface.func2(params.param1, params.param2)
    state = shared.NestedStruct2InterfaceState(
        prop1 = nested_struct2_interface.prop1,
        prop2 = nested_struct2_interface.prop2,
    )
    response = shared.NestedStruct2InterfaceFunc2Response(
        result=result,
        state=state
    )
    return response



@router.post(
    "/nested_struct3_interface/func1", 
    response_model=shared.NestedStruct3InterfaceFunc1Response
)
async def nested_struct3_interface_func1(params: shared.NestedStruct3InterfaceFunc1Request):
    result = nested_struct3_interface.func1(params.param1)
    state = shared.NestedStruct3InterfaceState(
        prop1 = nested_struct3_interface.prop1,
        prop2 = nested_struct3_interface.prop2,
        prop3 = nested_struct3_interface.prop3,
    )
    response = shared.NestedStruct3InterfaceFunc1Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/nested_struct3_interface/func2", 
    response_model=shared.NestedStruct3InterfaceFunc2Response
)
async def nested_struct3_interface_func2(params: shared.NestedStruct3InterfaceFunc2Request):
    result = nested_struct3_interface.func2(params.param1, params.param2)
    state = shared.NestedStruct3InterfaceState(
        prop1 = nested_struct3_interface.prop1,
        prop2 = nested_struct3_interface.prop2,
        prop3 = nested_struct3_interface.prop3,
    )
    response = shared.NestedStruct3InterfaceFunc2Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/nested_struct3_interface/func3", 
    response_model=shared.NestedStruct3InterfaceFunc3Response
)
async def nested_struct3_interface_func3(params: shared.NestedStruct3InterfaceFunc3Request):
    result = nested_struct3_interface.func3(params.param1, params.param2, params.param3)
    state = shared.NestedStruct3InterfaceState(
        prop1 = nested_struct3_interface.prop1,
        prop2 = nested_struct3_interface.prop2,
        prop3 = nested_struct3_interface.prop3,
    )
    response = shared.NestedStruct3InterfaceFunc3Response(
        result=result,
        state=state
    )
    return response


