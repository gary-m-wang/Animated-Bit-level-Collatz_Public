#!/usr/bin/env python
# coding: utf-8

# ### Visualization

# In[7]:


#importing some useful packages

# %matplotlib notebook
get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# from PIL import Image, ImageDraw

# from array import *

# import numpy as np


#  - Traditional line plot

# In[8]:


plt.plot(sequence_odd_terms)


#  - Binary: 1 bits on background of 0 bits, shown as static image

# In[9]:


# Bit-wise mask to cut off uppermost bits (MSB end) which will leave lowermost bits (LSB end) for display
number_of_bits_to_display = 12


# In[10]:


bits_list = list(2 ** bit for bit in range(number_of_bits_to_display))


# In[11]:


print(bits_list)


# In[12]:


plt.imshow([bits_list], cmap = 'gray')


# In[13]:


bits_mask = list(bits_list)
bits_mask.reverse()


# In[14]:


print(bits_mask)


# In[15]:


plt.imshow([bits_mask], cmap = 'gray')


# In[16]:


# Python has no built in sign or signum function
# sign = lambda x: -1 if x < 0 else (1 if x > 0 else (0 if x == 0 else NaN))


# In[17]:


image_mask = []
for each_bit in bits_list:
    image_row = []
    for each_mask in bits_mask:
        if (each_bit & each_mask):
            image_row.append(1)
        else:
            image_row.append(0)
    image_mask.append(image_row)


# In[18]:


print(image_mask[0], image_mask[-1])


# In[19]:


plt.imshow(image_mask, cmap = 'gray')


# In[20]:


image_odd_terms = []
for each_odd_term in sequence_odd_terms:
    image_row = []
    for each_mask in bits_mask:
        if (each_odd_term & each_mask):
            image_row.append(1)
        else:
            image_row.append(0)
    image_odd_terms.append(image_row)


# In[21]:


print(image_odd_terms[0], image_odd_terms[-1])


# In[22]:


plt.imshow(image_odd_terms, cmap = 'gray')

