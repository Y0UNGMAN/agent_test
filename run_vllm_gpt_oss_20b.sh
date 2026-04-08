#!/bin/bash

# 本脚本用于本地使用 vLLM 启动 gpt-oss-20b 模型
# 直接在文件内写好配置，修改下面变量即可

set -e

# 模型目录：请改成你的本地模型路径
MODEL_DIR="/root/autodl-tmp/models/gpt-oss-20b"

# vLLM 服务绑定地址和端口
HOST="0.0.0.0"
PORT="8000"

# 服务端对外注册的模型名称，可用于 OpenAI 兼容调用
SERVED_MODEL_NAME="gpt-oss-20b"

if [ ! -d "$MODEL_DIR" ]; then
  echo "错误：模型目录不存在： $MODEL_DIR"
  echo "请先运行 download_gpt_oss_20b.py 下载模型，或将 MODEL_DIR 修改为正确目录。"
  exit 1
fi

cat <<EOF
==========================================================
正在使用 vLLM 启动模型: $MODEL_DIR
API 地址将映射到: http://$HOST:$PORT/v1
模型名称 (用于客户端调用): $SERVED_MODEL_NAME
==========================================================
EOF

python -m vllm.entrypoints.openai.api_server \
  --model "$MODEL_DIR" \
  --served-model-name "$SERVED_MODEL_NAME" \
  --dtype auto \
  --host "$HOST" \
  --port "$PORT" \
  --max-model-len 32768 \
  --gpu-memory-utilization 0.85 \
  --enable-prefix-caching 
