from typing import Annotated

from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends

from .manager import ConnectionManager

router = APIRouter(prefix='/ws', tags=['Websocket'])


@router.websocket("/{client_id}")
async def websocket_endpoint(
    websocket: WebSocket,
    client_id: int,
    manager: Annotated[ConnectionManager, Depends()],
):
    await manager.connect(websocket)
    await manager.broadcast_json({"message": f"Client #{client_id} join the chat"})
    try:
        while True:
            # Example for handle JSON message:
            json_data: dict | list = await manager.receive_json(websocket)
            await manager.send_personal_json(websocket, json_data)

            # Example for handle text message:
            # data = await manager.receive_text(websocket)
            # await manager.broadcast_json({"message": f"Client #{client_id} says: {data}"})
    except WebSocketDisconnect:
        await manager.disconnect(websocket)
        await manager.broadcast_json({"message": f"Client #{client_id} left the chat"})


# For testing in Swagger
@router.post('/send_json')
async def send_mailing(
    payload: dict,
    manager: Annotated[ConnectionManager, Depends()],
):
    await manager.broadcast_json(payload)
