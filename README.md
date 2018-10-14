# matrix-layer-rotation
Hackerrank matrix layer rotation problem

Problem:
You are given a 2D matrix of dimension - m x n - and a positive integer - r -. 
You have to rotate the matrix - r - times and print the resultant matrix. 
Rotation should be in anti-clockwise direction.

Rotation of a  matrix is represented by the following 2 dimension figure. 
Note: - that in one rotation, you have to shift elements by one step only.
      - a matrix can be > 2 dimensions.
       - m = number of rows and n = number of items in each row.      

    a11 < a12 < a13 < a14      |
     v                 ^       |     matrix = [[a11,a12,a13,a14], \
    a21   a22 < a23   a24      |               [a21,a22,a23,a24], \
     v     v     ^     ^       |               [a31,a32,a33,a34], \
    a31   a32 > a33   a34      |               [a41,a42,a43,a44]]
     v                 ^       |
    a41 > a42 > a43 > a44      |

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
