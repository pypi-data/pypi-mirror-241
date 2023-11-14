# AziraClient

AziraClient is a comprehensive library designed for testing and interacting with message bus streams, handling user authentication, and managing WebSocket connections in a streamlined manner.

The goal here is to make it easier for people to get off the ground quickly with using ZeroMQ for sending message streams in realtime. 

The basis for this was built for an application that allows users to subscribe to stock tokens that interests them and receive that continuously in realtime.

## Features

  User authentication and registration.

- WebSocket connection management.
- Subscription to message bus streams.
- Testing utilities for ZeroMQ message bus.

## Installation

To install AziraClient, run the following command:

    ``pip install aziraclient``

## Quick Start

Here's a quick example to get you started:

```python
from aziraclient.auth.auth_client import AuthClient
from aziraclient.subscription.subscription import SubscribeToToken

# User authentication
"""
base_url: url where your server application is running.
"""
auth_client = AuthClient(base_url="http://localhost:8000")
auth_client.register_user("username", "password")
auth_client.login_user("username", "password")

# WebSocket subscription
"""
username: name of what you registered with
jwt_token: would be returned upon successful login.
action: "subscribe" or "unsubscribe"
token_name: name of token to subscribe to.

"""
tester = SubscribeToToken("username", "jwt_token", "action", "token_name")
tester.test_connection()

```

## Modules

### Authentication

Handles user registration and login, managing JWT tokens for secure access.

### Subscription

Manages WebSocket subscriptions, allowing users to subscribe or unsubscribe from specific tokens.

### Message Bus Tester

Provides tools for testing and interacting with ZeroMQ message bus streams.

## Usage

Refer to `example_usage.py` for detailed examples on how to use each module.

## Contributing

Contributions to aziraclient are welcome! Please read our contributing guidelines for details on how to submit pull requests, report issues, or request features.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
