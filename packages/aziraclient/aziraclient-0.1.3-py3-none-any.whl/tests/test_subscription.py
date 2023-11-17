import unittest
import asyncio
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aziraclient.subscription.subscription import SubscribeToToken

class TestSubscriber(unittest.TestCase):
    """
    Test cases for ZMQTestSubscriber class.
    """

    def test_subscribe(self):
        """
        Test the subscribe functionality of the ZMQTestSubscriber.
        """
        # Initialize the ZMQTestSubscriber with specific tokens
        username = "<Enter your username>"
        password = "<Enter your password>"
        jwt_token = "<Enter your generated jwt token>"
        action = "subscribe"
        token = "NSE:26009"
        tester = SubscribeToToken(username, jwt_token, action, token)
        # asyncio.get_event_loop().run_until_complete(tester.test_connection())


        #Checks if the subscriber is correctly set up
        self.assertTrue(tester.is_subscribed)

        # Note: Actual testing of ZMQ subscriptions might require a running ZMQ server
        # and could be more complex than a simple unit test.

if __name__ == '__main__':
    unittest.main()
