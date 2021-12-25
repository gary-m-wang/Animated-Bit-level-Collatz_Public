#!/usr/bin/env python
# coding: utf-8

# ## Begin with end in mind: image display animating the 'motion' of 1 bits on background of 0 bits (so as to ignore the 0's being non-interesting)

#  - Python is good choice for coding because of readily available package to plot and show image

# ### Program Description
# Implement by an inner loop nested inside an outer loop
#  - Inner loop is to repeat, while n is even, calculating (n /= 2), until n becomes odd
#  - Then knowing n being odd, execute four math steps
#  1. (n -= 1)
#  2. (n /= 2)
#  3. (n *= 3)
#  4. (n += 2)
#  - All of the above are put in the outer loop, to repeat indefinitely in principle. Yet for practicality, make it termiate after some set number of iterations, or reaching (n == 1), whichever comes first.

# ### User input to set starting positive interger n

# In[1]:


import numpy as np


# In[2]:


### User input
start_n = 7
###


# In[3]:


# Conform to dtype = np.uint64 positive integer n
start_n = max(1, abs(int(start_n)))
start_n = np.array([start_n], dtype = np.uint64)


# In[4]:


print([start_n])


# ### Calculation of sequence counting each odd term as an iteration

# In[5]:


count_to_terminate_iterations = 100


# In[6]:


sequence_odd_terms = np.array([], dtype = np.uint64)
sequence_math_step_1 = np.array([], dtype = np.uint64)
sequence_math_step_2 = np.array([], dtype = np.uint64)
sequence_math_step_3 = np.array([], dtype = np.uint64)
sequence_math_step_4 = np.array([], dtype = np.uint64)


# In[7]:


n = start_n


# In[8]:


for count_iterations in range(count_to_terminate_iterations):
    while (not (n[0] % 2)):
        n[0] /= 2
    print('Odd term n == ', n[0], 'at iteration ', count_iterations)
    sequence_odd_terms = np.append(sequence_odd_terms, n)
    n[0] -= 1
    sequence_math_step_1 = np.append(sequence_math_step_1, n)
    n[0] /= 2
    sequence_math_step_2 = np.append(sequence_math_step_2, n)
    n[0] *= 3
    sequence_math_step_3 = np.append(sequence_math_step_3, n)
    n[0] += 2
    sequence_math_step_4 = np.append(sequence_math_step_4, n)
    if (n[0] <= 2):
        print('Terminated upon reaching n == 1 at iteration ', count_iterations)
        break
else:
    print('Terminated with n == ', n[0],' without reaching n == 1 after iteration ', count_iterations)


# In[9]:


print(sequence_odd_terms.size)


# In[10]:


print([sequence_odd_terms])


# ### Visualization

#  - Binary: 1 bits on background of 0 bits, shown as static image

# In[11]:


from PIL import Image, ImageDraw, ImageFont


# In[12]:


# Bit-wise mask to cut off uppermost bits (MSB end) which will leave lowermost bits (LSB end) for display
number_of_bits_to_show = 12


# In[13]:


array_bits_show = np.fromiter((2 ** bit for bit in range(number_of_bits_to_show)), dtype = np.uint64)
array_reversed_bits_show = np.fromiter((2 ** bit for bit in reversed(range(number_of_bits_to_show))), dtype = np.uint64)


# In[14]:


array_mask = np.bitwise_and(np.transpose([array_bits_show]), array_reversed_bits_show)
array_mask_binary = np.array(array_mask != 0, dtype = np.uint8)
array_mask_color = np.stack((array_mask_binary * 255, array_mask_binary * 191, array_mask_binary * 127), axis = -1)


# In[15]:


pil_image_mask = Image.fromarray(array_mask_color)
pil_image_mask_x100 = pil_image_mask.resize((pil_image_mask.size[0] * 100, pil_image_mask.size[1] * 100), resample = 0)


# In[16]:


pil_image_mask_x100.show()


# In[17]:


array_odd_terms = np.bitwise_and(np.transpose([sequence_odd_terms]), array_reversed_bits_show)
array_odd_terms_binary = np.array(array_odd_terms != 0, dtype = np.uint8)
array_odd_terms_color = np.stack((array_odd_terms_binary * 255, array_odd_terms_binary * 191, array_odd_terms_binary * 127), axis = -1)


# In[18]:


pil_image_odd_terms = Image.fromarray(array_odd_terms_color)
pil_image_odd_terms_x100 = pil_image_odd_terms.resize((pil_image_odd_terms.size[0] * 100, pil_image_odd_terms.size[1] * 100), resample = 0)


# In[19]:


pil_image_odd_terms_x100.show()


# In[20]:


pil_image_odd_terms_x100.save('pil_image_odd_terms_x100.png')


# In[21]:


pil_text_on_image_odd_terms_x100 = pil_image_odd_terms_x100.copy()


# In[22]:


# Draw method to position text on image
font_arial = ImageFont.truetype('arial.ttf', 50)
fill_color = (0, 255, 0)
pil_draw_static = ImageDraw.Draw(pil_text_on_image_odd_terms_x100)


# In[23]:


text_mod = '(odd terms) % ' + str(2 ** number_of_bits_to_show)
position_mod = (250, 5)
pil_draw_static.text(position_mod, text_mod, font = font_arial, fill = fill_color)


# In[24]:


for enumerator, each_odd_term in enumerate(sequence_odd_terms):
    text_str = ''
    for each_element in array_odd_terms[enumerator]:
        if (text_str == ''):
            text_str = ' = ' + str(each_element)
        else:
            text_str = text_str + ' + ' + str(each_element)
    text_str = str(int(each_odd_term % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*enumerator)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)


# In[25]:


pil_text_on_image_odd_terms_x100.show()


# In[26]:


pil_text_on_image_odd_terms_x100.save('pil_text_on_image_odd_terms_x100.png')


#  - Binary: 1 bits on background of 0 bits, shown as animated image

# In[27]:


# Draw method to position text on image
font_arial = ImageFont.truetype('arial.ttf', 50)
fill_color = (0, 255, 0)


# In[28]:


text_mod = 'for (each odd term) % ' + str(2 ** number_of_bits_to_show)


# In[29]:


array_row_blank = np.zeros(number_of_bits_to_show)


# In[30]:


# number_of_rows_in_frame = 12 # hardcoded with allocation of blank rows where to position text on animated image
array_frame_blank = np.zeros((12, number_of_bits_to_show))


# In[31]:


pil_image_frames = []
for each_odd_term, each_math_step_1, each_math_step_2, each_math_step_3, each_math_step_4 in zip(sequence_odd_terms, sequence_math_step_1, sequence_math_step_2, sequence_math_step_3, sequence_math_step_4):
    array_frame = np.copy(array_frame_blank)

    array_frame[1, :] = np.bitwise_and(each_odd_term, array_reversed_bits_show)
    array_frame_binary = np.array(array_frame != 0, dtype = np.uint8)
    array_frame_color = np.stack((array_frame_binary * 255, array_frame_binary * 191, array_frame_binary * 127), axis = -1)
    pil_image_frame = Image.fromarray(array_frame_color)
    pil_image_frame_x100 = pil_image_frame.resize((pil_image_frame.size[0] * 100, pil_image_frame.size[1] * 100), resample = 0)

    pil_draw_static = ImageDraw.Draw(pil_image_frame_x100)
    position_mod = (250, 5)
    pil_draw_static.text(position_mod, text_mod, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[1, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_odd_term % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*1)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    pil_image_frames.append(pil_image_frame_x100)

    if (each_odd_term == 1):
        break

    array_frame[4, :] = np.bitwise_and(each_math_step_1, array_reversed_bits_show)
    array_frame_binary = np.array(array_frame != 0, dtype = np.uint8)
    array_frame_color = np.stack((array_frame_binary * 255, array_frame_binary * 191, array_frame_binary * 127), axis = -1)
    pil_image_frame = Image.fromarray(array_frame_color)
    pil_image_frame_x100 = pil_image_frame.resize((pil_image_frame.size[0] * 100, pil_image_frame.size[1] * 100), resample = 0)

    pil_draw_static = ImageDraw.Draw(pil_image_frame_x100)
    position_mod = (250, 5)
    pil_draw_static.text(position_mod, text_mod, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[1, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_odd_term % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*1)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[4, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_1 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*4)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    pil_image_frames.append(pil_image_frame_x100)

    array_frame[6, :] = np.bitwise_and(each_math_step_2, array_reversed_bits_show)
    array_frame_binary = np.array(array_frame != 0, dtype = np.uint8)
    array_frame_color = np.stack((array_frame_binary * 255, array_frame_binary * 191, array_frame_binary * 127), axis = -1)
    pil_image_frame = Image.fromarray(array_frame_color)
    pil_image_frame_x100 = pil_image_frame.resize((pil_image_frame.size[0] * 100, pil_image_frame.size[1] * 100), resample = 0)

    pil_draw_static = ImageDraw.Draw(pil_image_frame_x100)
    position_mod = (250, 5)
    pil_draw_static.text(position_mod, text_mod, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[1, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_odd_term % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*1)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[4, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_1 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*4)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[6, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_2 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*6)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    pil_image_frames.append(pil_image_frame_x100)

    array_frame[8, :] = np.bitwise_and(each_math_step_3, array_reversed_bits_show)
    array_frame_binary = np.array(array_frame != 0, dtype = np.uint8)
    array_frame_color = np.stack((array_frame_binary * 255, array_frame_binary * 191, array_frame_binary * 127), axis = -1)
    pil_image_frame = Image.fromarray(array_frame_color)
    pil_image_frame_x100 = pil_image_frame.resize((pil_image_frame.size[0] * 100, pil_image_frame.size[1] * 100), resample = 0)

    pil_draw_static = ImageDraw.Draw(pil_image_frame_x100)
    position_mod = (250, 5)
    pil_draw_static.text(position_mod, text_mod, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[1, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_odd_term % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*1)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[4, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_1 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*4)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[6, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_2 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*6)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[8, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_3 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*8)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    pil_image_frames.append(pil_image_frame_x100)

    array_frame[10, :] = np.bitwise_and(each_math_step_4, array_reversed_bits_show)
    array_frame_binary = np.array(array_frame != 0, dtype = np.uint8)
    array_frame_color = np.stack((array_frame_binary * 255, array_frame_binary * 191, array_frame_binary * 127), axis = -1)
    pil_image_frame = Image.fromarray(array_frame_color)
    pil_image_frame_x100 = pil_image_frame.resize((pil_image_frame.size[0] * 100, pil_image_frame.size[1] * 100), resample = 0)

    pil_draw_static = ImageDraw.Draw(pil_image_frame_x100)
    position_mod = (250, 5)
    pil_draw_static.text(position_mod, text_mod, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[1, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_odd_term % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*1)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[4, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_1 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*4)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[6, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_2 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*6)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[8, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_3 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*8)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    text_str = ''
    for each_element in array_frame[10, :]:
        if (text_str == ''):
            text_str = ' = ' + str(int(each_element))
        else:
            text_str = text_str + ' + ' + str(int(each_element))
    text_str = str(int(each_math_step_4 % (2 ** number_of_bits_to_show))) + text_str
    position_str = (25, 50 + 100*10)
    pil_draw_static.text(position_str, text_str, font = font_arial, fill = fill_color)

    pil_image_frames.append(pil_image_frame_x100)

    # number_of_rows_in_frame = 12 # hardcoded with allocation of blank rows where to position text on animated image
    for shift_up_rows in range(12 - 3):
        array_frame[1:-1, :] = array_frame[2:, :]
        array_frame[-2, :] = np.copy(array_row_blank)
        array_frame_binary = np.array(array_frame != 0, dtype = np.uint8)
        array_frame_color = np.stack((array_frame_binary * 255, array_frame_binary * 191, array_frame_binary * 127), axis = -1)
        pil_image_frame = Image.fromarray(array_frame_color)
        pil_image_frame_x100 = pil_image_frame.resize((pil_image_frame.size[0] * 100, pil_image_frame.size[1] * 100), resample = 0)
        pil_image_frames.append(pil_image_frame_x100)


# In[32]:


for loop_end_freeze_frames in range(3):
    pil_image_frames.append(pil_image_frames[-1])


# In[33]:


array_frame_blank_binary = np.array(array_frame_blank != 0, dtype = np.uint8)
array_frame_blank_color = np.stack((array_frame_blank_binary * 255, array_frame_blank_binary * 191, array_frame_blank_binary * 127), axis = -1)


# In[34]:


pil_image_frame_blank = Image.fromarray(array_frame_blank_color)
pil_image_frame_blank_x100 = pil_image_frame_blank.resize((pil_image_frame_blank.size[0] * 100, pil_image_frame_blank.size[1] * 100), resample = 0)


# In[35]:


for loop_end_blank_frames in range(6):
    pil_image_frames.append(pil_image_frame_blank_x100)


# In[36]:


pil_image_frames[0].save('text_on_animated_image_start_n_at_7.gif', format='GIF', append_images=pil_image_frames[1:], save_all=True, duration=500, loop=0)


# In[ ]:




