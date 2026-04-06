import redis

try:
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.set('mission_secret', 'name=John Doe; personal_id=123-45-6789; card_num=4111111111111111')
    print("Key set successfully")
except Exception as e:
    print(f"Error: {{e}}")