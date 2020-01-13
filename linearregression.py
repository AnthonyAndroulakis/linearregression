import random
import matplotlib.pyplot as plt #for plotting
import numpy as np #for plotting

learningrate = 20
epochs = 1000000
csv_file = 'auto_insurance_sweden.csv'

x=[]
with open(csv_file, 'r') as f:
    for row in f:
        x.append(row.split(',')[0])
x = [float(i) for i in x]

y=[]
with open(csv_file, 'r') as f:
    for row in f:
        y.append(row.split(',')[1])
y = [float(i) for i in y]

if min(x) == 0:
    slope = random.randrange(int(min(y)/learningrate),int(max(y)/max(x)))
elif max(x) == 0:
    slope = random.randrange(int(min(y)/min(x)),int(max(y)/learningrate))
else:
    slope = random.randrange(int(min(y)/min(x)),int(max(y)/max(x))) #pick a decent slope range
yint = random.randrange(int(min(y)),int(max(y))) #pick a decent y intercept range

for i in range(epochs):
    #index = random.randrange(0,len(x)) #pick random index
    for index in range(len(x)):
        linevalue = slope*x[index]+yint
        xpt = x[index]
        ypt = y[index]
        if ypt > linevalue and xpt > 0:
            slope = slope+learningrate
            yint = yint+learningrate
        elif ypt > linevalue and xpt < 0:
            slope = slope-learningrate
            yint = yint+learningrate
        elif ypt < linevalue and xpt > 0:
            slope = slope-learningrate
            yint = yint-learningrate
        elif ypt < linevalue and xpt < 0:
            lope = slope+learningrate
            yint = yint-learningrate

print('Fitted Line: ')
print('y = '+str(slope)+'*x + '+str(yint))
xline = np.linspace(len(x),int(min(x)),int(max(x)))
yline = slope*xline+yint
plt.scatter(x, y) #plot the original points
plt.plot(xline,yline,'-r', label='y='+str(slope)+'*x+'+str(yint))
plt.show()
