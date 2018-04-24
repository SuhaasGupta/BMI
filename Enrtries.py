import random

f = open("entries.txt", "w+")
a = range(160,191)
b = range(70,100)
for each in range(0,500):
    h= random.choice(a)
    w= random.choice(b)
    f.write(str(h)+ ",")
    f.write(str(w)+ "\n")
    
    
f.close()
