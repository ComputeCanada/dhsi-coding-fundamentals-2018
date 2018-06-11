tail -n +2 "$1" | cut -d / -f 1 | sed 's/"*EPLABB[0-9]\{8\}//' | sort | uniq -c | sort -r | head -n 10
