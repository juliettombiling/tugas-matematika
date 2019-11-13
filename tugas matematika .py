#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sympy
from sympy import limit
from sympy.abc import x


# In[3]:


print ("1")
limit((2*x**2+x-15)/(x**2+7*x+12),x,4)


# In[4]:


print ("2")
limit ((3*x**2-14*x+8)/(x**2-3*x-4),x,4)


# In[5]:


print ("3")
limit ((x**2-5*x+6)/(x**2+2*x-8),x,2)


# In[6]:


print ("4")
limit((x**2-9)/(x**2-x-6),x,3)


# In[1]:


print("Untuk tugas ke-2 saya menggunakan function sym.init_printing untuk mendapatkan hasil printing yang paling baik. Lalu, taruh perintah untuk bisa membaca symbol dari rumus limit dan juga menambahkan rumusnya yaitu sym.Limit(1/x,x,sym.oo)")


# In[2]:


import sympy as sym
sym.init_printing()
x = sym.symbols('x')

sym.Limit (1 / x, x, sym.oo)


# In[3]:


print ("grup 1")
sym.Limit ((x**2-1)/ (x-1) ,x,1)


# In[4]:


print ("jawaban")
sym.Limit((x**2-1)/(x-1),x,1).doit()


# In[5]:


print("Untuk tugas ke-3 adalah tugas Integral maka jangan lupa menambah kode Integral yah!!")


# In[6]:


import sympy as sym
sym.init_printing()
a, b, x, y, z, t, w, = sym.symbols('a b x y z t w')


# In[7]:


print ('1')
sym.Integral (4*x**6-2*x**3+7*x-4)


# In[8]:


print ('jawaban')
sym.integrate (4*x**6-2*x**3+7*x-4)


# In[9]:


print ('6')
sym.Integral (3*sym.sqrt(w)+10*sym.sqrt(w**3))


# In[10]:


print ('6')
sym.integrate (3*sym.sqrt(w)+10*sym.sqrt(w**3))


# In[11]:


print ('11')
sym.Integral (sym.sqrt(z)*(z**2-1/(4*z)))


# In[12]:


print ('11')
sym.integrate (sym.sqrt(z)*(z**2-1/(4*z)))


# In[13]:


print ('16')
sym.Integral (12 + csc(x)*(sin(x)+csc(x)))


# In[ ]:




