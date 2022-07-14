#!/usr/bin/env python
# coding: utf-8

# In[212]:


import numpy as np
import matplotlib.pyplot as plt


# In[90]:


#TOTAL NUMBER OF KLEBSIELLA PNEUMONIAE BACTEREMIA CASES AT MDACC

import matplotlib.pyplot as plt

# function to add value labels
def addlabels(x,y):
	for i in range(len(x)):
		plt.text(i, y[i], y[i], ha = 'center',fontsize=10,color='b')


# creating data on which bar chart will be plot
x = ['2016', '2017', '2018', '2019', '2020','2021','2022']
y = [72,112,106,99,74,66,38]

# setting figure size by using figure() function
plt.figure(figsize = (10, 5))

# making the bar chart on the data
plt.bar(x, y, color='r', width=0.5,label='Kp')

# calling the function to add value labels
addlabels(x, y)

# giving title to the plot
plt.title("Klebsiella pneumoniae bacteremia MDACC",fontsize = 10, fontweight = 'bold' )

# giving X and Y labels
plt.xlabel("Year",fontsize = 14, fontweight = 'bold')
plt.ylabel("No of cases", fontsize = 14, fontweight = 'bold')

# visualizing the plot
plt.savefig('bacteremia_Kp.png',dpi=400)
plt.show()


# In[109]:


#NO OF ESBL POSITIVE CASES 

import matplotlib.pyplot as plt
import numpy as np


labels = ['2016', '2017', '2018', '2019', '2020','2021','2022']
Kp = [72,112,106,99,74,66,38]
ESBL = [16,34,41,44,30,30,20]


x = np.arange(len(labels))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize =(8, 6))
rects1 = ax.bar(x - width/2, Kp, width, label='Kp',color='r')
rects2 = ax.bar(x + width/2, ESBL, width, label='ESBL',color='g')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('No of Cases', fontweight ='bold', fontsize = 12)
ax.set_title("ESBL_Kp 2016-2022",fontsize = 14, fontweight = 'bold')
ax.set_xlabel('Year', fontweight ='bold', fontsize = 12)
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()
plt.savefig('ESBL_Kp.png',dpi=400)
plt.show()


# In[155]:


#STACKED GRAPH FOR ESBL SELECTION CRITERIA

import matplotlib.pyplot as plt
import numpy as np

def addlabels(x,y):
	for i in range(len(x)):
		plt.text(i, y[i], y[i], ha = 'center',fontsize=10,fontweight='bold')

fig, ax = plt.subplots(figsize =(8, 6))
x = ['2016', '2017', '2018', '2019', '2020','2021','2022']



ESBL = [16,34,41,44,30,30,20]
CROR_only = np.array([7,1,2,2,2,4,0])
ESBL_only = np.array([0,5,3,6,1,1,0])
CROR_ESBL = np.array([9,28,36,36,27,25,20])

  
# plot bars in stack manner
ax.bar(x, CROR_only,color='g')
ax.bar(x, ESBL_only,bottom=CROR_only, color='c')
ax.bar(x, CROR_ESBL,bottom=CROR_only+ESBL_only, color='y')
ax.set_xlabel("Year", fontsize=14,fontweight ='bold')
ax.set_ylabel("No of cases",fontsize=14,fontweight ='bold')
ax.legend(["CROR_only", "ESBL_only", "CROR_ESBL"])
addlabels(x,ESBL)

for bar in ax.patches:
    height = bar.get_height()
    width = bar.get_width()
    x = bar.get_x()
    y = bar.get_y()
    label_text = height
    label_x = x + width / 2
    label_y = y + height / 2
    if height > 0:
         ax.text(label_x, label_y, label_text, ha='center',color='w',fontweight ='bold',    
            va='center',fontsize=11)

    


plt.title("ESBL Selection Criteria",fontsize=14,fontweight ='bold' )
plt.savefig('ESBL_selection.png',dpi=400)
plt.show()


# In[190]:


#PIE CHART FOR REPEAT INFORMATION

import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots(figsize =(8,6))
y = np.array([159,56])
mylabels = ["Unique samples", "Repeat samples"]


ax.pie(y,labels=mylabels,autopct='%.1f%%')
plt.tight_layout()
plt.savefig('Repeat_info.png',dpi=400)


# In[211]:


#DETAILED REPEAT INFORMATION

import matplotlib.pyplot as plt

# function to add value labels
def addlabels(x,y):
	for i in range(len(x)):
		plt.text(i, y[i], y[i], ha = 'center',fontsize=10,color='r')


# creating data on which bar chart will be plot
x = ['≥1 year','≥6 months', '<6 months','<1 month','30 days','10-20 days', '<10 days','same day']
y = [8,10,10,19,8,4,7,4]

# setting figure size by using figure() function
plt.figure(figsize = (12, 5))

# making the bar chart on the data
plt.bar(x, y, color='c', width=0.5,label='Kp')


# calling the function to add value labels
addlabels(x, y)

# giving title to the plot
plt.title("Repeat information",fontsize = 12, fontweight = 'bold' )

# giving X and Y labels
plt.xlabel("Time",fontsize = 12, fontweight = 'bold')
plt.ylabel("No of isolates", fontsize = 12, fontweight = 'bold')

# visualizing the plot
plt.savefig('repeat_total.png',dpi=400)
plt.show()


# In[222]:


#OVERALL GRAPH OF ESBL and NON_ESBL isolates

import matplotlib.pyplot as plt
import numpy as np


labels = ['2016', '2017', '2018', '2019', '2020','2021','2022']
Kp = [72,112,106,99,74,66,38]
ESBL = [16,34,41,44,30,30,20]
Non_ESBL=[56,78,65,55,44,36,18]


br1 = np.arange(len(labels))# the label locations
br2 =[x + width for x in br1]
br3 = [x + width for x in br2]
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize =(8, 6))
rects1 = ax.bar(br1, Kp, width, label='Kp',color='r')
rects2 = ax.bar(br2,Non_ESBL, width, label='Non_ESBL',color='c')
rects3 = ax.bar(br3, ESBL, width, label='ESBL',color='g')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('No of Cases', fontweight ='bold', fontsize = 12)
ax.set_title("ESBL_Kp 2016-2022",fontsize = 14, fontweight = 'bold')
ax.set_xlabel('Year', fontweight ='bold', fontsize = 12)
ax.set_xticks(x, labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()
plt.savefig('ESBL_Non_ESBL_Kp.png',dpi=400)
plt.show()


# In[233]:


#ESBL rates

import matplotlib.pyplot as plt

# function to add value labels
def addlabels(x,y):
	for i in range(len(x)):
		plt.text(i, y[i], y[i], ha = 'center',fontsize=10)

labels = ['2016', '2017', '2018', '2019', '2020','2021','2022']
ESBL = [22.2,30.4,38.7,44.4,40.5,45.5,52.6]

plt.figure(figsize = (12, 5))

# making the bar chart on the data
plt.plot(labels, ESBL, color='r',label='ESBL_rate',marker='o')


# calling the function to add value labels


# giving title to the plot
plt.title("ESBL_rates",fontsize = 12, fontweight = 'bold' )

# giving X and Y labels
plt.xlabel("Year",fontsize = 12, fontweight = 'bold')
plt.ylabel("ESBL%", fontsize = 12, fontweight = 'bold')


plt.grid(True)
plt.savefig('ESBL_rates.png',dpi=400)
plt.show()


# In[239]:


#FINAL COUNT


import matplotlib.pyplot as plt

# function to add value labels
def addlabels(x,y):
	for i in range(len(x)):
		plt.text(i, y[i], y[i], ha = 'center',fontsize=10, fontweight = 'bold')
        
x = ['unique_ESBL', 'available_databank','already_sequenced', 'to_be_sequenced']
y = [159, 142, 20, 122]

plt.figure(figsize = (8, 5))

# making the bar chart on the data
plt.bar(x, y, color='c', width=0.2,label='Kp')


# calling the function to add value labels
addlabels(x, y)

# giving title to the plot
plt.title("Final count",fontsize = 12, fontweight = 'bold' )

# giving X and Y labels
plt.xlabel("Catergory",fontsize = 12, fontweight = 'bold')
plt.ylabel("No of isolates", fontsize = 12, fontweight = 'bold')

# visualizing the plot
plt.savefig('final_total.png',dpi=400)
plt.show()


# In[ ]:





# In[ ]:




