import pickle

# Open the token.pickle file
with open("token.pickle", "rb") as token_file:
    credentials = pickle.load(token_file)

# Print the information inside the file
print("Access Token:", credentials.token)
print("Refresh Token:", credentials.refresh_token)
print("Token Expiry:", credentials.expiry)
print("Client ID:", credentials.client_id)
print("Client Secret:", credentials.client_secret)
