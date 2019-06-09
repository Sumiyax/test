import matplotlib.pyplot as plt
#当前物品价值和
v = 0
#当前物品重量和
w = 0
#背包重量
b = input("请输入背包重量：")
b = int(b)
c = []
k = input("请输入物品重量，且每件物品重量用空格分隔")
k = k.split(",")
k = [int(k[i]) for i in range(len(k))]
j = input("请输入物品价值，且每件物品重量用空格分隔")
j= j.split(",")
j = [int(j[i]) for i in range(len(j))]

len1 = len(k)
for i in range(len1):
    for l in range(i,len1):
        if w+k[l]<=b:
            v = v+j[l]
            w = w+k[l]
        else :
            continue
    c.append(v)
    v = 0
    w = 0
maxV = max(c)
print(maxV)
print(c)
h = []
for u in range(len(c)):
    h.append(u)
a = []
x = []
for f in range(len(c)):
    for z in range(f+1):
        a.append(h[z])
        x.append(c[z])
    plt.bar(x = a,height= x)
    plt.show()
plt.bar(x=h, height=c)
plt.show()