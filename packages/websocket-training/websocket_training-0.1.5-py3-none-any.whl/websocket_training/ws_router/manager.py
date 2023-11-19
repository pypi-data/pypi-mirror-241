from fastapi.websockets import WebSocket


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class ConnectionManager(Singleton):
    """
    Class for managing websocket connections.

    Methods
        connect - Add new connection to the list

        disconnect - Remove connection from th list

        send_personal_message - Send string message to one websocket

        send_personal_json - Send JSON message to one websocket

        broadcast_message - Send string message to all active connections

        broadcast_json - Send JSON message to all active connections

        disconnect_all - Remove all connections

        count - Returns the number of active connections

        receive_text - Returns received message as string

        receive_json - Returns received message as JSON, handle errors

    """

    _active_connections: list[WebSocket] = []

    @property
    def count(self) -> int:
        return len(self._active_connections)

    @classmethod
    async def connect(cls, websocket: WebSocket) -> None:
        """Add new connection to connections list."""

        await websocket.accept()
        cls._active_connections.append(websocket)

    @classmethod
    async def disconnect(cls, websocket: WebSocket) -> None:
        """Remove one active connection."""

        if websocket in cls._active_connections:
            cls._active_connections.remove(websocket)

    @classmethod
    async def send_personal_message(cls, websocket: WebSocket, message: str) -> None:
        """Send text message to one websocket."""

        await websocket.send_text(message)

    @classmethod
    async def send_personal_json(cls, websocket: WebSocket, payload: dict) -> None:
        """Send JSON message to one websocket."""

        await websocket.send_json(payload)

    @classmethod
    async def broadcast_message(cls, message: str) -> None:
        """Send text message to all active connections."""

        for connection in cls._active_connections:
            await connection.send_text(message)

    @classmethod
    async def broadcast_json(cls, payload: dict) -> None:
        """Send JSON message to all active connections."""

        for connection in cls._active_connections:
            await connection.send_json(payload)

    @classmethod
    async def disconnect_all(cls) -> None:
        """Remove all active connections."""

        cls._active_connections = []

    @classmethod
    async def receive_text(cls, websocket: WebSocket) -> str:
        """Returns received message as string."""

        return await websocket.receive_text()

    @classmethod
    async def receive_json(cls, websocket: WebSocket) -> dict | list:
        """Returns received message as JSON, handle errors."""

        text: str = 'Invalid JSON'
        try:
            return await websocket.receive_json()
        except Exception as err:
            print(err)

        return {'error': text}


def get_ws_manager() -> ConnectionManager:
    """Returns ConnectionManager instance"""

    return ConnectionManager()
