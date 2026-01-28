#!/usr/bin/env python
# coding: utf-8

# In[3]:


num=[]
n=int(input("ENTER THE LIMIT "))
print("ENTER THE NUMBERS")
for i in range(n):
    num.append(int(input()))
num.sort()
print("SORTED DATA",num)
length=len(num)
if length%2==0:
    median=(num[length//2-1]+num[length//2])/2
    lower_half=num[:length//2]
    upper_half=num[length//2:]
else:
    median=num[length//2]
    lower_half=num[:length//2]
    upper_half=num[length//2+1:]
def find_median(num):
    l=len(num)
    if l%2==0:
        return (num[l//2-1]+num[l//2])/2
    else:
        return num[l//2]
Q1 = find_median(lower_half)
Q3 = find_median(upper_half)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
out=[]
for x in num:
    if x<lower_bound or x>upper_bound:
        out.append(x)
print("\n--- STATISTICAL SUMMARY ---")
print("Median:", median)
print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print("Lower Bound:", lower_bound)
print("Upper Bound:", upper_bound)
print("Outliers:", out)


# In[ ]:




