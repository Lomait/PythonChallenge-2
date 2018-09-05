
# coding: utf-8

# In[2]:

l1=['car', 'device', 'fruit' , 'sport']
l2=['apple', 'tennis', 'computer','mercedes']
MyDict=[]
for i in l1:
    for j in l2:
        if i=='car' and j=='mercedes':
            MyDict.append([i, j])
        elif i=='device' and j=='computer':
            MyDict.append([i, j])
        elif i=='fruit' and j=='apple':
            MyDict.append([i, j])
        elif i=='sport' and j=='tennis':
            MyDict.append([i, j])
            print 'MyDict=',dict(MyDict)


# In[ ]:



