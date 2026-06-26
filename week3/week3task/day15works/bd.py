from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            message = await websocket.receive_text()

            # Send back to sender
            await websocket.send_text(f"You said: {message}")

            # Broadcast to others
            for client in clients:
                if client != websocket:
                    await client.send_text(f"Broadcast: {message}")

    except WebSocketDisconnect:
        clients.remove(websocket)