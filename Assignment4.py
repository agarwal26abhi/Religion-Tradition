
# coding: utf-8

# # Assignment 4
# 
# Before working on this assignment please read these instructions fully. In the submission area, you will notice that you can click the link to **Preview the Grading** for each step of the assignment. This is the criteria that will be used for peer grading. Please familiarize yourself with the criteria before beginning the assignment.
# 
# This assignment requires that you to find **at least** two datasets on the web which are related, and that you visualize these datasets to answer a question with the broad topic of **religious events or traditions** (see below) for the region of **Ann Arbor, Michigan, United States**, or **United States** more broadly.
# 
# You can merge these datasets with data from different regions if you like! For instance, you might want to compare **Ann Arbor, Michigan, United States** to Ann Arbor, USA. In that case at least one source file must be about **Ann Arbor, Michigan, United States**.
# 
# You are welcome to choose datasets at your discretion, but keep in mind **they will be shared with your peers**, so choose appropriate datasets. Sensitive, confidential, illicit, and proprietary materials are not good choices for datasets for this assignment. You are welcome to upload datasets of your own as well, and link to them using a third party repository such as github, bitbucket, pastebin, etc. Please be aware of the Coursera terms of service with respect to intellectual property.
# 
# Also, you are welcome to preserve data in its original language, but for the purposes of grading you should provide english translations. You are welcome to provide multiple visuals in different languages if you would like!
# 
# As this assignment is for the whole course, you must incorporate principles discussed in the first week, such as having as high data-ink ratio (Tufte) and aligning with Cairo’s principles of truth, beauty, function, and insight.
# 
# Here are the assignment instructions:
# 
#  * State the region and the domain category that your data sets are about (e.g., **Ann Arbor, Michigan, United States** and **religious events or traditions**).
#  * You must state a question about the domain category and region that you identified as being interesting.
#  * You must provide at least two links to available datasets. These could be links to files such as CSV or Excel files, or links to websites which might have data in tabular form, such as Wikipedia pages.
#  * You must upload an image which addresses the research question you stated. In addition to addressing the question, this visual should follow Cairo's principles of truthfulness, functionality, beauty, and insightfulness.
#  * You must contribute a short (1-2 paragraph) written justification of how your visualization addresses your stated research question.
# 
# What do we mean by **religious events or traditions**?  For this category you might consider calendar events, demographic data about religion in the region and neighboring regions, participation in religious events, or how religious events relate to political events, social movements, or historical events.
# 
# ## Tips
# * Wikipedia is an excellent source of data, and I strongly encourage you to explore it for new data sources.
# * Many governments run open data initiatives at the city, region, and country levels, and these are wonderful resources for localized data sources.
# * Several international agencies, such as the [United Nations](http://data.un.org/), the [World Bank](http://data.worldbank.org/), the [Global Open Data Index](http://index.okfn.org/place/) are other great places to look for data.
# * This assignment requires you to convert and clean datafiles. Check out the discussion forums for tips on how to do this from various sources, and share your successes with your fellow students!
# 
# ## Example
# Looking for an example? Here's what our course assistant put together for the **Ann Arbor, MI, USA** area using **sports and athletics** as the topic. [Example Solution File](./readonly/Assignment4_example.pdf)

# In[194]:

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel("http://www.thearda.com/download/download.aspx?file=U.S.%20Religion%20Census%20Religious%20Congregations%20and%20Membership%20Study,%202010%20(County%20File).XLSX")
df1=pd.read_excel("http://www.thearda.com/download/download.aspx?file=Religious%20Congregations%20and%20Membership%20Study,%202000%20(Counties%20File).XLSX")


# In[193]:

import numpy as np
df=df[df["CNTYNAME"]=="Washtenaw County"]
df1=df1[df1["COUNTY"]=="Washtenaw"]
df2=pd.DataFrame({"EVANGELICAL PROTESTANT":[df["EVANADH"].iloc[0],df1["EVANAD"].iloc[0]],"BLACK PROTESTANT":[df["BPRTADH"].iloc[0],0]
                  ,"MAINLINE PROTESTANT":[df["MPRTADH"].iloc[0],df1["MAINAD"].iloc[0]],"ORTHODOX":[df["ORTHADH"].iloc[0],df1["ORTHAD"].iloc[0]]
                 ,"CATHOLIC":[df["CATHADH"].iloc[0],df1["CATHAD"].iloc[0]],"OTHER":[df["OTHADH"].iloc[0],df1["OTHERAD"].iloc[0]],
                 "UNCLAIMED":[df["POP2010"].iloc[0]-df["TOTADH"].iloc[0],df1["POP200"].iloc[0]-df1["TOTAD"].iloc[0]]},index=[2010,2000])
df2["POPULATION"]=0
for i in range(0,2):
    df2["POPULATION"].iloc[i]=df2.iloc[i].sum()

for i in df2.columns:
    df2[i]=df2[i]/df2["POPULATION"]*100
df2.drop("POPULATION",axis=1,inplace=True)
df2=df2.reindex_axis(["EVANGELICAL PROTESTANT","CATHOLIC","MAINLINE PROTESTANT","ORTHODOX","BLACK PROTESTANT","OTHER","UNCLAIMED"],axis=1)
plt.figure(figsize=(18,8))
plt.bar(range(1,8),df2.iloc[0],width=-.3,label="2010",align="edge",edgecolor="black",alpha=.8)
plt.bar(range(1,8),df2.iloc[1],width=.3,label="2000",align="edge",edgecolor="black",alpha=.8)
ob=plt.gca()
ob.tick_params(bottom="off")
ob.spines["right"].set_visible(False)
ob.spines["top"].set_visible(False)
ob.legend(loc=0,fontsize="x-large")
ob.set_title("Religious Traditions of Ann Arbor city",fontsize="xx-large")
ob.set_xlabel("")
plt.xticks(np.arange(1,8),df2.columns,fontsize="large")
for i in range(0,2):
    lt=list(df2.iloc[i].values)
    for x,y in zip(range(1,8),lt):
        if(i==0):
            ob.text(x-.3,y+1,str(y)[:4]+"%",fontsize="large")
        else:
            ob.text(x+.05,y+1,str(y)[:4]+"%",fontsize="large")
plt.show()






# In[ ]:



