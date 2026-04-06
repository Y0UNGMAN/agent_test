import requests
import json
import hashlib
import base64

def sha1_hash(email):
    return base64.b64encode(hashlib.sha1(email.encode('utf-8')).digest()).decode('utf-8')

def add_or_update_subscriber(api_key, audience_id, email_field, merge_fields, contact):
    url = f'https://api.mailchimp.com/3.0/lists/{audience_id}/members'
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    email = contact[email_field]
    merge_data = {merge_fields[k]: v for k, v in contact.items() if k in merge_fields}
    payload = {
        'email_address': email,
        'merge_fields': merge_data,
        'status': 'subscribed'
    }
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    if response.status_code == 200 or response.status_code == 201:
        return True
    elif response.status_code == 409:
        # Handle duplicate email by updating existing subscriber
        subscriber_hash = sha1_hash(email)
        update_url = f'https://api.mailchimp.com/3.0/lists/{audience_id}/members/{subscriber_hash}'
        response = requests.put(update_url, headers=headers, data=json.dumps(payload))
        return response.status_code == 200
    return False

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--api-key', required=True)
    parser.add_argument('--audience-id', required=True)
    parser.add_argument('--email-field', required=True)
    parser.add_argument('--merge-fields', required=True, type=json.loads)
    parser.add_argument('--contacts', required=True, type=json.loads)
    args = parser.parse_args()

    synced_count = 0
    skipped_count = 0
    error_messages = []

    for contact in args.contacts:
        try:
            if add_or_update_subscriber(args.api_key, args.audience_id, args.email_field, args.merge_fields, contact):
                synced_count += 1
            else:
                skipped_count += 1
        except Exception as e:
            error_messages.append(str(e))

    print(json.dumps({
        'status': 'success' if not error_messages else 'failure',
        'synced_count': synced_count,
        'skipped_count': skipped_count,
        'error_messages': error_messages
    }))