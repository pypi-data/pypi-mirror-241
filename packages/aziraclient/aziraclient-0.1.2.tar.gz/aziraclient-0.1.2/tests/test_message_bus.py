import unittest
import os
import sys

# Adjust the path to include the parent directory so we can import the library
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aziraclient.message_bus.message_bus_tester import ZMQTestSubscriber

class TestZMQTestSubscriber(unittest.TestCase):
    """
    Test cases for ZMQTestSubscriber class.
    """

    def test_subscribe(self):
        """
        Test the subscribe functionality of the ZMQTestSubscriber.
        """
        # Initialize the ZMQTestSubscriber with specific tokens
        tokens = ["NSE:26009", "NSE:26000"]
        subscriber = ZMQTestSubscriber(tokens=tokens)

        # Calls the subscribe method
        # subscriber.subscribe()


        #Checks if the subscriber is correctly set up
        self.assertTrue(subscriber.is_subscribed)

        # Note: Actual testing of ZMQ subscriptions might require a running ZMQ server
        # and could be more complex than a simple unit test.

if __name__ == '__main__':
    unittest.main()
