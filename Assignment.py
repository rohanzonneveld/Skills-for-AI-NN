import numpy as np

# 1.
# Define three characters from your own name, and draw them in a 5x5 matrix. E.g.if you name is Sieuwert,
# make SIE, or SUT, ... Be unique.

# A, S, O

# 2. 
# Create four variations for each character. Make variation one of each character by redrawing it differently,
# e.g. emphasizing one of the strokes. Variant 2 should be based on slightly blurring the first version. Variant
# 3 should add some noise to a few pixels of the image. Variant four should combine noise and blurring.

A1 =[0, 0, 1, 0, 0,
    0, 1, 0, 1, 0,
    0, 1, 1, 1, 0,
    1, 0, 0, 0, 1,
    1, 0, 0, 0, 1]

A2=[]
A3=[]
A4=[]
O1=[]
O2=[]
O3=[]
O4=[]
S1=[]
S2=[]
S3=[]
S4=[]

# 3.
# Make a correlation matrix for your inputs (12 x 12 matrix) by taking inproducts between all input values. How similar are your inputs to each other? Explain from the correlation matrix which two characters are
# most likely to be confused.

correlation=[[np.dot(A1,A1), np.dot(A1,A2),np.dot(A1,A3), np.dot(A1,A4),np.dot(A1,O1), np.dot(A1,O2),np.dot(A1,O3), np.dot(A1,O4),np.dot(A1,S1), np.dot(A1,S2),np.dot(A1,S3), np.dot(A1,S4)],
            [np.dot(A2,A1), np.dot(A2,A2),np.dot(A2,A3), np.dot(A2,A4),np.dot(A2,O1), np.dot(A2,O2),np.dot(A2,O3), np.dot(A2,O4),np.dot(A2,S1), np.dot(A2,S2),np.dot(A2,S3), np.dot(A2,S4)],
            [np.dot(A3,A1), np.dot(A3,A2),np.dot(A3,A3), np.dot(A3,A4),np.dot(A3,O1), np.dot(A3,O2),np.dot(A3,O3), np.dot(A3,O4),np.dot(A3,S1), np.dot(A3,S2),np.dot(A3,S3), np.dot(A3,S4)],
            [np.dot(A4,A1), np.dot(A4,A2),np.dot(A4,A3), np.dot(A4,A4),np.dot(A4,O1), np.dot(A4,O2),np.dot(A4,O3), np.dot(A4,O4),np.dot(A4,S1), np.dot(A4,S2),np.dot(A4,S3), np.dot(A4,S4)],
            [np.dot(O1,A1), np.dot(O1,A2),np.dot(O1,A3), np.dot(O1,A4),np.dot(O1,O1), np.dot(O1,O2),np.dot(O1,O3), np.dot(O1,O4),np.dot(O1,S1), np.dot(O1,S2),np.dot(O1,S3), np.dot(O1,S4)],
            [np.dot(O2,A1), np.dot(O2,A2),np.dot(O2,A3), np.dot(O2,A4),np.dot(O2,O1), np.dot(O2,O2),np.dot(O2,O3), np.dot(O2,O4),np.dot(O2,S1), np.dot(O2,S2),np.dot(O2,S3), np.dot(O2,S4)],
            [np.dot(O3,A1), np.dot(O3,A2),np.dot(O3,A3), np.dot(O3,A4),np.dot(O3,O1), np.dot(O3,O2),np.dot(O3,O3), np.dot(O3,O4),np.dot(O3,S1), np.dot(O3,S2),np.dot(O3,S3), np.dot(O3,S4)],
            [np.dot(O4,A1), np.dot(O4,A2),np.dot(O4,A3), np.dot(O4,A4),np.dot(O4,O1), np.dot(O4,O2),np.dot(O4,O3), np.dot(O4,O4),np.dot(O4,S1), np.dot(O4,S2),np.dot(O4,S3), np.dot(O4,S4)],
            [np.dot(S1,A1), np.dot(S1,A2),np.dot(S1,A3), np.dot(S1,A4),np.dot(S1,O1), np.dot(S1,O2),np.dot(S1,O3), np.dot(S1,O4),np.dot(S1,S1), np.dot(S1,S2),np.dot(S1,S3), np.dot(S1,S4)],
            [np.dot(S2,A1), np.dot(S2,A2),np.dot(S2,A3), np.dot(S2,A4),np.dot(S2,O1), np.dot(S2,O2),np.dot(S2,O3), np.dot(S2,O4),np.dot(S2,S1), np.dot(S2,S2),np.dot(S2,S3), np.dot(S2,S4)],
            [np.dot(S3,A1), np.dot(S3,A2),np.dot(S3,A3), np.dot(S3,A4),np.dot(S3,O1), np.dot(S3,O2),np.dot(S3,O3), np.dot(S3,O4),np.dot(S3,S1), np.dot(S3,S2),np.dot(S3,S3), np.dot(S3,S4)],
            [np.dot(S4,A1), np.dot(S4,A2),np.dot(S4,A3), np.dot(S4,A4),np.dot(S4,O1), np.dot(S4,O2),np.dot(S4,O3), np.dot(S4,O4),np.dot(S4,S1), np.dot(S4,S2),np.dot(S4,S3), np.dot(S4,S4)]]

# print(correlation)

# 4.
# Create a matrix NN1 to recognise your three characters. It should work on all variations, so perhaps use
# a combination/average version of the three characters. Make improvements to find best matrix. Try to
# make it so that the matrix gives an equally high output for each input character, to make comparison easy.

NN1=[]