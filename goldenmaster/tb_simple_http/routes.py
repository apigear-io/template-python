from fastapi import APIRouter
from . import shared

router = APIRouter()


simple_interface = shared.SimpleInterfaceState()
simple_array_interface = shared.SimpleArrayInterfaceState()



@router.post(
    "/tb_simple/simple_interface/func_bool", 
    response_model=shared.SimpleInterfaceFuncBoolResponse
)
async def simple_interface_funcBool(params: shared.SimpleInterfaceFuncBoolRequest):
    result = simple_interface.funcBool(params.param_bool)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_float = simple_interface.prop_float,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_interface/func_int", 
    response_model=shared.SimpleInterfaceFuncIntResponse
)
async def simple_interface_funcInt(params: shared.SimpleInterfaceFuncIntRequest):
    result = simple_interface.funcInt(params.param_int)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_float = simple_interface.prop_float,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_interface/func_float", 
    response_model=shared.SimpleInterfaceFuncFloatResponse
)
async def simple_interface_funcFloat(params: shared.SimpleInterfaceFuncFloatRequest):
    result = simple_interface.funcFloat(params.param_float)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_float = simple_interface.prop_float,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_interface/func_string", 
    response_model=shared.SimpleInterfaceFuncStringResponse
)
async def simple_interface_funcString(params: shared.SimpleInterfaceFuncStringRequest):
    result = simple_interface.funcString(params.param_string)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_float = simple_interface.prop_float,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response



@router.post(
    "/tb_simple/simple_array_interface/func_bool", 
    response_model=shared.SimpleArrayInterfaceFuncBoolResponse
)
async def simple_array_interface_funcBool(params: shared.SimpleArrayInterfaceFuncBoolRequest):
    result = simple_array_interface.funcBool(params.param_bool)
    state = shared.SimpleArrayInterfaceState(
        prop_bool = simple_array_interface.prop_bool,
        prop_int = simple_array_interface.prop_int,
        prop_float = simple_array_interface.prop_float,
        prop_string = simple_array_interface.prop_string,
    )
    response = shared.SimpleArrayInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_array_interface/func_int", 
    response_model=shared.SimpleArrayInterfaceFuncIntResponse
)
async def simple_array_interface_funcInt(params: shared.SimpleArrayInterfaceFuncIntRequest):
    result = simple_array_interface.funcInt(params.param_int)
    state = shared.SimpleArrayInterfaceState(
        prop_bool = simple_array_interface.prop_bool,
        prop_int = simple_array_interface.prop_int,
        prop_float = simple_array_interface.prop_float,
        prop_string = simple_array_interface.prop_string,
    )
    response = shared.SimpleArrayInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_array_interface/func_float", 
    response_model=shared.SimpleArrayInterfaceFuncFloatResponse
)
async def simple_array_interface_funcFloat(params: shared.SimpleArrayInterfaceFuncFloatRequest):
    result = simple_array_interface.funcFloat(params.param_float)
    state = shared.SimpleArrayInterfaceState(
        prop_bool = simple_array_interface.prop_bool,
        prop_int = simple_array_interface.prop_int,
        prop_float = simple_array_interface.prop_float,
        prop_string = simple_array_interface.prop_string,
    )
    response = shared.SimpleArrayInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_array_interface/func_string", 
    response_model=shared.SimpleArrayInterfaceFuncStringResponse
)
async def simple_array_interface_funcString(params: shared.SimpleArrayInterfaceFuncStringRequest):
    result = simple_array_interface.funcString(params.param_string)
    state = shared.SimpleArrayInterfaceState(
        prop_bool = simple_array_interface.prop_bool,
        prop_int = simple_array_interface.prop_int,
        prop_float = simple_array_interface.prop_float,
        prop_string = simple_array_interface.prop_string,
    )
    response = shared.SimpleArrayInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response


