from fastapi import APIRouter
from . import shared

router = APIRouter()


struct_interface = shared.StructInterfaceState()
struct_array_interface = shared.StructArrayInterfaceState()



@router.post(
    "/testbed1/struct_interface/func_bool", 
    response_model=shared.StructInterfaceFuncBoolResponse
)
async def struct_interface_funcBool(params: shared.StructInterfaceFuncBoolRequest):
    result = struct_interface.funcBool(params.param_bool)
    state = shared.StructInterfaceState(
        prop_bool = struct_interface.prop_bool,
        prop_int = struct_interface.prop_int,
        prop_float = struct_interface.prop_float,
        prop_string = struct_interface.prop_string,
    )
    response = shared.StructInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_interface/func_int", 
    response_model=shared.StructInterfaceFuncIntResponse
)
async def struct_interface_funcInt(params: shared.StructInterfaceFuncIntRequest):
    result = struct_interface.funcInt(params.param_int)
    state = shared.StructInterfaceState(
        prop_bool = struct_interface.prop_bool,
        prop_int = struct_interface.prop_int,
        prop_float = struct_interface.prop_float,
        prop_string = struct_interface.prop_string,
    )
    response = shared.StructInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_interface/func_float", 
    response_model=shared.StructInterfaceFuncFloatResponse
)
async def struct_interface_funcFloat(params: shared.StructInterfaceFuncFloatRequest):
    result = struct_interface.funcFloat(params.param_float)
    state = shared.StructInterfaceState(
        prop_bool = struct_interface.prop_bool,
        prop_int = struct_interface.prop_int,
        prop_float = struct_interface.prop_float,
        prop_string = struct_interface.prop_string,
    )
    response = shared.StructInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_interface/func_string", 
    response_model=shared.StructInterfaceFuncStringResponse
)
async def struct_interface_funcString(params: shared.StructInterfaceFuncStringRequest):
    result = struct_interface.funcString(params.param_string)
    state = shared.StructInterfaceState(
        prop_bool = struct_interface.prop_bool,
        prop_int = struct_interface.prop_int,
        prop_float = struct_interface.prop_float,
        prop_string = struct_interface.prop_string,
    )
    response = shared.StructInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response



@router.post(
    "/testbed1/struct_array_interface/func_bool", 
    response_model=shared.StructArrayInterfaceFuncBoolResponse
)
async def struct_array_interface_funcBool(params: shared.StructArrayInterfaceFuncBoolRequest):
    result = struct_array_interface.funcBool(params.param_bool)
    state = shared.StructArrayInterfaceState(
        prop_bool = struct_array_interface.prop_bool,
        prop_int = struct_array_interface.prop_int,
        prop_float = struct_array_interface.prop_float,
        prop_string = struct_array_interface.prop_string,
    )
    response = shared.StructArrayInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_array_interface/func_int", 
    response_model=shared.StructArrayInterfaceFuncIntResponse
)
async def struct_array_interface_funcInt(params: shared.StructArrayInterfaceFuncIntRequest):
    result = struct_array_interface.funcInt(params.param_int)
    state = shared.StructArrayInterfaceState(
        prop_bool = struct_array_interface.prop_bool,
        prop_int = struct_array_interface.prop_int,
        prop_float = struct_array_interface.prop_float,
        prop_string = struct_array_interface.prop_string,
    )
    response = shared.StructArrayInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_array_interface/func_float", 
    response_model=shared.StructArrayInterfaceFuncFloatResponse
)
async def struct_array_interface_funcFloat(params: shared.StructArrayInterfaceFuncFloatRequest):
    result = struct_array_interface.funcFloat(params.param_float)
    state = shared.StructArrayInterfaceState(
        prop_bool = struct_array_interface.prop_bool,
        prop_int = struct_array_interface.prop_int,
        prop_float = struct_array_interface.prop_float,
        prop_string = struct_array_interface.prop_string,
    )
    response = shared.StructArrayInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_array_interface/func_string", 
    response_model=shared.StructArrayInterfaceFuncStringResponse
)
async def struct_array_interface_funcString(params: shared.StructArrayInterfaceFuncStringRequest):
    result = struct_array_interface.funcString(params.param_string)
    state = shared.StructArrayInterfaceState(
        prop_bool = struct_array_interface.prop_bool,
        prop_int = struct_array_interface.prop_int,
        prop_float = struct_array_interface.prop_float,
        prop_string = struct_array_interface.prop_string,
    )
    response = shared.StructArrayInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response


