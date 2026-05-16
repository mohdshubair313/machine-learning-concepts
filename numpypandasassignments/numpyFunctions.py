import numpy as np
import numpy.ma as ma

# =====================================================================
# 🚀 NUMPY MASTER CHEATSHEET & IMPORTANT FUNCTIONS
# =====================================================================
# Ye file ek complete guide hai Numpy ke un sabhi functions ke liye jo 
# assignments aur industry me use hote hain. Har function kya karta hai
# aur kaise use hota hai, yahan detail me examples ke sath diya gaya hai.
# =====================================================================

# ---------------------------------------------------------------------
# 1. ARRAY CREATION FUNCTIONS (Array Banane Ke Tareeke)
# ---------------------------------------------------------------------

# np.array()
# Kya karta hai: Normal Python list/tuple ko Numpy Array me badalta hai.
# Kaise use karein:
my_list = [1, 2, 3, 4]
arr = np.array(my_list)

# np.arange(start, stop, step)
# Kya karta hai: Ek sequence of numbers deta hai (jaise range() hota hai python me).
# Stop value count nahi hoti.
# Kaise use karein:
arr_seq = np.arange(1, 17) # Dega: [1, 2, ..., 16]

# np.random.randint(low, high, size)
# Kya karta hai: Random integers generate karta hai 'low' se 'high' ke beech me.
# 'size' bataata hai ki matrix ka shape kya chahiye. High value include nahi hoti.
# Kaise use karein:
random_arr = np.random.randint(1, 21, size=(5, 5)) # 5x5 matrix banegi with random ints between 1-20

# np.eye(N)
# Kya karta hai: Identity matrix banata hai (Diagonals par 1, baaki sab 0).
# Kaise use karein:
identity_matrix = np.eye(3, dtype=bool) # 3x3 array (True on diagonal, False elsewhere)


# ---------------------------------------------------------------------
# 2. SHAPE & MANIPULATION FUNCTIONS (Array ki Shape Badalna)
# ---------------------------------------------------------------------

# .reshape(shape)
# Kya karta hai: Array ki rows aur columns ko badalta hai, bina data change kiye.
# Total elements same hone chahiye (jaise 16 items ko 4x4 me badalna).
# Kaise use karein:
arr_2d = np.arange(1, 17).reshape((4, 4)) 

# .flatten()
# Kya karta hai: Kisi bhi 2D ya 3D matrix ko pighla kar wapas ek line me (1D array) badal deta hai.
# Kaise use karein:
flat_arr = arr_2d.flatten()

# np.concatenate((arr1, arr2))
# Kya karta hai: Do ya do se zyada arrays ko aapas me jodta hai (join karta hai).
# Kaise use karein:
joined_arr = np.concatenate((np.array([1, 2]), np.array([3, 4]))) # Dega: [1, 2, 3, 4]

# np.fill_diagonal(array, val)
# Kya karta hai: Matrix ke diagonal elements (jaise [0,0], [1,1]) ko seedhe replace karta hai.
# Kaise use karein:
# np.fill_diagonal(arr_2d, 0) # Diagonals par 0 aa jayega


# ---------------------------------------------------------------------
# 3. INDEXING & SLICING (Data Select aur Nikalna)
# ---------------------------------------------------------------------

# Slicing: arr[row_start:row_end, col_start:col_end]
# Kya karta hai: Kisi badi matrix me se ek chota tukda nikalta hai.
# Example: 
sub_array = arr_2d[2:5, 1:4] # Row 2 se 4 tak, aur Col 1 se 3 tak select hoga.

# Fancy Indexing
# Kya karta hai: Random rows/cols ko select karne ke liye lists of index use karte hain.
# Example: (Corners nikalne ke liye)
corners = arr_2d[[0, 0, -1, -1], [0, -1, 0, -1]] # [row_indices_ki_list], [col_indices_ki_list]

# Boolean Indexing (Filtering)
# Kya karta hai: Condition laga kar array ke elements dhoondhta hai aur modify kar sakta hai.
# Example:
arr_2d[arr_2d > 10] = 10 # Jo bhi elements 10 se bade hain, Numpy automatically unhe 10 bana dega.


# ---------------------------------------------------------------------
# 4. MATHEMATICAL & STATISTICAL OPERATIONS (Maths aur Stats)
# ---------------------------------------------------------------------

# np.sum(arr, axis)
# Kya karta hai: Elements ko jodata (add) hai. Axis=0 matlab Column-wise, Axis=1 matlab Row-wise.
# Kaise use karein:
 row_sum = np.sum(arr_2d, axis=1)

# Stats Functions:
# np.mean() -> Average nikalta hai poore array ka.
# np.median() -> Middle value nikalta hai.
# np.std() -> Standard Deviation nikalta hai.
# np.var() -> Variance nikalta hai.

# Broadcasting & np.newaxis
# Kya karta hai: Agar 2 arrays ka shape alag hai (jaise ek 2D aur ek 1D), toh Numpy unhe 
# stretch karke add/sub kar deta hai. 
# np.newaxis ek naya dimension add karta hai taaki arrays ka size match ho sake.
# Example:
# col_array = np.array([1, 2, 3, 4])
# arr_2d - col_array[:, np.newaxis] # 1D array ko 2D column vector banakar subtract karega


# ---------------------------------------------------------------------
# 5. LINEAR ALGEBRA (Matrices ke Advance Calculations)
# ---------------------------------------------------------------------
# Sabhi algebra functions `np.linalg` ke andar aate hain.

# np.linalg.det(matrix)
# Kya karta hai: Matrix ka Determinant value nikalta hai.
# Example:
# det = np.linalg.det(np.array([[1, 2], [3, 4]]))

# np.linalg.inv(matrix)
# Kya karta hai: Matrix ka Inverse nikalta hai (Matrix ^ -1).
# Example:
# inverse = np.linalg.inv(np.array([[1, 2], [3, 4]]))

# np.linalg.eigvals(matrix)
# Kya karta hai: Matrix ke Eigenvalues calculate karta hai.
# Example:
# eigenvalues = np.linalg.eigvals(np.array([[1, 2], [3, 4]]))

# np.dot(array1, array2)
# Kya karta hai: Do matrices ka dot product (Matrix Multiplication) karta hai.
# Example:
# product = np.dot(np.array([[1, 2], [3, 4]]), np.array([[5, 6], [7, 8]]))

# ---------------------------------------------------------------------
# 6. STRUCTURED ARRAYS (Table ya Database jaisa Data)
# ---------------------------------------------------------------------

# Kya karta hai: Ek hi array me alag-alag type (string, integer, float) ka data 
# bilkul kisi Excel table ya SQL database jaisa store karne deta hai.
# Kaise use karein:
data_type = [('name', 'U10'), ('age', 'i4'), ('weight', 'f4')] # U10=String, i4=Integer, f4=Float
data = np.array([('Alice', 25, 55.5), ('Bob', 30, 85.3)], dtype=data_type)

# np.sort(data, order='field_name')
# Kya karta hai: Structured array ko kisi specific column (jaise age) ke hisaab se sort karta hai.
# sorted_data = np.sort(data, order='age')


# ---------------------------------------------------------------------
# 7. MASKED ARRAYS (Data Chupana / Ignore karna)
# ---------------------------------------------------------------------
# Kabhi kabhi hamare paas kharab data hota hai (jaise extreme outliers) jisko 
# delete karne ki jagah hum calculation karte time chupana (mask karna) chahte hain.

# ma.masked_greater(array, value)
# Kya karta hai: Jo elements value se bade hain, unko "mask" (hide) kar deta hai 
# taaki wo calculations (jaise sum/mean) me gin-ne me na aayein.
# Kaise use karein:
# masked_arr = ma.masked_greater(arr_2d, 10)

# ma.masked_array(array, mask)
# Kya karta hai: Ek custom mask lagata hai. Jaise mask=np.eye(3) dene par diagonals hide ho jayenge.
# Kaise use karein:
# custom_masked = ma.masked_array(arr_2d, mask=np.eye(4, dtype=bool))

# .filled(fill_value)
# Kya karta hai: Jo items mask kiye gaye the (chupe the), unko bahar lakar 'fill_value' se replace karta hai.
# Kaise use karein:
# final_arr = custom_masked.filled(0) # Chhipe hue sabhi elements ab 0 ban jayenge
