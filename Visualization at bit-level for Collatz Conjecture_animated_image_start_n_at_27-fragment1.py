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


### User input
n = 27
###


# In[2]:


# Conform to positive integer n
n = max(1, abs(int(n)))
print(n)


# ### Calculation of sequence counting each odd term as an iteration

# In[3]:


count_to_terminate_iterations = 100


# In[4]:


sequence_odd_terms = []
sequence_math_step_1, sequence_math_step_2, sequence_math_step_3, sequence_math_step_4 = [], [], [], []

for count_iterations in range(count_to_terminate_iterations):
    while (not (n % 2)):
        n /= 2
        n = int(n)
    print('Odd term n == ', n, 'at iteration ', count_iterations)
    sequence_odd_terms.append(n)
    n -= 1
    sequence_math_step_1.append(n)
    n /= 2
    n = int(n)
    sequence_math_step_2.append(n)
    n *= 3
    n = int(n)
    sequence_math_step_3.append(n)
    n += 2
    sequence_math_step_4.append(n)
    if (n <= 2):
        print('Terminated upon reaching n == 1 at iteration ', count_iterations)
        break
else:
    print('Terminated with n == ', n,' without reaching n == 1 after iteration ', count_iterations)


# In[5]:


print(len(sequence_odd_terms))


# In[6]:


print(sequence_odd_terms)

