import zmq
import logging

class ZMQTestSubscriber:
    """
    A class to subscribe to a ZeroMQ message bus and log received messages.
    """

    def __init__(self, port="5556", tokens=None):
        """
        Initializes the ZMQTestSubscriber with specified port and tokens.
        :param port: Port number to connect to for the ZeroMQ message bus.
        :param tokens: List of tokens to subscribe to. If None or empty, subscribes to all messages.
        """
        self.port = port
        self.tokens = tokens
        self.logger = self.setup_logger()
        self.subscribed = False # indicates subscriber subscription status

    def setup_logger(self):
        """
        Sets up the logger for the class.
        Configures logging to output both to the console and to a file.
        """
        logger = logging.getLogger("MessageBusTester")
        logger.setLevel(logging.INFO)

        c_handler = logging.StreamHandler()
        f_handler = logging.FileHandler('message_bus_test.log')

        c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
        f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(c_format)
        f_handler.setFormatter(f_format)

        logger.addHandler(c_handler)
        logger.addHandler(f_handler)

        return logger

    def subscribe(self):
        """
        Subscribes to the ZeroMQ message bus and logs received messages.
        """
        context = zmq.Context()
        socket = context.socket(zmq.SUB)
        socket.connect(f"tcp://localhost:{self.port}")

        if self.tokens is None or not self.tokens:
            socket.setsockopt_string(zmq.SUBSCRIBE, "")
            self.logger.info("Subscribed to all messages.")
        else:
            for token in self.tokens:
                socket.setsockopt_string(zmq.SUBSCRIBE, token)
            self.logger.info(f"Subscribed to tokens: {self.tokens}")

        self.subscribed = True
        self.logger.info(f"Listening for messages on port {self.port}...")
        while True:
            try:
                message = socket.recv_string()
                token, data = message.split(' & ')
                if self.tokens is None or token in self.tokens:
                    self.logger.info(f"Received message for token {token}: {data}")
            except zmq.ZMQError as e:
                self.logger.error(f"ZMQ Error: {e}")
                self.subscribed = False
                break
        
    def is_subscribed(self):
        """
        Checks if the subscriber is currently subscribed
        """

        return self.subscribed
