# All the datasets loaded from the pydataset library will be pandas dataframes.
import pandas as pd
import numpy as np
from pydataset import data


# 1. Copy the code from the lesson to create a dataframe full of student grades.
np.random.seed(123)

students = ['Sally', 'Jane', 'Suzie', 'Billy', 'Ada', 'John', 'Thomas',
            'Marie', 'Albert', 'Richard', 'Isaac', 'Alan']

math_grades = np.random.randint(low=60, high=100, size=len(students))
english_grades = np.random.randint(low=60, high=100, size=len(students))
reading_grades = np.random.randint(low=60, high=100, size=len(students))

df = pd.DataFrame({'name': students,
                   'math': math_grades,
                   'english': english_grades,
                   'reading': reading_grades})

type(df)


# a. Create a column named passing_english that indicates whether each student has a passing grade in english.

df_stu= df.copy() #made a copy of dataframe

df_stu['passing_english'] = np.where(df['english']>= 70, True, False) #create new col named passing_english

# b. Sort the english grades by the passing_english column. How are duplicates handled?
sorted_eng_df= df_stu.sort_values(by= 'passing_english', ascending=False)

# c. Sort the english grades first by passing_english and then by student name. All the students that are failing english should be first,
# and within the students that are failing english they should be ordered alphabetically. The same should be true for the students passing english. 
# (Hint: you can pass a list to the .sort_values method)
sorted_eng_df_name= df_stu.sort_values(by= ['passing_english','name'], ascending=[False, True])

# d. Sort the english grades first by passing_english, and then by the actual english grade, similar to how we did in the last step.
sorted_eng_df_grade= df_stu.sort_values(by= ['passing_english','english'], ascending=[False, False])

# e. Calculate each students overall grade and add it as a column on the dataframe. 
# The overall grade is the average of the math, english, and reading grades.
df_stu['overall_grade'] = (df_stu['math']+ df_stu['english'] + df_stu['reading'])/3




# 2. Load the mpg dataset. Read the documentation for the dataset and use it for the following questions:
mpg = data('mpg') 


# a. How many rows and columns are there?
mpg.shape

# b. What are the data types of each column?
mpg.dtypes

# c. Summarize the dataframe with .info and .describe
mpg.info()

mpg.describe()

# d. Rename the cty column to city.
mpg_copy= mpg.rename(columns={'cty': 'city'})

# e. Rename the hwy column to highway.
mpg_copy= mpg_copy.rename(columns={'hwy': 'highway'})

# f.Do any cars have better city mileage than highway mileage?
mpg_copy[mpg_copy.city > mpg_copy.highway] # No cars have better city mileage than highway mileage


# g. Create a column named mileage_difference this column should contain the difference 
# between highway and city mileage for each car.
mpg_copy['mileage_difference']= (mpg_copy['highway'] - mpg_copy['city'])

# h. Which car (or cars) has the highest mileage difference?
sorted_mpg_desc= mpg_copy.sort_values(by='mileage_difference', ascending=False)

sorted_mpg_desc.head() #top 5 cars with the highest mileage difference

# I. Which compact class car has the lowest highway mileage? The best?
mpg_copy[mpg_copy['class'] == 'compact'].sort_values(by = 'highway', ascending = True) # lowest highway mileage
mpg_copy[mpg_copy['class'] == 'compact'].sort_values(by = 'highway', ascending = False) # best highway mileage



# J. Create a column named average_mileage that is the mean of the city and highway mileage.
mpg_copy = mpg_copy.assign(average_mileage= (mpg_copy['city'] + mpg_copy['highway'])/2)

# K. Which dodge car has the best average mileage? The worst?
sorted_dodge_best= mpg_copy[mpg_copy['manufacturer'] == 'dodge'].sort_values(by = 'average_mileage', ascending = False) # best mileage

sorted_dodge_best.head() # isolate top 5 best mileage


sorted_dodge_worst= mpg_copy[mpg_copy['manufacturer'] == 'dodge'].sort_values(by = 'average_mileage', ascending = True) #worse mileage

sorted_dodge_worst.head() # isolate worse 5




# 3. Load the Mammals dataset. Read the documentation for it, and use the data to answer these questions:
mammals = data('Mammals')

mam_df= mammals.copy # make a copy

# -How many rows and columns are there?
mammals.shape

# -What are the data types?
mammals.dtypes

# -Summarize the dataframe with .info and .describe
mammals.info()

mammals.describe()

# -What is the the weight of the fastest animal?
mammals.sort_values(by='speed', ascending=False).head(1)

# -What is the overal percentage of specials?
percent = (mammals['specials'].sum()/len(mammals)) * 100

# -How many animals are hoppers that are above the median speed? What percentage is this?
median_speed= mammals.speed.median()
hoppers= mammals[mammals.hoppers]
hoppers_median = mammals[(mammals['hoppers'] == True) & (mammals['speed'] > median_speed)]
p_hopper= (len(hoppers_median) / len(mammals)) *100