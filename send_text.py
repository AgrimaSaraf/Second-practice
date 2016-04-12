from twilio import rest

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC98dba65930a6cf050c60ec2a1ef046be"
auth_token  = "99ee1df69cb2b1fab18abffa0b195b31"
client = rest.TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(
    body="This is a message from the other side!",
    to="+919629776244",    # Replace with your phone number
    from_="+12015968296") # Replace with your Twilio number
print message.sid
