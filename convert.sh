#!/bin/bash

# One dir to keep papers that I have already processed
# and another dir to store newly added papers
existing_file="./pdf/"
output_dir="./txt/"

counter=0

total=$(find ./pdf -type f -name "*.pdf" | wc -l)

find ./pdf -type f -name "*.pdf" | while read -r file
do
    base_name=$(basename "$file" .pdf)

    pdftotext -enc UTF-8 "$file" "$output_dir/$base_name.txt"
	
    counter=$((counter + 1))
    echo -ne "Processed $counter out of $total PDFs.\r"
    
done
