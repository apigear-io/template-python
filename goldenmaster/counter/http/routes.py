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
        vector_array = counter.vector_array,
        extern_vector_array = counter.extern_vector_array,
    )
    response = shared.CounterIncrementResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/counter/counter/increment_array", 
    response_model=shared.CounterIncrementArrayResponse
)
async def counter_incrementArray(params: shared.CounterIncrementArrayRequest):
    result = counter.incrementArray(params.vec)
    state = shared.CounterState(
        vector = counter.vector,
        extern_vector = counter.extern_vector,
        vector_array = counter.vector_array,
        extern_vector_array = counter.extern_vector_array,
    )
    response = shared.CounterIncrementArrayResponse(
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
        vector_array = counter.vector_array,
        extern_vector_array = counter.extern_vector_array,
    )
    response = shared.CounterDecrementResponse(
        result=result,
        state=state
    )
    return response

@router.post(
    "/counter/counter/decrement_array", 
    response_model=shared.CounterDecrementArrayResponse
)
async def counter_decrementArray(params: shared.CounterDecrementArrayRequest):
    result = counter.decrementArray(params.vec)
    state = shared.CounterState(
        vector = counter.vector,
        extern_vector = counter.extern_vector,
        vector_array = counter.vector_array,
        extern_vector_array = counter.extern_vector_array,
    )
    response = shared.CounterDecrementArrayResponse(
        result=result,
        state=state
    )
    return response


