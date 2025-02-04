import  numpy as np

arr = np.array([1,2,3])
print(arr)
print(type(arr))
arr1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
'''print (arr1)
arr1 = np.array([[[1,2,3],[4,5,6],[7,8,9]],[[1,2,3],[4,5,6],[7,8,9]]])
print (arr1)
arr1 = np.array([(1,2,3),(4,5,6)])
print (arr1)
x=(1,2,3),(4,5,6)
arr1 = np.array(x)
print (arr1)'''

# write 2 matrices A(3,3) and B(3,3) and do the operation A+B, A-B, 2*B

A= np.array([[1,2,3],[4,5,6],[7,8,9]])
B= np.array([[10,11,12],[13,14,15],[16,17,18]])
'''C= A+B
D= A-B
E= 2*B
print('A+B =',C)
print('A-B = ',D)
print('2*B = ',E)
#matrix multiplication as per element-wise multiplication
F= A*B
print('A*B = ',F)
#matrix multiplication as per linear algebra rules
res = A.dot(B)
print(res)
# compare A to B
print(A<B)
#compare A elements to 2
print(A==2)
# check if B is pair
print(B%2==0)
# calculate he sqrt of B
print(np.sqrt(B))
# calculate the exp of A
print(np.exp(A))
# calculate sin/cos A/B
print(np.sin(A), np.cos(B))
# find the min/max in the matrix
print(A.min(),  A.max())
print(A.min())
print(A.max())
# find SUM A
print(A.sum())

# find the min/max in all ligne
print(A.min(axis=0))
print(B.max(axis=0))
# find the min/max in all column
print(B.max(axis=1), A.min(axis=1))'''

'''
# how to work with matrice
print(A[0])
print(A[0,2])
print(A[0:2])
print(A[0:2][1:3])
# to find the last element in A
print(A[-1])
# find the pair in matrix
print(A[A%2==0])
# find the impair in B
print(B[B%2==0])
# find the element that are superior to the mean
print(A[A>A.mean()])

# how to print the row of the matrix
for row in A:
    print(row)
# how to print element per element in matrix
for row in B:
    for element in row:
        print(element)'''
'''
# Shape manipulation
C = np.array([[ 1,  2,  3,  4,  5,  6],
              [ 7,  8,  9, 10, 11, 12],
              [13, 14, 15, 16, 17, 18]])
print(C)
print(C.reshape(9,2))
print(C.T) #transpose C
# ou bien 
print(C.transpose())'''
'''
#how to fill array
empty_arr =np.empty(shape=(3,4))
print(empty_arr)
arr_zeros = np.zeros(shape = (2,3))
print(arr_zeros)
arr_ones = np.ones(shape = (3,5))
print(arr_ones)
arr_twos = np.full(shape = (2,4), fill_value = 2)
print(arr_twos)
arr_full = np.full(shape = (5,5), fill_value ='two-three')
print(arr_full)
empty_like = np.empty_like(B) #matrix empty but keep de dimention of the like
print(empty_like)
array_rng= np.arange(40)   # print the number from 0 to (n-1) the same Logic as the range in the liste
print(array_rng)
array_rng= np.arange(start=2, stop= 89, step=23)  # we can define the first and last element and the steps as well
print(array_rng)'''

'''generate 4 arrays of size 10:
a- the first one should be empty
b- the second one should be full of 0s
c- the third one should be full of 1s
d- the last one should be full of 2s'''

a=np.empty(shape = 10)
print(a)
b=np.zeros(shape= 10)
print(b)
c = np.ones(shape= 10)
print(c)
d = np.full(shape= 10, fill_value= 2)
print(d)

#to define the shape of a matrix we use
print(b.shape)
#to define the size of a matrix we use
print(c.size)


'''EXERCICE TO DO'''

'''array_1D = np.array([10,11,12,13, 14])

array_2D = np.array([[20,30,40,50,60], [43,54,65,76,87], [11,22,33,44,55]])

array_3D = np.array([[[1,2,3,4,5], [11,21,31,41,51]], [[11,12,13,14,15], [51,52,53,54,5]]])

#Slice the first column of the 2-D array.
first_col= array_2D[ : ,0]
print (first_col)

# slice the first and second of the first column
first_col1= array_2D[ :2, :2]
print(first_col1)

#Slice the last two columns of the 2-nd row of the 2-D array
sec_col_sec_row = array_2D[1,-2:]
print(sec_col_sec_row)


#Slice the 2-nd row of the 2-D array excluding the last two columns
sec_row_exlu = array_2D[1,:-2]
print(sec_row_exlu)'''
print(A[0][0]+A[-1][-1])


