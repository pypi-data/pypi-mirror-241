import requests

class AuthClient:
    def __init__(self, base_url="http://localhost:8000"):
        self.base_url = base_url
        self.token_file = "auth_token.txt"

    def register_user(self, username, password):
        """Function to register a new user."""
        try:
            response = requests.post(f"{self.base_url}/api/v1/users/register", json={"username": username, "password": password})
            if response.status_code == 200:
                return "Registration successful."
            else:
                return f"Registration failed: {response.json().get('detail', 'Unknown error')}"
        except requests.ConnectionError:
            return "Error: Unable to connect to the server."
        except requests.Timeout:
            return "Error: Server timed out."
        except requests.RequestException as e:
            return f"Error: {e}"

    def login_user(self, username, password):
        """Function to log in an existing user."""
        try:
            response = requests.post(f"{self.base_url}/api/v1/users/login", json={"username": username, "password": password})
            if response.status_code == 200:
                response_data = response.json()
                token = response_data.get("access_token")
                token = token['access_token']
                self.write_token_to_file(str(token))
                return {
                    "message": "Login successful.",
                    "username": username,
                    "access_token": token,
                    "token_type": response_data.get("token_type")
                }
            else:
                return f"Login failed: {response.json().get('detail', 'Unknown error')}"
        except requests.ConnectionError:
            return "Error: Unable to connect to the server."
        except requests.Timeout:
            return "Error: Server timed out."
        except requests.RequestException as e:
            return f"Error: {e}"

    def write_token_to_file(self, token):
        """Write the JWT token to a file."""
        try:
            with open(self.token_file, 'w') as file:
                file.write(token)
            return f"Token written to {self.token_file}"
        except IOError as e:
            return f"Error writing token to file: {e}"
