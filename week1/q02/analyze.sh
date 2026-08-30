#!/usr/bin/env bash

# 检查参数
if [ $# -ne 1 ]; then
    echo "Usage: $0 <csv_file_path>" >&2
    exit 1
fi

FILE="$1"

# 文件不存在时输出错误到stderr，返回非零退出码
if [ ! -f "$FILE" ]; then
    echo "Error: file '$FILE' not found." >&2
    exit 2
fi

echo "=== Top 2 paths with most 5xx requests ==="
# 过滤5xx状态，按path统计次数，降序排列，次数相同按path字典序
awk -F',' 'NR>1 && $4 ~ /^5[0-9]{2}$/ {cnt[$3]++}
END {
    for (p in cnt) print cnt[p], p
}' "$FILE" | sort -k1,1nr -k2,2 | head -n 2

echo ""
echo "=== Average latency (ms) ==="
# 跳过表头，计算平均延迟，保留两位小数
awk -F',' 'NR>1 {sum += $5; n++}
END {
    if (n > 0) printf "%.2f\n", sum / n}' "$FILE"

