#!/bin/bash
cd "$(dirname "$0")"
echo "🚀 Nvidia Ecosystem - 英伟达生态链金融分析"
echo "========================"
echo "访问: http://127.0.0.1:3001/"
echo "按 Ctrl+C 停止"
echo ""
source ~/.hermes/hermes-agent/venv/bin/activate 2>/dev/null
python3 -m http.server 3001 --bind 127.0.0.1
