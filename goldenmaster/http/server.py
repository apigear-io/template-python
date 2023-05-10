from fastapi import Depends, FastAPI, Header, HTTPException

  
import testbed2_http  
import tb_enum_http  
import tb_same1_http  
import tb_same2_http  
import tb_simple_http  
import testbed1_http  
import tb_empty_http

app = FastAPI()


app.include_router(
    router=testbed2_http.routes.router,
    prefix="/testbed2",
)

app.include_router(
    router=tb_enum_http.routes.router,
    prefix="/tb.enum",
)

app.include_router(
    router=tb_same1_http.routes.router,
    prefix="/tb.same1",
)

app.include_router(
    router=tb_same2_http.routes.router,
    prefix="/tb.same2",
)

app.include_router(
    router=tb_simple_http.routes.router,
    prefix="/tb.simple",
)

app.include_router(
    router=testbed1_http.routes.router,
    prefix="/testbed1",
)

app.include_router(
    router=tb_empty_http.routes.router,
    prefix="/tb.empty",
)
