import golfblitz_client, join_friendly, asyncio

client = golfblitz_client.Client(username='kek', password='kek')

@client.on_websocket_recieve(class_match=".ScriptMessage")
async def invited_to_match(message):
    
    if message['extCode'] == "PLAYER_INVITED_TO_FRIEND_MATCH":
        print("Joining friendly match lobby.")
        await client.join_friendly_match(match_id=message['data']['match_id'])

    elif message['extCode'] == "FRIENDLY_MATCH_START_MATCHMAKING":
        print("Joining friendly match UDP.")
        asyncio.create_task(join_friendly.join_friendly(user_id=client.user_id, auth_token=client.auth_token, friendly_match_id=message['data']['match_id']))

@client.on_ready
def ready():
    print(f"Logged in as {client.display_name}")

client.run()