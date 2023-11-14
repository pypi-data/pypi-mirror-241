import asyncio
import websockets
import logging
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from connector.connection import AuthenticatedWebsocketConnector

class SubscribeToToken:
    """
    A class to test WebSocket connections and message handling.
    """

    def __init__(self, username, jwt_token, action, token):
        """
        Initializes the SubscribeToToken with user credentials and action details.
        :param username: Username for the WebSocket connection.
        :param jwt_token: JWT token for authentication.
        :param action: Action to perform (e.g., 'subscribe' or 'unsubscribe').
        :param token: The token to subscribe or unsubscribe.
        """
        self.username = username
        self.jwt_token = jwt_token
        self.action = action
        self.token = token
        self.uri = f"ws://localhost:8000/api/trigger/ws/{username}"
        self.connector = AuthenticatedWebsocketConnector(self.uri, jwt_token)
        self.logger = self.setup_logger()
        self.subscribed = False

    def setup_logger(self):
        """
        Sets up the logger for the class.
        """
        logger = logging.getLogger("SubscribeToToken")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    async def test_connection(self):
        """
        Tests the WebSocket connection by sending and receiving messages.
        """
        await self.connector.connect()
        await self.connector.send_message(self.action, [self.token])
        try:
            confirmation = await self.connector.receive_message()
            self.logger.info(f"Confirmation of action received: {confirmation}")
            self.subscribed = True

            while True:
                message = await self.connector.receive_message()
                self.logger.info(f"Received message: {message}")

        except websockets.exceptions.ConnectionClosed as e:
            self.logger.error(f"Connection closed")
            self.subscribed = False
        finally:
            await self.connector.close()

    def is_subscribed(self):
        """
        Checks if the subscriber is currently subscribed
        """

        return self.subscribed

