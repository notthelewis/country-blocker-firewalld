#!/usr/bin/bash
file="$1"
while IFS= read -r line
 do
   firewall-cmd --permanent --add-rich-rule="rule family='"$2"' source address='"$line"' reject"
done<$file

