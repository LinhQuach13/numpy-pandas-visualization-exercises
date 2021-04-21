#Exercises Part I
# Make a file named pandas_series.py or pandas_series.ipynb for the following 
# exercises.

#  1. Use pandas to create a Series from the following data:

# ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]
 
 # Name the variable that holds the series fruits.
import pandas as pd
import matplotlib.pyplot as plt

fruits= pd.Series(["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"])

# Determine the number of elements in fruits.
fruits.count()

# Output only the index from fruits.
fruits.index

# Output only the values from fruits.
fruits.values

# Confirm the data type of the values in fruits.
type(fruits)

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

# Determine the most frequently occurring fruit name from the series.
fruits_vc[fruits_vc==fruits_vc.max()]

# Determine the least frequently occurring fruit name from the series.
fruits_vc[fruits_vc==fruits_vc.min()]

#another way to do problem above
f_list=[]
for f in fruits_vc.keys():
    if fruits_vc[f]==fruits_vc.min():
        f_list.append(f)



# Exercises Part II
# Explore more attributes and methods while you continue to work 
# with the fruits Series.


# - 1. Capitalize all the string values in fruits.
fruits.str.capitalize()


# - 2. Count the letter "a" in all the string values (use string vectorization).
fruits.str.count('a')


# - 3. Output the number of vowels in each and every string value.
fruits.str.count('[aeiou]') 


# - 4. Write the code to get the longest string value from fruits.
lns= fruits.apply(len).nlargest(1)
fruits[lns.idxmax()]


# - 5. Write the code to get the string values with 5 or more letters in the name.
ag= fruits.str.len() >= 5


# - 6. Use the .apply method with a lambda function to find the fruit(s) 
# containing the letter "o" two or more times.
fruits[fruits.apply(lambda fruit: fruit.count('o') > 1)]


# - 7. Write the code to get only the string values containing the
#  substring "berry".
fruits[fruits.str.contains('berry')]


# - 8. Write the code to get only the string values containing the 
# substring "apple".

fruits[fruits.str.contains('apple')]

# - 9. Which string value contains the most vowels?
fruits[fruits.str.count('[aeiou]').max()]




# Exercises Part III
# Use pandas to create a Series named letters from the following string:

#     'hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy'

# 1. Which letter occurs the most frequently in the letters Series?
letters.value_counts().idxmax()

# 2. Which letter occurs the Least frequently?
letters.value_counts().idxmin()

# 3. How many vowels are in the Series?
total_vowels= sum(letters.str.count('[aeiou]'))

# 4. How many consonants are in the Series?
letters.str.lower().str.count('[^aeiou]').sum()   

# 5. Create a Series that has all of the same letters but uppercased.
letters.str.upper()

# 6. Create a bar plot of the frequencies of the 6 most commonly occuring letters.
#To see all count of all letters in list
import matplotlib.pyplot as plt


letters.value_counts().plot.bar(rot=0)

plt.show()

sorted_letters= letters.value_counts().sort_values() #sorted all values

sorted_letters.tail(6).plot.bar(rot=0) # Most common values were the last 6 values, plotted the last 6 values in sorted list

plt.show()

# Use pandas to create a Series named numbers from the following list:

#     ['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', 
# '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', 
# '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', 
# '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', 
# '$2,791,759.67', '$769,681.94', '$452,650.23']

# make the list a pd series
numbers= pd.Series(['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23'])


# 7. What is the data type of the numbers Series?
type(numbers)

# 8. How many elements are in the number Series?
len(numbers.keys())


# 9. Perform the necessary manipulations by accessing Series attributes and methods to
#  convert the numbers Series to a numeric data type.


num=numbers.str.replace("$", " ").str.replace(",","") # make a string to be able to vectorize and use replace to replace $ and ,


num.astype('float') #make num variable a float datatype


# 10. Run the code to discover the maximum value from the Series.
nms.max()


# 11. Run the code to discover the minimum value from the Series.
nms.min()

# 12. What is the range of the values in the Series?
nms.max()-nms.min()


# 13. Bin the data into 4 equally sized intervals or bins and 
# output how many values fall into each bin.
b_num= nms.value_counts(bins=4)
pd.cut(nms, 4)
pd.cut(nms, 4).value_counts().sort_index()

# 14. Plot the binned data in a meaningful way. Be sure to include a title and axis labels.

nms.value_counts(bins=4).sort_index(ascending=False).plot(kind='barh', 
                                                                   color='g',  
                                                                   width=1)

plt.title('4 bins')
plt.xlabel('Count')
plt.ylabel('US dollars in ($)')
plt.show()


# Use pandas to create a Series named exam_scores from the following list:

#     [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]


exam_scores= pd.Series([60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78])

#  15. How many elements are in the exam_scores Series?
len(exam_scores.keys())


#  16. Run the code to discover the minimum, the maximum, the mean, and the median 
#   scores for the exam_scores Series.
exam_scores.describe()


#17.  Plot the Series in a meaningful way and make sure your chart has a
#  title and axis labels.
exam_scores.plot.hist(color='magenta')

plt.title('Distribution of Scores')
plt.xlabel('Scores')
plt.show()


#  18. Write the code necessary to implement a curve for your exam_grades Series and 
#  save this as curved_grades. Add the necessary points to the highest grade to make
#  it 100, and add the same number of points to every other score 
#  in the Series as well.
c = 100 - exam_scores.max()

c_scores = exam_scores + c


#  19. Use a method to convert each of the numeric values in the curved_grades Series into a categorical value of letter grades. For example, 86 should be a 'B' 
#  and 95 should be an 'A'. Save this as a Series named letter_grades.
bin_e = [0, 70, 75, 80, 90, 101]
bin_labels = ['F', 'D', 'C', 'B', 'A']

grades = pd.cut(c_scores, bins=bin_e, labels=bin_labels)


# 20. Plot your new categorical letter_grades Series in a meaninful way 
# and include a title and axis labels.

grades.value_counts().sort_index().plot.barh(color='mediumorchid',
                                                    ec='black',
                                                    width=.8)

plt.title('Grades')
plt.xlabel('# of Students')
plt.ylabel('Letter Grade')

plt.show()
 




