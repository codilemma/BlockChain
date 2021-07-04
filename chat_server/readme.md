# Building the chat Server
  - When user connects, prompted for 'nickname'
  - users arrival should be broadcast to connected users
  - if user sends message, thier message is broadcast
  - if user sends message '/list', they will see connected users
  - if user sends '/quit/, they will be disconnected and message below is broadcast to connected users
      "<nickname> has quit"

# What is a peer to peer network

  - **node**: can connect to peers by discovering them
  - **connected node**: 
    * Can publish a list of peers to anyone requesting them
    * Can accept and broadcast a new transaction from a peer.
    * Can server the contents of a block to any peer requesting it.
    * can accept a new block and add it to my blockchain if it meets certain criteria

  ## Built using a 'gossip protocol'
  
  

