# ## Topic 4: Arrays

# ### Arrays are similar to lists in many ways.
# ### Differences include:
# ###  -> lists allow hybrid/varied datatypes and arrays do not
# ###  -> arrays allow manipulations to be performed across all elements

# In[32]:


# Array functionality is not available by default so it needs to be imported
from array import array
my_array = array('i',[45,99,67,78])
print(my_array)
my_array.index(67)


# ![arraytypes.png](attachment:arraytypes.png)

# In[33]:


# My array can be converted to the more familiar list type to manipulate
my_list_from_array = my_array.tolist()
my_list_from_array.sort()
print(my_list_from_array)
