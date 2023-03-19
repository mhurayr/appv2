# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import requests

# View our quick start guide to get your API key:
# https://www.voiceflow.com/api/dialog-manager#section/Quick-Start
api_key = "{VF.DM.6415b59b17fda40007fe3a3a.evdv62LKAdRla1d4}"

user_id = "user_123"  # Unique ID used to track conversation state
user_input = "Hello world!"  # User's message to your Voiceflow assistant

body = {"action": {"type": "text", "payload": "Hello world!"}}

# Start a conversation
response = requests.post(
    f"https://general-runtime.voiceflow.com/state/user/{user_id}/interact",
    json=body,
    headers={"Authorization": api_key},
)

# Log the response
print(response.json())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
