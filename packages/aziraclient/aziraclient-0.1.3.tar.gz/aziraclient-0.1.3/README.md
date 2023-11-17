# AziraClient

AziraClient is a compreshensive libraru built on top of [Azira](https://github.com/manny-uncharted/Azira) a service grants users the ability to subscribe and receive crypto tokens data in near real-time. A possible use case for this is when you need to build bots that sends you real-time updates or applications that continuously needs real-time updates about a particular crypto token.

## Features

* registration
* login
* subscribe to receive data about your tokens in real-time

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

#### Notes

Here are things I need to do to improve this. At the moment this package only works with this project. [Azira](https://github.com/manny-uncharted/Azira)

* If you're interested in testing things out you can check the main project and run it alongside
* Make sure the library works with every stock token on the stock market.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
