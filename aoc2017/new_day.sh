mkdir $1dec && cd $1dec
touch $1.py && touch $1.in && touch $1.sample
echo "from collections import defaultdict" >> $1.py
echo "" >> $1.py
echo "for line in open('$1.sample', 'r+').readlines():" >> $1.py
echo "	line = line.strip()" >> $1.py
code .