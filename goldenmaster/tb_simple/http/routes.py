from fastapi import APIRouter
from . import shared

router = APIRouter()


void_interface = shared.VoidInterfaceState()
simple_interface = shared.SimpleInterfaceState()
simple_array_interface = shared.SimpleArrayInterfaceState()
no_properties_interface = shared.NoPropertiesInterfaceState()
no_operations_interface = shared.NoOperationsInterfaceState()
no_signals_interface = shared.NoSignalsInterfaceState()



@router.post(
    "/tb_simple/void_interface/func_void", 
    response_model=shared.VoidInterfaceFuncVoidResponse
)
async def void_interface_funcVoid(params: shared.VoidInterfaceFuncVoidRequest):
    result = void_interface.funcVoid()
    state = shared.VoidInterfaceState(
    )
    response = shared.VoidInterfaceFuncVoidResponse(
        result=result,
        state=state
    )
    return response



@router.post(
    "/tb_simple/simple_interface/func_no_return_value", 
    response_model=shared.SimpleInterfaceFuncNoReturnValueResponse
)
async def simple_interface_funcNoReturnValue(params: shared.SimpleInterfaceFuncNoReturnValueRequest):
    result = simple_interface.funcNoReturnValue(params.param_bool)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncNoReturnValueResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_interface/func_bool", 
    response_model=shared.SimpleInterfaceFuncBoolResponse
)
async def simple_interface_funcBool(params: shared.SimpleInterfaceFuncBoolRequest):
    result = simple_interface.funcBool(params.param_bool)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
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
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_interface/func_int32", 
    response_model=shared.SimpleInterfaceFuncInt32Response
)
async def simple_interface_funcInt32(params: shared.SimpleInterfaceFuncInt32Request):
    result = simple_interface.funcInt32(params.param_int32)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncInt32Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_interface/func_int64", 
    response_model=shared.SimpleInterfaceFuncInt64Response
)
async def simple_interface_funcInt64(params: shared.SimpleInterfaceFuncInt64Request):
    result = simple_interface.funcInt64(params.param_int64)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncInt64Response(
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
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_interface/func_float32", 
    response_model=shared.SimpleInterfaceFuncFloat32Response
)
async def simple_interface_funcFloat32(params: shared.SimpleInterfaceFuncFloat32Request):
    result = simple_interface.funcFloat32(params.param_float32)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncFloat32Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_interface/func_float64", 
    response_model=shared.SimpleInterfaceFuncFloat64Response
)
async def simple_interface_funcFloat64(params: shared.SimpleInterfaceFuncFloat64Request):
    result = simple_interface.funcFloat64(params.param_float)
    state = shared.SimpleInterfaceState(
        prop_bool = simple_interface.prop_bool,
        prop_int = simple_interface.prop_int,
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
        prop_string = simple_interface.prop_string,
    )
    response = shared.SimpleInterfaceFuncFloat64Response(
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
        prop_int32 = simple_interface.prop_int32,
        prop_int64 = simple_interface.prop_int64,
        prop_float = simple_interface.prop_float,
        prop_float32 = simple_interface.prop_float32,
        prop_float64 = simple_interface.prop_float64,
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
        prop_int32 = simple_array_interface.prop_int32,
        prop_int64 = simple_array_interface.prop_int64,
        prop_float = simple_array_interface.prop_float,
        prop_float32 = simple_array_interface.prop_float32,
        prop_float64 = simple_array_interface.prop_float64,
        prop_string = simple_array_interface.prop_string,
        prop_read_only_string = simple_array_interface.prop_read_only_string,
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
        prop_int32 = simple_array_interface.prop_int32,
        prop_int64 = simple_array_interface.prop_int64,
        prop_float = simple_array_interface.prop_float,
        prop_float32 = simple_array_interface.prop_float32,
        prop_float64 = simple_array_interface.prop_float64,
        prop_string = simple_array_interface.prop_string,
        prop_read_only_string = simple_array_interface.prop_read_only_string,
    )
    response = shared.SimpleArrayInterfaceFuncIntResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_array_interface/func_int32", 
    response_model=shared.SimpleArrayInterfaceFuncInt32Response
)
async def simple_array_interface_funcInt32(params: shared.SimpleArrayInterfaceFuncInt32Request):
    result = simple_array_interface.funcInt32(params.param_int32)
    state = shared.SimpleArrayInterfaceState(
        prop_bool = simple_array_interface.prop_bool,
        prop_int = simple_array_interface.prop_int,
        prop_int32 = simple_array_interface.prop_int32,
        prop_int64 = simple_array_interface.prop_int64,
        prop_float = simple_array_interface.prop_float,
        prop_float32 = simple_array_interface.prop_float32,
        prop_float64 = simple_array_interface.prop_float64,
        prop_string = simple_array_interface.prop_string,
        prop_read_only_string = simple_array_interface.prop_read_only_string,
    )
    response = shared.SimpleArrayInterfaceFuncInt32Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_array_interface/func_int64", 
    response_model=shared.SimpleArrayInterfaceFuncInt64Response
)
async def simple_array_interface_funcInt64(params: shared.SimpleArrayInterfaceFuncInt64Request):
    result = simple_array_interface.funcInt64(params.param_int64)
    state = shared.SimpleArrayInterfaceState(
        prop_bool = simple_array_interface.prop_bool,
        prop_int = simple_array_interface.prop_int,
        prop_int32 = simple_array_interface.prop_int32,
        prop_int64 = simple_array_interface.prop_int64,
        prop_float = simple_array_interface.prop_float,
        prop_float32 = simple_array_interface.prop_float32,
        prop_float64 = simple_array_interface.prop_float64,
        prop_string = simple_array_interface.prop_string,
        prop_read_only_string = simple_array_interface.prop_read_only_string,
    )
    response = shared.SimpleArrayInterfaceFuncInt64Response(
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
        prop_int32 = simple_array_interface.prop_int32,
        prop_int64 = simple_array_interface.prop_int64,
        prop_float = simple_array_interface.prop_float,
        prop_float32 = simple_array_interface.prop_float32,
        prop_float64 = simple_array_interface.prop_float64,
        prop_string = simple_array_interface.prop_string,
        prop_read_only_string = simple_array_interface.prop_read_only_string,
    )
    response = shared.SimpleArrayInterfaceFuncFloatResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_array_interface/func_float32", 
    response_model=shared.SimpleArrayInterfaceFuncFloat32Response
)
async def simple_array_interface_funcFloat32(params: shared.SimpleArrayInterfaceFuncFloat32Request):
    result = simple_array_interface.funcFloat32(params.param_float32)
    state = shared.SimpleArrayInterfaceState(
        prop_bool = simple_array_interface.prop_bool,
        prop_int = simple_array_interface.prop_int,
        prop_int32 = simple_array_interface.prop_int32,
        prop_int64 = simple_array_interface.prop_int64,
        prop_float = simple_array_interface.prop_float,
        prop_float32 = simple_array_interface.prop_float32,
        prop_float64 = simple_array_interface.prop_float64,
        prop_string = simple_array_interface.prop_string,
        prop_read_only_string = simple_array_interface.prop_read_only_string,
    )
    response = shared.SimpleArrayInterfaceFuncFloat32Response(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/simple_array_interface/func_float64", 
    response_model=shared.SimpleArrayInterfaceFuncFloat64Response
)
async def simple_array_interface_funcFloat64(params: shared.SimpleArrayInterfaceFuncFloat64Request):
    result = simple_array_interface.funcFloat64(params.param_float)
    state = shared.SimpleArrayInterfaceState(
        prop_bool = simple_array_interface.prop_bool,
        prop_int = simple_array_interface.prop_int,
        prop_int32 = simple_array_interface.prop_int32,
        prop_int64 = simple_array_interface.prop_int64,
        prop_float = simple_array_interface.prop_float,
        prop_float32 = simple_array_interface.prop_float32,
        prop_float64 = simple_array_interface.prop_float64,
        prop_string = simple_array_interface.prop_string,
        prop_read_only_string = simple_array_interface.prop_read_only_string,
    )
    response = shared.SimpleArrayInterfaceFuncFloat64Response(
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
        prop_int32 = simple_array_interface.prop_int32,
        prop_int64 = simple_array_interface.prop_int64,
        prop_float = simple_array_interface.prop_float,
        prop_float32 = simple_array_interface.prop_float32,
        prop_float64 = simple_array_interface.prop_float64,
        prop_string = simple_array_interface.prop_string,
        prop_read_only_string = simple_array_interface.prop_read_only_string,
    )
    response = shared.SimpleArrayInterfaceFuncStringResponse(
        result=result,
        state=state
    )
    return response



@router.post(
    "/tb_simple/no_properties_interface/func_void", 
    response_model=shared.NoPropertiesInterfaceFuncVoidResponse
)
async def no_properties_interface_funcVoid(params: shared.NoPropertiesInterfaceFuncVoidRequest):
    result = no_properties_interface.funcVoid()
    state = shared.NoPropertiesInterfaceState(
    )
    response = shared.NoPropertiesInterfaceFuncVoidResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/no_properties_interface/func_bool", 
    response_model=shared.NoPropertiesInterfaceFuncBoolResponse
)
async def no_properties_interface_funcBool(params: shared.NoPropertiesInterfaceFuncBoolRequest):
    result = no_properties_interface.funcBool(params.param_bool)
    state = shared.NoPropertiesInterfaceState(
    )
    response = shared.NoPropertiesInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response





@router.post(
    "/tb_simple/no_signals_interface/func_void", 
    response_model=shared.NoSignalsInterfaceFuncVoidResponse
)
async def no_signals_interface_funcVoid(params: shared.NoSignalsInterfaceFuncVoidRequest):
    result = no_signals_interface.funcVoid()
    state = shared.NoSignalsInterfaceState(
        prop_bool = no_signals_interface.prop_bool,
        prop_int = no_signals_interface.prop_int,
    )
    response = shared.NoSignalsInterfaceFuncVoidResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_simple/no_signals_interface/func_bool", 
    response_model=shared.NoSignalsInterfaceFuncBoolResponse
)
async def no_signals_interface_funcBool(params: shared.NoSignalsInterfaceFuncBoolRequest):
    result = no_signals_interface.funcBool(params.param_bool)
    state = shared.NoSignalsInterfaceState(
        prop_bool = no_signals_interface.prop_bool,
        prop_int = no_signals_interface.prop_int,
    )
    response = shared.NoSignalsInterfaceFuncBoolResponse(
        result=result,
        state=state
    )
    return response


