from fastapi import FastAPI, WebSocket
app = FastAPI()
@app.websocket("/ws/echo")
async def websocket_echo(websocket: WebSocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        await websocket.send_text(f"Echo: {message}")