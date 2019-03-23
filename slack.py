from slackclient import SlackClient
import os
slack_token = ["xoxp-450789184706-450695730467-585918023602-681341909cda95ac41638837d5098e30"]
sc = SlackClient(slack_token)

sc.api_call(
  "chat.postEphemeral",
  channel="#general",
  text= "Test Message",
)