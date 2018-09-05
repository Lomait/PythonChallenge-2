
# coding: utf-8

# In[1]:

f={'input.txt':'randy', 'code.py':'stan', 'output.txt':'randy', 'test.py':'ali', 'djangoweb.py':'ali'}      
import collections
from collections import defaultdict
vv = defaultdict(list)

kk=f.items()
#print kk
#print kk[4]
for k , v in kk:
    vv[v].append(k)
print dict(vv) 


# In[ ]:



