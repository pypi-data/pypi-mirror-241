### Installation

    pip install websocket-training

### Usage
    
    import uvicorn
    from fastapi import FastAPI
    
    from websocket_training.ws_router import connect_ws, get_ws_manager, ConnectionManager
    
    app = FastAPI()
    connect_ws(app)
    
    manager: ConnectionManager = get_ws_manager()
    print(manager.count())
    
    
    if __name__ == '__main__':
        uvicorn.run('main:app')
