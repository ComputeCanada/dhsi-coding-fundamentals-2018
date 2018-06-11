#!/bin/bash

while read -r LINE; do
    grep "Web URL" MostPopularByBranch.csv > "$LINE".csv
    grep "$LINE" MostPopularByBranch.csv >> "$LINE".csv
done < branchCodes.txt
