import asyncio
import websockets
import json
import logging
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AuthenticatedWebsocketConnector:
    def __init__(self, uri, jwt_token, ping_interval=10):
        self.uri = uri
        self.jwt_token = jwt_token
        self.ping_interval = ping_interval
        self.websocket = None

    async def connect(self):
        try:
            self.websocket = await websockets.connect(self.uri, extra_headers={"Authorization": f"Bearer {self.jwt_token}"})
            asyncio.create_task(self.ping_pong())
        except Exception as e:
            logger.error(f"Error during connection: {e}")
            raise

    async def send_message(self, action, tokens):
        if self.websocket:
            try:
                message = f"{action}|{','.join(tokens)}"
                await self.websocket.send(message)
            except Exception as e:
                logger.error(f"Error sending message: {e}")
                raise

    async def receive_message(self):
        if self.websocket:
            try:
                return await self.websocket.recv()
            except Exception as e:
                logger.error(f"Error receiving message: {e}")
                raise

    async def ping_pong(self):
        while self.websocket:
            try:
                await self.websocket.ping()
                await asyncio.sleep(self.ping_interval)
            except websockets.exceptions.ConnectionClosed as e:
                logger.error(f"Connection closed: {e}")
                break
            except Exception as e:
                logger.error(f"Error in ping_pong: {e}")
                break

    async def close(self):
        if self.websocket:
            try:
                await self.websocket.close()
            except Exception as e:
                logger.error(f"Error closing websocket: {e}")
                raise