import csv
from random import SystemRandom

with open("4000-most-common-english-words-csv.csv", 'r') as f:
    reader = csv.reader(f)
    words = list(reader)
    rand = SystemRandom()
    pwd = []
    for x in range(4):
    	pwd.append(rand.choice(words)[0])
    print("-".join(pwd))
