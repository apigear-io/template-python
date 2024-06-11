from fastapi import APIRouter
from . import shared

router = APIRouter()


counter = shared.CounterState()



@router.post(
    "/counter/counter/increment", 
    response_model=shared.CounterIncrementResponse
)
async def counter_increment(params: shared.CounterIncrementRequest):
    result = counter.increment(params.vec)
    state = shared.CounterState(
        vector = counter.vector,
        extern_vector = counter.extern_vector,
    )
    response = shared.CounterIncrementResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/counter/counter/decrement", 
    response_model=shared.CounterDecrementResponse
)
async def counter_decrement(params: shared.CounterDecrementRequest):
    result = counter.decrement(params.vec)
    state = shared.CounterState(
        vector = counter.vector,
        extern_vector = counter.extern_vector,
    )
    response = shared.CounterDecrementResponse(
        result=result,
        state=state
    )
    return response


