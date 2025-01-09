from fastapi import FastAPI
from routers import root_router
app = FastAPI(

)

app.include_router(root_router)