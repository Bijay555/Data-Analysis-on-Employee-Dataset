#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as ticker
import statistics


# In[3]:


employee_left= pd.read_csv('Book1.csv')
curr_employee = pd.read_csv('Book2.csv')


# In[4]:


employee_left.head()


# In[5]:


curr_employee.head()


# In[6]:


employee_left.info()


# In[7]:


curr_employee.info()


# In[8]:


employee_left.dept.value_counts()


# This shows the most of the employees who left the company were sales,technical and support. 

# Promotion received by the employee from the dataset of employee who left the company

# In[9]:


employee_left['promotion_last_5years'] = employee_left.promotion_last_5years.replace(to_replace =1, 
                 value ="Yes") 
employee_left['promotion_last_5years'] = employee_left.promotion_last_5years.replace(to_replace =0, 
                 value ="No")
employee_left.promotion_last_5years.value_counts()


# Promotion received by the employee from the dataset of employee who are still in the company

# In[10]:


curr_employee['promotion_last_5years'] = curr_employee.promotion_last_5years.replace(to_replace =1, 
                 value ="Yes") 
curr_employee['promotion_last_5years'] = curr_employee.promotion_last_5years.replace(to_replace =0, 
                 value ="No")
curr_employee.promotion_last_5years.value_counts()


# In[11]:


plt.figure(figsize=(8,5))
sns.countplot(employee_left['salary'])
plt.title('Distribution of salaries of Employees who left the company')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()


# In[12]:


plt.figure(figsize=(8,5))
sns.countplot(curr_employee['salary'])
plt.title('Distribution of salaries of Employees who are still in the company')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()


# Department Plot

# In[14]:


plt.figure(figsize=(12,5))
sns.countplot(employee_left['dept'])
plt.title('Departments of Employees who left the Company')
plt.show()


# In[15]:


plt.figure(figsize=(12,5))
sns.countplot(curr_employee['dept'])
plt.title('Departments of Employees who are still in the Company')
plt.show()


# SATISFACTION LEVEL

# In[16]:


plt.figure(figsize=(14,6))
sns.boxplot(x='dept', y='satisfaction_level', data=employee_left)
plt.ylim([0,1])
plt.title('Distribution of satisfaction level of Employees that left by Department')
plt.xlabel('Department')
plt.ylabel('Satisfaction Level')
plt.show()


# From the above figure we can confirm that the average level of satisfaction for the employee who left the company was around 40%

# In[ ]:





# In[17]:


plt.figure(figsize=(14,6))
sns.boxplot(x='dept', y='satisfaction_level', data=curr_employee)
plt.ylim([0,1])
plt.title('Distribution of satisfaction level by Department of Employees that are still in the company')
plt.xlabel('Department')
plt.ylabel('Satisfaction Level')
plt.show()


# From the above figure we can confirm that the average level of satisfaction for the employee who left the company was around 70%

# Last evaluation and satisfaction level

# In[19]:


plt.figure(figsize=(15,8))
plt.title("last evaluation vs Satisfication level")
sns.scatterplot(x=employee_left['satisfaction_level'],y=employee_left['last_evaluation'],hue='number_project',data=employee_left, palette='cool')
plt.show()


# satisfaction level is high for less no of projects( i.e projects that are 4 or less than 4).
# As the no of projects increases the satisfaction level decresed in the dataset of emplyee who left the company.

# In[ ]:





# In[21]:


plt.figure(figsize=(15,8))
plt.title('Salary vs Satisfaction level')
sns.boxplot(x=employee_left['salary'],y=employee_left['satisfaction_level'],hue='time_spend_company',data=employee_left)
plt.show()


# Point drawn from above plot:
# Average monthly hours is very low for employees who has number of projects equal to 2 for all levels of salary.
# As we can see from the plot the employees from all levels for salary are loaded with projets and monthly hours is high.
# We can see there are so many oultiers from low and meduim salary levels.
# The box plot is bigger for low salary emplyoees who has number of projects equal to 3, 50% of these employees high monthly hours.

# In[ ]:





# In[22]:


plt.figure(figsize=(15,8))
plt.title("Average monthly hours vs promotions in last 5 years")
sns.boxplot(x=employee_left['promotion_last_5years'],y=employee_left['average_montly_hours'],hue='time_spend_company',data=employee_left)
plt.show()


# A lot of information can be collected from the above figure :
# 1. Promotion is given to the employee who has relatively very low average monthly hours.
# 2. There were lots of employee who worked for  extra hours but company didnt consider.
# 3. The employees who has not got the promotion are having higher avrage monthly hours and mostly time spend in the comapny is more than or equal 4 years with few outliers.

# In[ ]:





# In[26]:


plt.figure(figsize=(15,8))
plt.title("Average salary vs promotions in last 5 years")
sns.boxplot(x=employee_left['salary'],y=employee_left['average_montly_hours'],hue='number_project',data=employee_left)
plt.show()


# From the above figure we can get following information:
# 1. Very few employee had high salary.
# 2. There were many employee who used to do more projects and spend more monthly hoursstill have low salary.
# 3. More no of projects means more monthly hours.

# In[27]:


em_left =employee_left.pivot_table(index='salary',columns='promotion_last_5years',values='satisfaction_level')
em_left.plot.bar()
plt.title("Satisfaction Level of Employees who left based on Salary and Promotion Status")
plt.xlabel("Salary Range")
plt.ylabel("Satisfaction Level")


# In[28]:


plt.figure(figsize=(18,10))
plt.title("Department vs Satisfaction level")
sns.boxplot(x=employee_left['dept'],y=employee_left['satisfaction_level'],hue='time_spend_company',data=employee_left)
plt.show()


# Intersting points we can draw from above plot-
# 
# 1. Employees from R&D department having 6 years of time spend having large distribution of satisfaction levels.
# 2. Time spend equal to 4 in all departments are having same level of very low satisfaction levels same goes for time spend equals to 3 having same level of average satisfcations in all departments.
# 3. Employees from sales and Technical department of 2 yeras of time spend is also having larger distributions of satisfaction levels as expected.

# After all these analysis we can predict what were the causes for the employee to leave the company.
# Some of the reason are as follows:
# 1. Employees who are stressed up working more hours and having higher number of projects.
# 2. Mostly from sales and technical department were leaving the company.
# 3. the employees are not getting promotion even they are working tirelessly.

# In[ ]:


If we analysis the existing employee dataset then we can observe


# In[29]:


plt.figure(figsize=(15,8))
plt.title("last evaluation vs Satisfication level")
sns.scatterplot(x=curr_employee['satisfaction_level'],y=curr_employee['last_evaluation'],hue='number_project',data=curr_employee, palette='cool')
plt.show()


# The data looks promising and company also has brought improvement in treatment of their employee.
# But still some of the employee with low satisfaction level are doing more no of projects. this could be prone factor to leave the company.

# In[30]:


plt.figure(figsize=(15,8))
plt.title("Average salary vs promotions in last 5 years")
sns.boxplot(x=curr_employee['salary'],y=curr_employee['average_montly_hours'],hue='number_project',data=curr_employee)
plt.show()


# Still if we observe we find some employee who has high salary but less monthly hours where low salary employee are working harder for longer monthly hours. 

# In[31]:


plt.figure(figsize=(18,10))
plt.title("Department vs Satisfaction level")
sns.boxplot(x=curr_employee['dept'],y=curr_employee['satisfaction_level'],hue='time_spend_company',data=curr_employee)
plt.show()


# In department like technical, marketing, product management and RandD where there are still some employee who has low satisfaction leve;l but  works more that 6 years in company and still havent recived any promotion.
# These employee are more likely to leave the company in the coming days.
