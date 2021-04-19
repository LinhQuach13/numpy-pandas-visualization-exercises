#Use the following code for the questions below:

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])



# 1. How many negative numbers are there?
negative= []
for n in a:
    if n < 0:
        negative.append(n)
        total= len(negative)
print("There are a total of", total, "negative numbers.")



# 2. How many positive numbers are there?
positive= []
for n in a:
    if n > 0:
        positive.append(n)
        total_positives = len(positive)
print("The total number of positive numbers is:", total_positives)


# 3. How many even positive numbers are there?
even_positive= []
for n in a:
    if n > 0 and n % 2 ==0:
        even_positive.append(n)
        total_ep= len(even_positive)
print("There are", total_ep, "positive even numbers")


# 4. If you were to add 3 to each data point, how many positive numbers would there be?
new_array=[]
na_pos= []
for n in a:
    new_array.append(n+3)
for num in new_array:
        if num > 0:
            na_pos.append(num)
            total= len(na_pos)
print("The number of positive numbers after adding three is:", total)




# 5. If you squared each number, what would the new mean and standard deviation be?
n_array=[]
for n in a:
    n_array.append((np.abs(a))**0.5)
    for num in n_array: 
        m= num.mean()
        st= num.std()
print("The mean is:", m)
print("The standard deviation is:", st)
        


# # 6. A common statistical operation on a dataset is centering. 
# # This means to adjust the data such that the mean of the data is 0. 
# # This is done by subtracting the mean from each data point. Center the data set.
# #  See this link for more on centering.

N_array= []
for N in n_array:
    N_array.append(N - m) 



# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# Z=x−μ/ σ
z_score_arr=[]
for n in a:
    z_score_arr.append((n-m)/st)

print("The new list with z-scores for each point is:", z_score_arr)


# 8. Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py 
# and add your solutions.
   #Completed.




import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a= np.sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a= np.min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = np.max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a= np.mean(a)

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all 
# the numbers in the above list together
product_of_a = np.prod(a)

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared 
# like [1, 4, 9, 16, 25...]
squares_of_a= np.square(a)

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a= []
for n in a:
    if n % 2 != 0:
        odds_in_a.append(n)

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a= []
for n in a:
    if n % 2 == 0:
        evens_in_a.append(n)

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and
#  list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, 
# you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)

    #Answer:
    b = np.array([[3, 4, 5], 
             [6, 7, 8]])

    sum_of_b= b.sum()
    print(sum_of_b)

# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
    #Answer: 
min_of_b = b.min()


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
    #Answer: 
max_of_b = b.max()


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
    #answer: 
    mean_of_b= [(b[0].sum() + b[1].sum()/ (b[0].size + b[1].size))]

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number
        #Answer:
product_of_b= b.prod()

# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)
        #Answer: 
        square_of_b= np.square(b)


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)
            #Answer: 
            odds_in_b= b[b%2==1]


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)
            #Answer:
            evens_in_b= b[b%2==0]

# Exercise 9 - print out the shape of the array b.
z= np.broadcast(b)

print(z.shape)

# Exercise 10 - transpose the array b.
trans_b= np.transpose(b)

print(trans_b)


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
m= np.array(b).reshape(1,6)

print(m)

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
n= np.array(b).reshape(6,1)

print(n)

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.

#making it a numpy array
c = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])

# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c= c.min()
max_of_c = c.max()
sum_of_c= c.sum()
prod_of_c =c.prod()


print("Min of C:", min_of_c, "Max of C:", max_of_c, "Sum of C:", sum_of_c, "Product of C:", prod_of_c)


# Exercise 2 - Determine the standard deviation of c.
std_of_c= c.std()

print("The standard deviation of C is:", std_of_c)

# Exercise 3 - Determine the variance of c.
var_of_c= c.var()

print("The variance of C is:", var_of_c)

# Exercise 4 - Print out the shape of the array c
shape_c= np.broadcast(c)

print(c.shape)


# Exercise 5 - Transpose c and print out transposed result.
trans_c= np.transpose(c)

print(trans_c)



# Exercise 6 - Get the dot product of the array c with c. 
dt_prd_c= np.dot(c,c)

print(dt_prd_c)

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. 
# Answer should be 261
trans_c1= np.transpose(c)
mc_c= trans_c1 * c
s_trans_c= mc_c.sum()

print(s_trans_c)

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. 
# Answer should be 131681894400.
multip_c= c*c
trans_m_c= np.transpose(multip_c)
prd_trans_c= trans_m_c.prod()

print(prd_trans_c)


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

#setup
d = np.array([[90, 30, 45, 0, 120, 180], [45, -90, -30, 270, 90, 0], [60, 45, -45, 90, -45, 180]])

# Exercise 1 - Find the sine of all the numbers in d
sine_d= np.sin(d)

# Exercise 2 - Find the cosine of all the numbers in d
cosine_d= np.cos(d)

# Exercise 3 - Find the tangent of all the numbers in d
tangent_d= np.tan(d)

# Exercise 4 - Find all the negative numbers in d
neg_in_d= d[d<0]

print(neg_in_d)

# Exercise 5 - Find all the positive numbers in d
pos_in_d= d[d>0]

print(pos_in_d)

# Exercise 6 - Return an array of only the unique numbers in d.
uniq_d= np.unique(d)

# Exercise 7 - Determine how many unique numbers there are in d.
for dd in d:
    count= len(uniq_d)
    
print(count)

# Exercise 8 - Print out the shape of d.
shape_d= np.broadcast(d)

print(d.shape)

# Exercise 9 - Transpose and then print out the shape of d.
trans_d= np.transpose(d)

print(trans_d)

# Exercise 10 - Reshape d into an array of 9 x 2
A= np.array(d).reshape(9,2)

print(A)