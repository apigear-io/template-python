from fastapi import APIRouter
from . import shared

router = APIRouter()


nam_es = shared.NamEsState()



@router.post(
    "/tb_names/nam_es/some_function", 
    response_model=shared.NamEsSomeFunctionResponse
)
async def nam_es_someFunction(params: shared.Nam_EsSomeFunctionRequest):
    result = nam_es.SOME_FUNCTION(params.some_param)
    state = shared.NamEsState(
        switch = nam_es.switch,
        some_property = nam_es.some_property,
        some_poperty2 = nam_es.some_poperty2,
    )
    response = shared.Nam_EsSomeFunctionResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/tb_names/nam_es/some_function2", 
    response_model=shared.NamEsSomeFunction2Response
)
async def nam_es_someFunction2(params: shared.Nam_EsSomeFunction2Request):
    result = nam_es.Some_Function2(params.some_param)
    state = shared.NamEsState(
        switch = nam_es.switch,
        some_property = nam_es.some_property,
        some_poperty2 = nam_es.some_poperty2,
    )
    response = shared.Nam_EsSomeFunction2Response(
        result=result,
        state=state
    )
    return response


