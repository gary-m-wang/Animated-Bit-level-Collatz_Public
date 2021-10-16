#!/usr/bin/env python
# coding: utf-8

#  - Binary: 1 bits on background of 0 bits, shown as animated image

# In[23]:


image_row_blank = list(0 for _ in range(number_of_bits_to_display))


# In[24]:


image_frames = []
for each_odd_term, each_math_step_1, each_math_step_2, each_math_step_3, each_math_step_4 in zip(sequence_odd_terms, sequence_math_step_1, sequence_math_step_2, sequence_math_step_3, sequence_math_step_4):
    image_row_1 = []
    for each_mask in bits_mask:
        if (each_odd_term & each_mask):
            image_row_1.append(1)
        else:
            image_row_1.append(0)

    image_frames.append([image_row_blank, image_row_1, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank])

    if (each_odd_term == 1):
        break

    image_row_4 = []
    for each_mask in bits_mask:
        if (each_math_step_1 & each_mask):
            image_row_4.append(1)
        else:
            image_row_4.append(0)

    image_frames.append([image_row_blank, image_row_1, image_row_blank, image_row_blank, image_row_4, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank])

    image_row_6 = []
    for each_mask in bits_mask:
        if (each_math_step_2 & each_mask):
            image_row_6.append(1)
        else:
            image_row_6.append(0)

    image_frames.append([image_row_blank, image_row_1, image_row_blank, image_row_blank, image_row_4, image_row_blank, image_row_6, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank])

    image_row_8 = []
    for each_mask in bits_mask:
        if (each_math_step_3 & each_mask):
            image_row_8.append(1)
        else:
            image_row_8.append(0)

    image_frames.append([image_row_blank, image_row_1, image_row_blank, image_row_blank, image_row_4, image_row_blank, image_row_6, image_row_blank, image_row_8, image_row_blank, image_row_blank, image_row_blank])

    image_row_10 = []
    for each_mask in bits_mask:
        if (each_math_step_4 & each_mask):
            image_row_10.append(1)
        else:
            image_row_10.append(0)

    image_frames.append([image_row_blank, image_row_1, image_row_blank, image_row_blank, image_row_4, image_row_blank, image_row_6, image_row_blank, image_row_8, image_row_blank, image_row_10, image_row_blank])

    image_frames.append([image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_4, image_row_blank, image_row_6, image_row_blank, image_row_8, image_row_blank, image_row_10, image_row_blank])

    image_frames.append([image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_6, image_row_blank, image_row_8, image_row_blank, image_row_10, image_row_blank])

    image_frames.append([image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_8, image_row_blank, image_row_10, image_row_blank])

    image_frames.append([image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_10, image_row_blank])

    image_frames.append([image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_10, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank])

    image_frames.append([image_row_blank, image_row_10, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank])


# In[25]:


for loop_end_freeze_frames in range(3):
    image_frames.append(image_frames[-1])


# In[26]:


for loop_end_blank_frames in range(6):
    image_frames.append([image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank, image_row_blank])


# In[27]:


plt.imshow(image_frames[0], cmap = 'gray')


# In[28]:


print(len(image_frames))


# In[29]:


print(image_frames[0])


# In[30]:


anim_frames = len(image_frames)
frame_rate = 4

fig = plt.figure(figsize=(8, 8))

im = plt.imshow(image_frames[0], cmap = 'gray', interpolation = 'none', aspect = 'auto', vmin = 0, vmax = 1)

def animate_func(i):
    if (int(i % frame_rate) == 0):
        print('.', end = '')

    im.set_array(image_frames[i])
    return [im]

anim = animation.FuncAnimation(fig, animate_func, frames = anim_frames, interval = 1000 / frame_rate)

anim.save('animated_image_start_n_at_27.gif')

print('Done')


# In[ ]:




