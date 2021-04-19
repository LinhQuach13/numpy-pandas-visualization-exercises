#Exercises Part I
# Make a file named pandas_series.py or pandas_series.ipynb for the following 
# exercises.

#  1. Use pandas to create a Series from the following data:

# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
 
 # Name the variable that holds the series fruits.
import pandas as pd

fruits= pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# Determine the number of elements in fruits.
fruits.count()

# Output only the index from fruits.
fruits.index

# Output only the values from fruits.
fruits.values

# Confirm the data type of the values in fruits.
fruits.dtype

# Output only the first five values from fruits. Output the last three values. Output two random values from fruits.
fruits.head(5) 

fruits.tail(3)

fruits.sample(2)

# Run .describe() on the series to see what describe returns for a series of strings.
fruits.describe()

# Run the code necessary to produce only the unique fruit names.
fruits.unique()

# Determine how many times each value occurs in the series.
fruits_vc= fruits.value_counts()

# e. Determine the most frequently occurring fruit name from the series.
fruits_vc[fruits_vc==fruits_vc.max()]

# f. Determine the least frequently occurring fruit name from the series.
fruits_vc[fruits_vc==fruits_vc.min()]

#another way to do problem above
f_list=[]
for f in fruits_vc.keys():
    if fruits_vc[f]==fruits_vc.min():
        f_list.append(f)




