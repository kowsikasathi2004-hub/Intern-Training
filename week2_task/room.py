from fastapi import FastAPI

app = FastAPI()

room_bookings = []

@app.post("/room_booking")
def add_room_booking(name: str):
    room_bookings.append(name)
    return {"message": "Room booked successfully"}


@app.get("/room_booking")
def get_bookings():
    return room_bookings

@app.delete("/room_booking")
def delete_room_booking(name: str):
    if name in room_bookings:
        room_bookings.remove(name)
        return {"message": "Room booking successfully deleted"}
    return {"message": "Room booking not found"}

@app.put("/room_booking")
def update_room_booking(old_name: str, new_name: str):
    if old_name in room_bookings:
        index = room_bookings.index(old_name)
        room_bookings[index] = new_name
        return {"message": "Room booking updated successfully"}
    return {"message": "Room booking not found"}        
    