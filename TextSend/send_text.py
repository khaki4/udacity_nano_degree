from twilio.rest import TwilioRestClient

account_sid = "AC7611df1c6faa0c3f332fb7fe4caef67c" # Your Account SID from www.twilio.com/console
auth_token  = "d22b47f411c8186667d588bf91275d5d"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(
    body="My name is Jiwon Jeung",
    to="+8201096156863",    # Replace with your phone number
    from_="+19722013954") # Replace with your Twilio number

print(message.sid)