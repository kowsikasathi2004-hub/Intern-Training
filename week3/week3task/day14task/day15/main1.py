from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

from sse_starlette.sse import EventSourceResponse

import asyncio
import datetime

app = FastAPI()
clients = []
@app.get("/")
def home():
    return {"message": "FastAPI WebSocket & SSE Running Successfully!"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await websocket.accept()

    clients.append(websocket)

    try:

        while True:

            message = await websocket.receive_text()

            # Echo back to sender
            await websocket.send_text(f"You said: {message}")

            # Broadcast to all connected clients
            for client in clients:

                await client.send_text(f"Broadcast: {message}")

    except WebSocketDisconnect:

        clients.remove(websocket)

async def counter():

    count = 1

    while True:

        yield {
            "event": "counter",
            "data": f"Counter : {count}"
        }

        count += 1

        await asyncio.sleep(1)


@app.get("/events")
async def events():

    return EventSourceResponse(counter())


async def clock():

    while True:

        current_time = datetime.datetime.now().strftime("%H:%M:%S")

        yield {
            "event": "clock",
            "data": current_time
        }

        await asyncio.sleep(1)


@app.get("/clock")
async def live_clock():

    return EventSourceResponse(clock())