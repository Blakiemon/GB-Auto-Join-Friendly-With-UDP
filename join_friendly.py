import enet, asyncio

async def join_friendly(user_id, auth_token, friendly_match_id):
    host = enet.Host(peerCount = 1)
    peer = host.connect(address=enet.Address(b"35-225-183-118.noodlecakegames.net", 42775), channelCount=1)

    msg = bytearray()
    msg += bytes.fromhex('030A18')
    msg += bytearray(user_id.encode())
    msg += bytes.fromhex('1224')
    msg += bytearray(auth_token.encode())
    msg += bytes.fromhex('1A747B22667269656E646C795F6D617463685F6964223A2022')
    msg += bytearray(friendly_match_id.encode())
    msg += bytes.fromhex('222C202269735F667269656E646C795F6D61746368223A20747275657D2001')

    packet = enet.Packet(data=msg, flags=enet.PACKET_FLAG_RELIABLE)
    #Wait for connection to the server with the .service() method then send connect to friendly match packet
    host.service(1000)
    peer.send(0, packet)

    while True:
        event = host.service(1000)
        if event.type == enet.EVENT_TYPE_DISCONNECT:
            #Stop when disconnected
            return
        await asyncio.sleep(.5)