# Imports
import socket

# These are all used to log into the bot, these are NOT TO BE CHANGED
server = "irc.chat.twitch.tv"
port = 6667
channel = "#lordarandor"

# The nickname can be changed, and I recommend it
nickname = "TwitchDOS"

# This must be done by the account using it, go to https://twitchapps.com/tmi/ to get the code needed
# You will need to log in and allow it access
token = "INSERT TOKEN HERE"
########^^^^^^^CHANGE BEFORE PUSHING^^^^^^^########

sock = socket.socket()

print("Logging in")

# Connect to the server, then send the correct things to actually join the chat
sock.connect((server, port))
sock.send(f"PASS {token}\n".encode("utf-8"))
sock.send(f"NICK {nickname}\n".encode("utf-8"))
sock.send(f"JOIN {channel}\n".encode("utf-8"))

print("Logged in")

# Main loop for the reading
while True:
	# Get the response from the server, most of the time this is blank
	resp = sock.recv(2048).decode("utf-8")
	
	# Handle PONG message
	if resp.startswith("PING"):
		sock.send("PONG\n".encode("utf-8"))
		continue
	# If the message actually contains something, then we do things
	if len(resp) > 2:
		print(resp) # Will be replaced with other things later, once we start working