import Enrtries
import numpy as np
import pylab as plt

m = []
n = []
i = 1
o = []

f = open("entries.txt","r")
while i <= 500:
    r = f.readline().rstrip()
    k,l = r.split(",")
    m.append(int(k))
    n.append(int(l))
    #print k
    #print l
    i+= 1
f.close()

m = (np.array(m))
n = np.array(n)

BMI = (n/((m*m)/10000))


#print (BMI)
z = open("overweight.txt", "w+")
un = open("underweight.txt", "w+")
no = open("normalweight.txt", "w+")
o = []
u = []
n = []
for each in (BMI):
    if each > 35:
        #print list(BMI).index(each)
        o.append(each)
        z.write(str(each)+ ",")
    elif each < 25:
        u.append(each)
        un.write(str(each) + ",")
    elif each >= 25 and each <= 35:
        n.append(each)
        no.write(str(each) + ",")
print o

plt.plot(o, 'rs', u, 'g^', n, 'o')
plt.title("BMI graph for 500 players")
plt.xlabel("red-overweight, green-underweight, blue-Normal")
plt.ylabel("BMI")
'''for dd in range(0,501):
    plt.text(x,y, 'BMI')'''
plt.show()
plt.ioff()

z.close()
 
