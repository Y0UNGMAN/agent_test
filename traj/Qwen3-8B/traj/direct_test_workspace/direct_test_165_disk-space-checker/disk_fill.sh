#!/bin/bash
while true; do
    dd if=/dev/urandom of=/root/random_data bs=1M
    if [ $? -eq 0 ]; then
        echo "Wrote 1M of random data."
    else
        echo "Error writing data. Disk may be full."
        break
    fi
done