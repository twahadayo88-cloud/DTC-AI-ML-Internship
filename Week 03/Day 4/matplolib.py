""""import matplotlib.pyplot as plt
import numpy as np 

xpoint = np.array([0,6])
ypoint = np.array([0,250])
plt.plot(xpoint, ypoint)
plt.show()"""

#----------------------------------------------
"""""import matplotlib.pyplot as plt
import numpy as np 
xpoint=np.array([3,4])
ypoint=np.array([3,10])
plt.plot(xpoint, ypoint)
plt.show()"""""
#-----------------------------------------------

""""#Draw two ponts in diagram (plotting without line )
import matplotlib.pyplot as plt
import numpy as np 
xpoint=np.array([3,4])
ypoint=np.array([3,10])
plt.plot(xpoint, ypoint, 'o')
plt.show()"""

#--------------------------------------------

#Multiple points draw:
"""import matplotlib.pyplot as plt
import numpy as np 
xpoints = np.array([1,2,4,5,8])
ypoints = np.array([3,4,7,9,0])
plt.plot(xpoints,ypoints)
plt.show()"""""

#example 2
""""import matplotlib.pyplot as plt
import numpy as np 
ypoints = np.array([8, 4, 9, 3, 4])
xpoints = np.array([3,4,7,9,0])
plt.plot(xpoints,ypoints)
plt.show()"""""

#-------------------------------

# default X-points

""""import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3,8,1,10,5,7])
plt.plot(ypoints)
plt.show()"""
#---------------------------------

#Matplotlib Markers
"""import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([6, 9, 1, 8])

#plt.plot(ypoints, marker = 'o')
plt.plot(ypoints, marker = '*')

plt.show()"""

#-----------------------------------
# format string fmt
""""import matplotlib.pyplot as plt
import numpy as np 
ypoints = np.array([1,5,8,9])
plt.plot(ypoints, 'o:r')
plt.show()"""

#-------------------------------
# Marker Size
""""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,9,5,12])
plt.plot(ypoints, marker= 'o', ms = 20)
plt.show()"""

#---------------------------------------
# marker color
""""import matplotlib.pyplot as plt
import numpy as np
ypoints=np.array([3,9,5,12])
plt.plot(ypoints, marker= 'o', ms = 20, mec = 'r')
plt.show()"""

#------------------------------------
#Matplotlib Line

""""import matplotlib.pyplot as plt
import numpy as np 
ypoints = np.array([2,6,2,10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()"""
#-------------------------------------------
# for dashed
"""import matplotlib.pyplot as plt
import numpy as np 
ypoints = np.array([2,6,2,10])
plt.plot(ypoints, linestyle = 'dashed') #linestyle : ls, dotted :, dashed: --

plt.show()"""
#--------------------------------------
# Line width
"""import matplotlib.pyplot as plt
import numpy as np 
ypoint =np.array([3,9,5,2,7])
plt.plot(ypoint, linewidth='12.5')
plt.show()"""

#------------------------------
# Multiple Lines
"""import matplotlib.pyplot as plt
import numpy as np
x1 = np.array([2,5,7,9,6])
x2 = np.array([9,6,3,5,8])
plt.plot(x1)
plt.plot(x2)
plt.show()"""

#----------------- 
# Matplotlib labels and titles
""""import matplotlib.pyplot as plt
import numpy as np 

x= np.array([60, 65, 25, 70, 40, 45, 50])
y= np.array([200, 210, 220, 230, 235, 240, 300])

plt.plot(x,y)
plt.title("Daily Activity")
plt.xlabel("Average Pluse")
plt.ylabel("Calories Burange")

plt.show()"""

#---------------------------- 
# Font Properties for Tile And Lables
"""import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}

plt.title("Daily Activity", fontdict = font1)
plt.xlabel("Average Pluse", fontdict = font2)
plt.ylabel("Calories Burnage", fontdict = font2)

plt.plot(x, y)
plt.show()"""

#--------------------------
# Matplotlib adding Grid Lines
"""import matplotlib.pyplot as plt
import numpy as np 

x= np.array([10,15,20,25,30,35,40,45,50,55])
y= np.array([110,120,130,140,150,160,170,180,190,200])

plt.title("daily activity")
plt.xlabel("average pluse")
plt.ylabel("calories burnage")

plt.plot(x,y)
#plt.grid()
#plt.grid(axis='x')#display grid lines in x-axis
#plt.grid(axis='y')#display grid lines in y-axis
plt.show()"""

#-------------------------- 
# setting lines properties for the grid

"""import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("daily activity")
plt.xlabel("average pluse")
plt.ylabel("calories burnage")

plt.plot(x, y)

plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

plt.show()"""

#-----------------------------------------------------
# display multiple plots
"""import matplotlib.pyplot as plt
import numpy as np

x= np.array([1,2,3,4,5])
y=np.array([3,5,7,9,3])
plt.subplot(1,2,1)
plt.plot(x,y)

x=np.array([1,2,3,4,5])
y=np.array([10,20,30,40,50])

plt.subplot(1,2,2)
plt.plot(x,y)

plt.show()"""

#------------------------------------ 
# Titles in subplots 
"""import matplotlib.pyplot as plt
import numpy as np

x= np.array([1,2,3,4,5])
y=np.array([3,5,7,9,3])
plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("insourse")

x=np.array([1,2,3,4,5])
y=np.array([10,20,30,40,50])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("outsourse")

plt.suptitle("bikes")# add title on first 
plt.show()"""

#-------------------------------------------------
# Matplotlib Scatter plots 
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

plt.scatter(x, y)
plt.show()"""
#------------------------------------------------------
# make 2 plots on the same graph
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y)

x= np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y= np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x, y)
plt.show()"""
#----------------------------------
# Change color in graphs
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
plt.scatter(x,y,color='hotpink')# Adding color 

x= np.array([2,2,8,1,15,8,12,9,7,3,11,4,7,14,12])
y= np.array([100,105,84,105,90,99,90,95,94,100,79,112,91,80,85])

plt.scatter(x, y, color='#88c999')# Adding color
plt.show()"""

#---------------------------------------
# matplotlib ColorMap
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x, y, c=colors, cmap='viridis')

plt.colorbar()#if we have to add colorbar on side

plt.show()"""
#-------------------------
# set size of the dot
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
sizes =np.array([20,50,100,200,500,1000,60,90,10,300,600,800,75])

# plt.scatter(x, y,s=sizes)
plt.scatter(x, y, s=sizes, alpha=0.5) #by using alpha we can own size for the markers
plt.show()"""
#---------------------------------------------------------

# Matplotlib Bars
"""import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([2,5,8,6])

plt.bar(x,y)
plt.show()"""
#----------------------------------------------------
"""import matplotlib.pyplot as plt
import numpy as np

x=np.array(["mango","kivi"])
y=np.array([2,5])

#plt.bar(x,y)
plt.barh(x,y)# agar bar ko horizantal show karwana hoto
plt.show()"""

#--------------------------------------------
# Bars color change
"""import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([2,5,8,6])

plt.bar(x,y,color="hotpink")
#plt.barh(x,y,color="hotpink")
plt.show()"""
#-----------------------------------
# bars width
"""import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([2,5,8,6])

plt.bar(x,y,color="hotpink",width=0.3)
plt.show()"""

#---------------------
# bar height
"""import matplotlib.pyplot as plt
import numpy as np

x=np.array(["A","B","C","D"])
y=np.array([2,5,8,6])

plt.barh(x,y,color="hotpink",height=0.3)
plt.show()"""

#---------------------------------
# Matplotlib Histograms
"""import matplotlib.pyplot as plt
import numpy as np

x = np.array([150, 155, 160, 162, 165, 168, 170, 172, 175, 180])

plt.hist(x)
plt.show()"""

#-------------------------------------------------
# Matplotlib Pie Charts
"""import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 15, 25, 25])

plt.pie(y)
plt.show()"""

# labels in pie chart
"""import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()"""

# we have to pul the edge wedge 0.3 from the centre of the pie
import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode=[0.3,0.1,0,0]
plt.pie(y,labels=mylabels,explode=myexplode)

plt.show() 