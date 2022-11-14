# Asssignment 3 Matrix Addition, subtraction, multiplication & Transpose
n_rows= int(input("Number of rows:"))
n_columns = int(input("Number of columns:"))

# ----------------------------------------------------------------------------------
# Define matrix 1
M1 = [ ]
print("Enter the entries row-wise for matrix 1:")
# for user input
for i in range(n_rows):          # A for loop for row entries
    a = [ ]
    for j in range(n_columns):      # A for loop for column entries
         a.append(int(input()))
    M1.append(a)
# To print the matrix
for i in range(n_rows):
    for j in range(n_columns):
        print(M1[i][j], end = "  ")
    print( )     

# -----------------------------------------------------------------------------------
# Define matrix 2
M2 = [ ]
print("Enter the entries row-wise for matrix 2:")
# for user input
for i in range(n_rows):          # A for loop for row entries
    b = [ ]
    for j in range(n_columns):      # A for loop for column entries
        b.append(int(input()))
    M2.append(b)
# To print the matrix
for i in range(n_rows):
    for j in range(n_columns):
        print(M2[i][j], end = "  ")
    print()  

# ------------------------------------------------------------------------------------
# Matrix Addition
M3 = []
print("Addition of above two matrix is:")
for i in range(n_rows):
    c = []
    for j in range(n_columns):
        c.append(M1[i][j] + M2[i][j])
    M3.append(c)    
# To print addition matrix
for i in range(n_rows):
    for j in range(n_columns):
        print(M3[i][j],end="  ")
    print()

# -------------------------------------------------------------------------------------
# Matrix Subtraction
M3 = []
print("Subtraction of above two matrix is:")
for i in range(n_rows):
    d = []
    for j in range(n_columns):
        d.append(M1[i][j] - M2[i][j])
    M3.append(d)    
# To print addition matrix
for i in range(n_rows):
    for j in range(n_columns):
        print(M3[i][j],end="  ")
    print() 

# -------------------------------------------------------------------------------------
# Matrix Multiplication
M3 = []
print("Multiplication of above two matrix is:")
for i in range(n_rows):
    e = []
    for j in range(n_columns):
        e.append(M1[i][j] * M2[i][j])
    M3.append(e)    
# To print addition matrix
for i in range(n_rows):
    for j in range(n_columns):
        print(M3[i][j],end="  ")
    print()    

# --------------------------------------------------------------------------------------
# Transpose of Matrix
# Transpose of matrix M1
print("Transpose of matrix M1 is:")
for i in range(n_rows):
    for j in range(n_columns):
        print(M1[j][i], end = "  ")
    print( ) 

# Transpose of matrix M2
print("Transpose of matrix M2 is:")
for i in range(n_rows):
    for j in range(n_columns):
        print(M2[j][i], end = "  ")
    print( )


