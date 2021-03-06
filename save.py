import pandas as pd
import matplotlib.pyplot as plt
from extention import ExtentionOps
from memfuncs import MemFunc
import numpy as np

df = pd.read_csv("tfmem.csv")

#print(df.head())


# p = ["City MPG - Poor", "Highway MPG - Good", "Horsepower - Average",
#      "Risk - Low", "Value Loss - Low", "Price - Cheap"]

p = ["HighwayMPG-Good","Horsepower-Average","CityMPG-Poor","Price-cheap","Risk-Low","ValueLoss-Low","HighwayMPG-Good","Horsepower-Average","CityMPG-Poor","Price-cheap","Risk-Low","ValueLoss-Low"]


c = ['b','g','k','r','c','m']

e = ExtentionOps("add")
#e.convertToDomain()

X = np.arange(0,1.1, .05)

rows = [[0, 0, 0.2],[0.35, 0.55, 0.75],[0.4, 0.6, 0.8],[0.0557, 0.25567, 0.4557],[0, 0, 0.2],[0.7, 0.9, 1],[0, 0, 0.2],[0.35, 0.55, 0.75],[0.4, 0.6, 0.8]]


count = 0
for row in rows:
    A = e.convertToDomain([row[0],row[1],row[1],row[2]])
    #plt.plot(A[:,0],A[:,1],c='b',linewidth=2)

    m1 = MemFunc("trap",[row[0],row[1],row[1],row[2]])
    plt.plot(X,[m1.memFunc(i) for i in X ],c=c[count],linewidth=2)

    plt.xlim([0,1])
    plt.ylim([0,1])

    plt.title(p[count])
    plt.savefig("img/start-" + str(count) + ".png")
    plt.clf()

    # plt.show()
    # t = input()
    if count > 4:
        break
    count += 1







#
# plt.plot(B[:,0],B[:,1],c='b')
# plt.xlim([0,2])
# plt.ylim([0,1])
#



# A = []
# B = []

# for i in np.arange(0,1,.05):

#     A.append([i,e.round2(mem1.memFunc(i))])

#     B.append([i,e.round2(mem2.memFunc(i))])

# A = np.array(A)
# B = np.array(B)



# #A = [.2,.4,.4,.6]
# # B = [.4,.6,.6,.8]

# print("########")
# #p = e.comp(A)
# t = e.extention([A,B])
# #print(e.extention([p,t]))
