import numpy as np
import matplotlib.pyplot as plt
x1=[1,2,3,4,5]
y1=[10,20,15,25,30]
font={'color':'green','size':'20'}
plt.title("line chart",fontdict=font,loc='left')
plt.xlabel("number1")
plt.ylabel("number2")
plt.plot(x1,y1)
plt.grid(axis='x',color='red',linestyle='--',linewidth='0.5')
x=np.array([70,40,90,50])
y=np.array([30,90,10,60])
x1=np.array([20,10,50,90])
y1=np.array([60,90,20,77])
i=np.array([20,10,50,70])
j=np.array([89,75,25,62])
k=np.array([63,65,42,78])
l=np.array([24,26,32,51])
plt.subplot(2,2,1)
plt.title("p1")
plt.plot(x,y)
plt.subplot(2,2,2)
plt.title("p2")
plt.plot(x1,y1)
plt.subplot(2,2,3)
plt.title("p3")
plt.plot(i,j)
plt.subplot(2,2,4)
plt.title("p4")
plt.plot(k,l)
plt.suptitle("Superfile")
size=np.array([30,80])
plt.scatter(x1,y1,color='blue')
plt.scatter(x,y,color='purple')
plt.bar(x1,y1)
plt.barh(x,y)
plt.hist(x1)
plt.pie(x1)
track_stu=np.array([20,30,40,20,10])
track_name=["Data","Mobile","Web","Iot","CS"]
ex=[0.2,0,0,0,0]
col=["Red","Pink",'m','g','b']
plt.pie(track_stu, labels=track_name, startangle=90, explode=ex, shadow=True, 
colors=col)
plt.legend(title="Tracks")
plt.show()