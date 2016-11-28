awk '{for(i=1;i<=4;i++){split($i, chars, ""); printf("{0x%s%s, 0x%s%s},\n", chars[3], chars[4],chars[9], chars[10]);}}' < aes.txt > te1.txt
