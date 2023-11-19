# SANDI_CONNECT

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/your-library.svg)](https://badge.fury.io/py/your-library)

## Description

`SANDI_CONNECT` is a Python library designed to facilitate connections to MQTT brokers using WebSockets and to enable easy message sending. This library is particularly tailored for SANDI projects, streamlining the process of configuring PMUs (Phasor Measurement Units) to send protocol frames over UDP.

## Installation

Install `SANDI_CONNECT` via pip:

```bash 
pip install sandi_connect
```
## Configuration

To securely manage your credentials, SANDI_CONNECT uses environment variables. Set up a .env file in your project's root directory with the following variables:

```makefile
CLIENT_ID=your_client_id
USER=your_username
PASSWORD=your_password
```
Remember to add .env to your .gitignore file to keep your credentials secure.

## Usage

Below is a basic example of how to use SANDI_CONNECT to establish a connection to a SANDI project and send messages:

```python
from dotenv import load_dotenv
from sandi_connect import get_client, start_conection_sandi
# Load environment variables from the .env file
load_dotenv()

# Retrieve credentials from environment variables
client_id = os.getenv("CLIENT_ID")
user = os.getenv("USER")
password = os.getenv("PASSWORD")
topic = os.getenv("TOPIC")

# Load your credentials from the environment
client = get_client(client_id, user, password)

# Start a connection to the specified topic and port
start_conection_sandi(client, topic, <your_port>)

```
