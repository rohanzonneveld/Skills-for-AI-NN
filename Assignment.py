import numpy as np
import math

def create_matrix(
        size):  # first we need a function that creates empty matrices of the size we want (np.empty is not readable)
    if int(size) > 0:
        s = 1
        mat = []
        while s <= size:
            mat.append([0.0] * size) #the data type of matrix elements is set on creation, so float instead of int
            s += 1
        mat = np.array(mat)
    return mat

def create_blur_matrix(size):
    blurred_matrix = create_matrix(size)             # create a zeroes matrix of the required size
    if size > 1:
        for i in range(0, blurred_matrix.shape[1]):  # go through all columns of the matrix
            if i == 0:                               # set the edge case for the upper left corner
                blurred_matrix[i,i] = 0.8
                blurred_matrix[1,i] = 0.2
            elif i == (blurred_matrix.shape[1] - 1): # set the edge case for the bottom right corner
                blurred_matrix[i, i] = 0.8
                blurred_matrix[i-1, i] = 0.2
            else:
                blurred_matrix[i,i] = 0.6
                blurred_matrix[i-1,i] = 0.2
                blurred_matrix[i+1,i] = 0.2

        return blurred_matrix

def normalize(matrix):
    len=math.sqrt(np.vdot(matrix,matrix))
    if len == 0:
        len = 1
    return np.multiply((1/len),matrix)


# 1.
# Define three characters from your own name, and draw them in a 5x5 matrix. E.g.if you name is Sieuwert,
# make SIE, or SUT, ... Be unique.

# A, S, O

# 2. 
# Create four variations for each character. Make variation one of each character by redrawing it differently,
# e.g. emphasizing one of the strokes. Variant 2 should be based on slightly blurring the first version. Variant
# 3 should add some noise to a few pixels of the image. Variant four should combine noise and blurring.

blur=create_blur_matrix(5)

A =normalize(
    np.array(
    [[0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1]]))


A1=normalize(
    np.array(
    [[0, 0, 0.5, 0, 0],
    [0, 0.5, 0, 1, 0],
    [0, 0.5, 1, 1, 0],
    [0.5, 0, 0, 0, 1],
    [0.5, 0, 0, 0, 1]]))

A2=normalize(np.matmul(A1,blur))

A3=normalize(
    np.array(
    [[0.05, 0.01, 0.97, 0.02, 0],
    [0.04, 0.99, 0.00, 1.00, 0.01],
    [0.00, 0.99, 0.98, 0.95, 0.04],
    [1.00, 0.02, 0.09, -0.01, 0.94],
    [0.97, 0.03, 0.01, 0.04, 0.99]]))

A4=normalize(np.matmul(A3,blur))

O=normalize(
    np.array(
    [[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1]]))

O1=normalize(
    np.array(
    [[0.5, 1, 1, 1, 1],
[0.5, 0, 0, 0, 0],
[1, 0, 0, 0, 0.5],
[1, 0, 0, 0, 0.5],
[1, 1, 1, 0.5, 1]]))

O2 = normalize(np.matmul(O1,blur))

O3 = normalize(
    np.array(
    [[1, 0.9, 0.8, 0.75, 0.75],
    [0.95, 0.04, 0.01, 0, 0.87],
    [0.89, 0.01, 0, 0.02, 0.93],
    [0.86, 0.10, 0, 0.01, 0.99],
    [0.98, 0.97, 0.84, 0.82, 1]]))

O4 = normalize(np.matmul(O3,blur))

S=normalize(
    np.array(
    [[1, 1, 1, 1, 1],
[1, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0, 0, 0, 0, 1],
[1, 1, 1, 1, 1]]))

S1=normalize(
    np.array(
    [[0.5, 1, 1, 1, 1],
    [0.5, 0, 0, 0, 0],
    [0.5, 1, 1, 1, 1],
    [0, 0, 0, 0, 1],
    [0.5, 1, 1, 1, 1]]))

S2=normalize(np.matmul(S1, blur))

S3=normalize(
    np.array(
    [[0.90, 0.87, 0.88, 0.9, 0.80],
    [0.88, 0.08, 0.1, 0.03, 0.05],
    [0.90, 0.88, 0.92, 1.0, 0.78],
    [0.05, 0.04, 0.03, 0.06, 0.96],
    [0.90, 0.79, 0.88, 0.92, 0.95]]))

S4=normalize(np.matmul(S3, blur))

letters_list = [A,A1,A2,A3,A4,O,O1,O2,O3,O4,S,S1,S2,S3,S4]

# Make a correlation matrix for your inputs (12 x 12 matrix) by taking inproducts between all input values. How similar are your inputs to each other? Explain from the correlation matrix which two characters are
# most likely to be confused.

correlation=[[np.vdot(A1,A1), np.vdot(A1,A2),np.vdot(A1,A3), np.vdot(A1,A4),np.vdot(A1,O1), np.vdot(A1,O2),np.vdot(A1,O3), np.vdot(A1,O4),np.vdot(A1,S1), np.vdot(A1,S2),np.vdot(A1,S3), np.vdot(A1,S4)],
            [np.vdot(A2,A1), np.vdot(A2,A2),np.vdot(A2,A3), np.vdot(A2,A4),np.vdot(A2,O1), np.vdot(A2,O2),np.vdot(A2,O3), np.vdot(A2,O4),np.vdot(A2,S1), np.vdot(A2,S2),np.vdot(A2,S3), np.vdot(A2,S4)],
            [np.vdot(A3,A1), np.vdot(A3,A2),np.vdot(A3,A3), np.vdot(A3,A4),np.vdot(A3,O1), np.vdot(A3,O2),np.vdot(A3,O3), np.vdot(A3,O4),np.vdot(A3,S1), np.vdot(A3,S2),np.vdot(A3,S3), np.vdot(A3,S4)],
            [np.vdot(A4,A1), np.vdot(A4,A2),np.vdot(A4,A3), np.vdot(A4,A4),np.vdot(A4,O1), np.vdot(A4,O2),np.vdot(A4,O3), np.vdot(A4,O4),np.vdot(A4,S1), np.vdot(A4,S2),np.vdot(A4,S3), np.vdot(A4,S4)],
            [np.vdot(O1,A1), np.vdot(O1,A2),np.vdot(O1,A3), np.vdot(O1,A4),np.vdot(O1,O1), np.vdot(O1,O2),np.vdot(O1,O3), np.vdot(O1,O4),np.vdot(O1,S1), np.vdot(O1,S2),np.vdot(O1,S3), np.vdot(O1,S4)],
            [np.vdot(O2,A1), np.vdot(O2,A2),np.vdot(O2,A3), np.vdot(O2,A4),np.vdot(O2,O1), np.vdot(O2,O2),np.vdot(O2,O3), np.vdot(O2,O4),np.vdot(O2,S1), np.vdot(O2,S2),np.vdot(O2,S3), np.vdot(O2,S4)],
            [np.vdot(O3,A1), np.vdot(O3,A2),np.vdot(O3,A3), np.vdot(O3,A4),np.vdot(O3,O1), np.vdot(O3,O2),np.vdot(O3,O3), np.vdot(O3,O4),np.vdot(O3,S1), np.vdot(O3,S2),np.vdot(O3,S3), np.vdot(O3,S4)],
            [np.vdot(O4,A1), np.vdot(O4,A2),np.vdot(O4,A3), np.vdot(O4,A4),np.vdot(O4,O1), np.vdot(O4,O2),np.vdot(O4,O3), np.vdot(O4,O4),np.vdot(O4,S1), np.vdot(O4,S2),np.vdot(O4,S3), np.vdot(O4,S4)],
            [np.vdot(S1,A1), np.vdot(S1,A2),np.vdot(S1,A3), np.vdot(S1,A4),np.vdot(S1,O1), np.vdot(S1,O2),np.vdot(S1,O3), np.vdot(S1,O4),np.vdot(S1,S1), np.vdot(S1,S2),np.vdot(S1,S3), np.vdot(S1,S4)],
            [np.vdot(S2,A1), np.vdot(S2,A2),np.vdot(S2,A3), np.vdot(S2,A4),np.vdot(S2,O1), np.vdot(S2,O2),np.vdot(S2,O3), np.vdot(S2,O4),np.vdot(S2,S1), np.vdot(S2,S2),np.vdot(S2,S3), np.vdot(S2,S4)],
            [np.vdot(S3,A1), np.vdot(S3,A2),np.vdot(S3,A3), np.vdot(S3,A4),np.vdot(S3,O1), np.vdot(S3,O2),np.vdot(S3,O3), np.vdot(S3,O4),np.vdot(S3,S1), np.vdot(S3,S2),np.vdot(S3,S3), np.vdot(S3,S4)],
            [np.vdot(S4,A1), np.vdot(S4,A2),np.vdot(S4,A3), np.vdot(S4,A4),np.vdot(S4,O1), np.vdot(S4,O2),np.vdot(S4,O3), np.vdot(S4,O4),np.vdot(S4,S1), np.vdot(S4,S2),np.vdot(S4,S3), np.vdot(S4,S4)]]

# print(np.around(correlation,2))

# 4.
# Create a matrix NN1 to recognise your three characters. It should work on all variations, so perhaps use
# a combination/average version of the three characters. Make improvements to find best matrix. Try to
# make it so that the matrix gives an equally high output for each input character, to make comparison easy.

def NeuralNetwork(input, letters_list):
    A_NN = create_matrix(5)
    for r in range(5):
        for c in range(5):
            A_NN[r][c] = (A1[r][c] + A2[r][c] + A3[r][c] + A4[r][c])/4

    O_NN = create_matrix(5)
    for r in range(5):
        for c in range(5):
            O_NN[r][c] = (O1[r][c] + O2[r][c] + O3[r][c] + O4[r][c])/4

    S_NN = create_matrix(5)
    for r in range(5):
        for c in range(5):
            S_NN[r][c] = (S1[r][c] + S2[r][c] + S3[r][c] + S4[r][c])/4

    NN = [A_NN, O_NN, S_NN]
    answers_list = ['A','O','S']

    values = []
    for i in range(3):
        values.append(np.vdot(normalize(input),normalize(NN[i])))

    # setting threshold values
    if np.max(values)>0.8:
        if np.diff(np.sort(values)[-2:])>0.05:
            return 'Neural network classified input as {}'.format(answers_list[np.argmax(values)]), values
        else:
            return 'Neural network could not distinguish between A, O or S', values
    else: 
        return "Neural network doesn't recognize input as A, O or S", values


# testing all inputs
# for letter in letters_list:
#     print(NeuralNetwork(letter,letters_list))       

# 5.
# Test your matrix on all your inputs and show the scores, for instance in bar chart. Evaluate the score:
# does thecorrect answer indeed get the highest score? Is the difference between the scores big enough to
# set a simple threshold value?

# Threshold values added to function

# 6.
# Really test your network: make four or more inputs and use NN1 on it. Find multiple inputs (3 or
# more) that are not correctly classified. Check what happens if you input all 1's or all zeros? 
# Try to make an incorrectly classified character by changing only one pixel. Is thsi possible? 
# Can you do it by only changing two pixels? Three pixels?


Mattest1 = normalize(
    np.array(
    [[0.90, 0.87, 0.88, 0.9, 0.80],
    [0.88, 0.08, 0.1, 0.03, 0.05],
    [0.90, 0.88, 0.1, 0.7, 0.78],
    [0.05, 0.04, 0.03, 0.06, 0.96],
    [0.90, 0.79, 0.88, 0.92, 0.95]]))  #<--- This is S3 with two changed cells, one severe one slight (third row, third and fourth column). Output: ('Neural network could not distinguish between A, O or S', [0.5659186487364859, 0.9131970683479114, 0.9598313500490001]) 

Mattest2 = normalize(
    np.array(
    [[0, 0.87, 0.88, 0.9, 0.80],
    [0, 0.86, 0.1, 0.03, 0.05],
    [0, 0.8, 0.1, 1.0, 0.78],
    [0, 0.9, 0.1, 0.06, 0.96],
    [0, 0, 0.88, 0.92, 0.95]])) #<--- Input is a thinner S with left column left blank. Output: Neural network doesn't recognize input as A, O or S. [0.6009294054798037, 0.6608644263153981, 0.7985258312293275]

Mattest3 = normalize(
    np.array(
    [[0, 0, 0, 0, 0],
    [0, 0.92, 0.91, 0.88, 0.87],
    [0, 0.8, 0, 0.02, 0.93],
    [0, 0.93, 0, 0.01, 0.99],
    [0, 0.97, 0.84, 0.82, 1]])) #<--- Input is a smaller O with upper row and left column blank. Output: Neural network doesn't recognize input as A, O or S. -> [0.5481145336160349, 0.49868932552294776, 0.529879858890754]

Mattest4 = normalize(
    np.array(
    [[0.05, 0.92, 0.97, 0.92, 0],
    [0.94, 0.05, 0.00, 0.00, 0.91],
    [0.90, 0.99, 0.98, 0.95, 0.94],
    [1.00, 0.02, 0.09, 0.01, 0.94],
    [0.97, 0.03, 0.01, 0.04, 0.99]])) #<---Input is a bigger A. Output: Neural network doesn't recognize input as A, O or S", [0.7538409387436332, 0.7248278879680994, 0.7820713932357782]

# print(NeuralNetwork(Mattest1,letters_list))
# print(NeuralNetwork(Mattest2,letters_list))
# print(NeuralNetwork(Mattest3,letters_list))
# print(NeuralNetwork(Mattest4,letters_list))
# print(NeuralNetwork(np.ones((5,5)),letters_list))
# print(NeuralNetwork(np.zeros((5,5)),letters_list))

# 7.
# Find multiple inputs (not all zeros) so that NN1 cannot make a decision: it gives exactly equal values 
# for all characters. Is there a method for finding such inputs? Describe how you can create such counterexamples.
Mattest5 = normalize(
    np.array(
    [[0, 0, 0, 0, 1],
    [0, 0, 0, 0.965, 0],
    [0, 0.042, 0, 0, 0.3],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0.0002, 0]])) #<---- Composed by trial and error. Output: "Neural network doesn't recognize input as A, O or S", [0.23789935431077322, 0.23789815898812708, 0.23786327870683213]

## plot
import matplotlib.pyplot as plt

letter_name = ['A1','A2','A3','A4','O1','O2','O3','O4','S1','S2','S3','S4']

for i, letter in letters_list:

    plt.rcParams["figure.figsize"] = [7.5, 3.50]
    plt.rcParams["figure.autolayout"] = True

    fig, ax = plt.subplots()
    ax.matshow(correlation, cmap='YlGn')

    for i in range(5):
        for j in range(5):
            c = np.around(letter[j][i],2)
            ax.text(i, j, str(c), va='center', ha='center')

    plt.show()
    filename = 'letter_{}.png'.format(letter_name[i])
    plt.savefig(filename)

