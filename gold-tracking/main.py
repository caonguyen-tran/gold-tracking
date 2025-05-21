from fastapi import FastAPI
from api.user_router import router as user_router
import os
import uvicorn

from exception.exception_handler import register_exception_handlers

app = FastAPI(title="Gold Tracking")
prefix_path="/api/v1"
app.include_router(user_router, prefix=prefix_path)

# register exception response when cause error
register_exception_handlers(app)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8899))
    uvicorn.run("main:app", host="localhost", port=port, reload=True)