### Project Dependencies
- Pynacl: Signing and validating transactions
- Structlog: Logging Library (better than print() statements)
- Colorama: Allows colorful output (in logging)
- Marshmallo: Validates data structures, such as node sent/recieved JSON messages
- marshmallow-oneofschema: Allows marshmallow to validate more complex data structs
- Aiohttp: An asynchronous HTTP client(used to ind our public IP addy)

### Project Directory Structure
funcoin
├── funcoin
│     ├── __init__.py
│     ├── blockchain.py
│     ├── connections.py
│     ├── messages.py
│     ├── peers.py
│     ├── server.py
│     ├── transactions.py
│     ├── types.py
│     └── utils.py
├── __init__.py
├── node.py
├── poetry.lock
└── pyproject.toml

### Code Structure
- Module descriptions
    * blockchain.py: Module used to house the Blockchain class
    * peers.py: Logic to handle the propagation of messages that peers may send us: how we communicate. We'll call this the P2PProtocol.
    * connections.py: Lgic to handle the pool of active connections communicating with the node.
    * server.py:  basic TCP server.
