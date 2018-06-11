tail -n +2 "$1" | cut -d / -f 1 | sed 's/^"*[A-Z0-9]\{14\}//' | sort | uniq -c | sort -r | head -n 10
