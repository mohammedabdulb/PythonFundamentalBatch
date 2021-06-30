#!/usr/bin/env python
# coding: utf-8

# In[12]:


with open('TSRController.txt') as file_object:
    contents = file_object.read()


# In[13]:


print(contents)


# In[14]:


with open('TSRController.txt') as f:
    print(f.read())


# In[26]:


# Append the data into the file
with open('TSRController.txt','w') as abc:
    abc.write("python is a most demanding prog lang")
abc.close()

with open('TSRController.txt') as t:
    print(t.read())


# In[20]:


#Note :- Here whole file is got overwritte, now lets try to append the data in the last without modifying the file.


# In[27]:


# Append the data into the file
with open('TSRController.txt','a') as abc:
    abc.write("\n python syntaxes are simple")
abc.close()

with open('TSRController.txt') as t:
    print(t.read())


# In[28]:


#Note :- in above example just line got appended in the last , whole file we didn't override.


# In[29]:


# Try Except block :- Introduction to Exceptional Handling.
x = 5
y = 0

z = x/0
print(z)


# In[31]:


#note :- Here whole your code is exposed , hackers use this weak point to attack . Like ransomewhere attack happened  in past.
# Hence you should use Exceptional handling here.


# In[33]:


try:
    x = 5
    y = 0

    z = x/0
    print(z)
except ZeroDivisionError:
    print("dont try to divide a number by zero")
    


# In[ ]:




