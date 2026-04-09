from fastapi import APIRouter
from . import shared

router = APIRouter()


struct_interface = shared.StructInterfaceState()
struct_array_interface = shared.StructArrayInterfaceState()
struct_array2_interface = shared.StructArray2InterfaceState()



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
        prop_enum = struct_array_interface.prop_enum,
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
        prop_enum = struct_array_interface.prop_enum,
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
        prop_enum = struct_array_interface.prop_enum,
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
        prop_enum = struct_array_interface.prop_enum,
    )
    response = shared.StructArrayInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_array_interface/func_enum", 
    response_model=shared.StructArrayInterfaceFuncEnumResponse
)
async def struct_array_interface_funcEnum(params: shared.StructArrayInterfaceFuncEnumRequest):
    result = struct_array_interface.funcEnum(params.param_enum)
    state = shared.StructArrayInterfaceState(
        prop_bool = struct_array_interface.prop_bool,
        prop_int = struct_array_interface.prop_int,
        prop_float = struct_array_interface.prop_float,
        prop_string = struct_array_interface.prop_string,
        prop_enum = struct_array_interface.prop_enum,
    )
    response = shared.StructArrayInterfaceFuncEnumResponse(
        result=result,
        state=state
    )
    return response



@router.post(
    "/testbed1/struct_array2_interface/func_bool", 
    response_model=shared.StructArray2InterfaceFuncBoolResponse
)
async def struct_array2_interface_funcBool(params: shared.StructArray2InterfaceFuncBoolRequest):
    result = struct_array2_interface.funcBool(params.param_bool)
    state = shared.StructArray2InterfaceState(
        prop_bool = struct_array2_interface.prop_bool,
        prop_int = struct_array2_interface.prop_int,
        prop_float = struct_array2_interface.prop_float,
        prop_string = struct_array2_interface.prop_string,
        prop_enum = struct_array2_interface.prop_enum,
    )
    response = shared.StructArray2InterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_array2_interface/func_int", 
    response_model=shared.StructArray2InterfaceFuncIntResponse
)
async def struct_array2_interface_funcInt(params: shared.StructArray2InterfaceFuncIntRequest):
    result = struct_array2_interface.funcInt(params.param_int)
    state = shared.StructArray2InterfaceState(
        prop_bool = struct_array2_interface.prop_bool,
        prop_int = struct_array2_interface.prop_int,
        prop_float = struct_array2_interface.prop_float,
        prop_string = struct_array2_interface.prop_string,
        prop_enum = struct_array2_interface.prop_enum,
    )
    response = shared.StructArray2InterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_array2_interface/func_float", 
    response_model=shared.StructArray2InterfaceFuncFloatResponse
)
async def struct_array2_interface_funcFloat(params: shared.StructArray2InterfaceFuncFloatRequest):
    result = struct_array2_interface.funcFloat(params.param_float)
    state = shared.StructArray2InterfaceState(
        prop_bool = struct_array2_interface.prop_bool,
        prop_int = struct_array2_interface.prop_int,
        prop_float = struct_array2_interface.prop_float,
        prop_string = struct_array2_interface.prop_string,
        prop_enum = struct_array2_interface.prop_enum,
    )
    response = shared.StructArray2InterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_array2_interface/func_string", 
    response_model=shared.StructArray2InterfaceFuncStringResponse
)
async def struct_array2_interface_funcString(params: shared.StructArray2InterfaceFuncStringRequest):
    result = struct_array2_interface.funcString(params.param_string)
    state = shared.StructArray2InterfaceState(
        prop_bool = struct_array2_interface.prop_bool,
        prop_int = struct_array2_interface.prop_int,
        prop_float = struct_array2_interface.prop_float,
        prop_string = struct_array2_interface.prop_string,
        prop_enum = struct_array2_interface.prop_enum,
    )
    response = shared.StructArray2InterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/testbed1/struct_array2_interface/func_enum", 
    response_model=shared.StructArray2InterfaceFuncEnumResponse
)
async def struct_array2_interface_funcEnum(params: shared.StructArray2InterfaceFuncEnumRequest):
    result = struct_array2_interface.funcEnum(params.param_enum)
    state = shared.StructArray2InterfaceState(
        prop_bool = struct_array2_interface.prop_bool,
        prop_int = struct_array2_interface.prop_int,
        prop_float = struct_array2_interface.prop_float,
        prop_string = struct_array2_interface.prop_string,
        prop_enum = struct_array2_interface.prop_enum,
    )
    response = shared.StructArray2InterfaceFuncEnumResponse(
        result=result,
        state=state
    )
    return response


