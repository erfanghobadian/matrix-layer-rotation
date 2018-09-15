#########################################################################################
#
# def main(): and def createMatrix(): will not be used when submitting code to Hackerrank
#
#########################################################################################
#
# Problem:
# You are given a 2D matrix of dimension - m x n - and a positive integer - r -. 
# You have to rotate the matrix - r - times and print the resultant matrix. 
# Rotation should be in anti-clockwise direction.
#
# Rotation of a  matrix is represented by the following 2 dimension figure. 
#   Note: - that in one rotation, you have to shift elements by one step only.
#         - a matrix can be > 2 dimensions.
#         - m = number of rows and n = number of items in each row.      
#
#    a11 < a12 < a13 < a14      |
#     v                 ^       |     matrix = [[a11,a12,a13,a14], \
#    a21   a22 < a23   a24      |               [a21,a22,a23,a24], \
#     v     v     ^     ^       |               [a31,a32,a33,a34], \
#    a31   a32 > a33   a34      |               [a41,a42,a43,a44]]
#     v                 ^       |
#    a41 > a42 > a43 > a44      |
#
#########################################################################################
#
# As an example, rotate the Start matrix by 2:
#
#   start    --> 1 rotation --> 2 rotations
#
#  a b c d        b c d e         c d e f
#  l 1 2 e        a 2 3 f         b 3 4 g
#  k 4 3 f        l 1 4 g         a 2 1 h
#  j i h g        k j i h         l k j i
#
#########################################################################################

def createMatrix(M,N):

    # this function is called so the user does not have to provide 
    # the matrix input (items for each row) and it helps when testing.
    #
    # this will not be used when submitting code to Hackerrank

    matrix = [[] for _ in range(M)]

    # populate the matrix with '-'
    for i in range(M):
        for j in range(N):
            matrix[i].extend(['-'])

    # assign left, right, top, bottom indexes of the matrix
    l_index, r_index, t_index, b_index = matrixIndexes(M, N)

    start_value = 0
    while l_index < r_index and t_index < b_index:

        value = start_value * 100 + 1

        for i in range(l_index, r_index):  # move right ->
            matrix[t_index][i] = value
            value += 1

        for j in range(t_index, b_index):  # move down v
            matrix[j][r_index] = value
            value += 1

        for i in range(r_index, l_index, -1):  # move left <-
            matrix[b_index][i] = value
            value += 1

        for j in range(b_index, t_index, -1): # move up ^
            matrix[j][l_index] = value
            value += 1

        l_index += 1
        r_index -= 1
        t_index += 1
        b_index -= 1
        start_value += 1

    return matrix

def matrixIndexes(M, N):

    l_index = 0
    r_index = N-1
    t_index = 0
    b_index = M-1

    return l_index, r_index, t_index, b_index

def populateTemp(temp_m, M, N):

    # assign left, right, top, bottom indexes of the matrix
    l_index, r_index, t_index, b_index = matrixIndexes(M, N)

    index = -1

    # populate temp_m with value '-'.
    # This is done to represent all dimensions and indexes of the matrix.
    while l_index < r_index and t_index < b_index:
        index += 1

        for _ in range(l_index, r_index): # right
            temp_m[index].append('-')
        for _ in range(t_index, b_index): # down
            temp_m[index].append('-')
        for _ in range(r_index, l_index, -1): # left
            temp_m[index].append('-')
        for _ in range(b_index, t_index, -1): # up
            temp_m[index].append('-')

        l_index += 1
        r_index -= 1
        t_index += 1
        b_index -= 1

    return temp_m

def newTempIndex(l, i, R):

    # rotate left R times
    # return the index to be assigned the value

    if R == l:
        return i

    elif R < l:
        return i - R

    else: # R > l
        return i - (R % l)

def matrixRotation(matrix, r):

    M = len(matrix) # number of list in matrix
    N = len(matrix[0]) # number of items in each list of matrix
    R = r # number of rotations

    ###################################################################
    # EXTRACT and ROTATE while assigning to temp_m list
    ###################################################################

    dimension = min(M,N) // 2 # number of lists in temp_m list
    temp_m = [[] for _ in range(dimension)] # used for extraction from matrix
    
    # call populateTemp - each list in temp_m will be populated with '-'
    temp_m = populateTemp(temp_m, M, N)

    # assign left, right, top, bottom indexes of the matrix
    l_index, r_index, t_index, b_index = matrixIndexes(M, N)

    index = -1
    temp_index = 0

    # extract and rotate
    while l_index < r_index and t_index < b_index:
        index += 1
        length = len(temp_m[index])

        for i in range(l_index, r_index): # move right 
            temp_m[index][newTempIndex(length, temp_index, R)] = matrix[t_index][i]
            temp_index += 1

        for j in range(t_index, b_index): # move down
            temp_m[index][newTempIndex(length, temp_index, R)] = matrix[j][r_index]
            temp_index += 1

        for i in range(r_index, l_index, -1): # move left
            temp_m[index][newTempIndex(length, temp_index, R)] = matrix[b_index][i]
            temp_index += 1

        for j in range(b_index, t_index, -1): # move up
            temp_m[index][newTempIndex(length, temp_index, R)] = matrix[j][l_index]
            temp_index += 1

        temp_index = 0
        l_index += 1
        r_index -= 1
        t_index += 1
        b_index -= 1

    ###################################################################
    # ASSIGN each dimension of the matrix with rotated list
    ###################################################################    

    # assign left, right, top, bottom indexes of the matrix
    l_index, r_index, t_index, b_index = matrixIndexes(M, N)

    index = -1

    while l_index < r_index and t_index < b_index:

        index += 1

        for i in range(l_index, r_index): # move right
            matrix[t_index][i] = temp_m[index].pop(0)
        for j in range(t_index, b_index): # move down
            matrix[j][r_index] = temp_m[index].pop(0)
        for i in range(r_index, l_index, -1): # move left
            matrix[b_index][i] = temp_m[index].pop(0)
        for j in range(b_index, t_index, -1): # move up
            matrix[j][l_index] = temp_m[index].pop(0)

        l_index += 1
        r_index -= 1
        t_index += 1
        b_index -= 1

    # print each row of matrix as a string
    for row in matrix:
        print(" ".join(map(str,row)))

def main():

    # main(): will not be used when submitting code to Hackerrank

    # Hackerrank Test Cases - All Pass  
    #                                     
    # -------  M - N -- R -----+--------- M --- N -------- R ----+-------- M - N - R  ---#
    #  TC-0:   4   4    1      |  TC-5:  do not have data        | TC-10:  4   4   2     #
    #  TC-1:  10   8   40      |  TC-6:  210   202        7865   | TC-11:  5   4   7     #
    #  TC-2:  20  35   20      |  TC-7:  136   240      212131   | TC-12:  2   2   3     #
    #  TC-3:  50  75  100      |  TC-8:  250   289    42971434   |                       #
    #  TC-4:  do not have data |  TC-9:  300   300   999999999   |                       #
    # -------------------------+---------------------------------+-----------------------#

    print('\n')
    print("Provide 3 integers as input - number_of_rows  items_in_row  number_of_rotations")

    M,N,R = map(int, input().split())

    matrix = createMatrix(M, N)

    # print each row of matrix as a string to compare start matrix with final rotated matrix.
    print('\n')
    print("Start matrix {}".format('\n'))
    for row in matrix:
        print(" ".join(map(str,row)))
    print('\n')

    matrixRotation(matrix, R)

if __name__ == '__main__':
    main()