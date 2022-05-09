from fastapi import FastAPI, Response
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn

# Create server
app = FastAPI()

# Add static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Index request
@app.get("/", response_class=HTMLResponse)
async def index(res : Response) -> HTMLResponse:
    res.headers["Link"] = "<static/style.css>;rel=stylesheet;media=all"
    return ""

# Run server on direct call
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)