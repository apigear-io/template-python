from fastapi import Depends, FastAPI, Header, HTTPException

  
import testbed2.http  
import tb_enum.http  
import tb_same1.http  
import tb_same2.http  
import tb_simple.http  
import testbed1.http  
import tb_names.http  
import custom_types.http  
import extern_types.http  
import counter.http  
import tb_empty.http

app = FastAPI()


app.include_router(
    router=testbed2.http.routes.router,
    prefix="/testbed2",
)

app.include_router(
    router=tb_enum.http.routes.router,
    prefix="/tb.enum",
)

app.include_router(
    router=tb_same1.http.routes.router,
    prefix="/tb.same1",
)

app.include_router(
    router=tb_same2.http.routes.router,
    prefix="/tb.same2",
)

app.include_router(
    router=tb_simple.http.routes.router,
    prefix="/tb.simple",
)

app.include_router(
    router=testbed1.http.routes.router,
    prefix="/testbed1",
)

app.include_router(
    router=tb_names.http.routes.router,
    prefix="/tb.names",
)

app.include_router(
    router=custom_types.http.routes.router,
    prefix="/custom_types",
)

app.include_router(
    router=extern_types.http.routes.router,
    prefix="/extern_types",
)

app.include_router(
    router=counter.http.routes.router,
    prefix="/counter",
)

app.include_router(
    router=tb_empty.http.routes.router,
    prefix="/tb.empty",
)
