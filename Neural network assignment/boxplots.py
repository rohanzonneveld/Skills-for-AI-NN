import numpy as np
import math
import matplotlib.pyplot as plt

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

print(np.around(correlation,2))

# 4.
# Create a matrix NN1 to recognise your three characters. It should work on all variations, so perhaps use
# a combination/average version of the three characters. Make improvements to find best matrix. Try to
# make it so that the matrix gives an equally high output for each input character, to make comparison easy.

# NN1=create_matrix(5)
# for r in range(5):
#     for c in range (5):
#         NN1[r][c]=(A1[r][c]+A2[r][c]+A3[r][c]+A4[r][c]+O1[r][c]+O2[r][c]+O3[r][c]+O4[r][c]+S1[r][c]+S2[r][c]+S3[r][c]+S4[r][c])/12

O_NN = create_matrix(5)
for r in range(5):
    for c in range(5):
        O_NN[r][c] = (O1[r][c] + O2[r][c] + O3[r][c] + O4[r][c])/4

S_NN = create_matrix(5)
for r in range(5):
    for c in range(5):
        S_NN[r][c] = (S1[r][c] + S2[r][c] + S3[r][c] + S4[r][c])/4

A_NN = create_matrix(5)
for r in range(5):
    for c in range(5):
        A_NN[r][c] = (A1[r][c] + A2[r][c] + A3[r][c] + A4[r][c])/4

NN2 = [ A_NN, O_NN, S_NN]
answers_list = ['A','O','S']

values = []
for letter in letters_list:
    max = 0
    for i in range(3):
        value = np.vdot(normalize(letter),normalize(NN2[i]))
        values.append(value)
        if value > max:
            max = value
            idx = i
    print('Deze letter is een: ' + answers_list[idx])

# Make bar chart for A-inputs
variants = ['Original', 'Small changes', 'blurred', 'Noise', 'Blur and noise']
A_values_input_A = [values[0], values[3],values[6],values[9],values[12]]
O_values_input_A = [values[1], values[4],values[7],values[10],values[13]]
S_values_input_A = [values[2], values[5],values[8],values[11],values[14]]

x_axis = np.arange(len(variants))

plt.bar(x_axis -0.2, A_values_input_A, width=0.2, label = 'A')
plt.bar(x_axis +0.0, O_values_input_A, width=0.2, label = 'O')
plt.bar(x_axis + 0.2, S_values_input_A, width =0.2, label = 'S')

plt.xticks(x_axis, variants)
plt.xlabel('Input variant of A')
plt.ylabel('Normalised correlation []')
plt.title('Correlation between A-inputs and all neurons')
plt.legend()
# plt.savefig('C:/Users/Beheer/Documents/Studie/Artificial Intelligence/Skills for AI/Neural Network project/A_inputs.jpg')
plt.show()



# Make bar chart for O-inputs
A_values_input_O = [values[15], values[18],values[21],values[24],values[27]]
O_values_input_O = [values[16], values[19],values[22],values[25],values[28]]
S_values_input_O = [values[17], values[20],values[23],values[26],values[29]]

x_axis = np.arange(len(variants))

plt.bar(x_axis -0.2, A_values_input_O, width=0.2, label = 'A')
plt.bar(x_axis +0.0, O_values_input_O, width=0.2, label = 'O')
plt.bar(x_axis + 0.2, S_values_input_O, width =0.2, label = 'S')

plt.xticks(x_axis, variants)
plt.xlabel('Input variant of O')
plt.ylabel('Normalised correlation []')
plt.title('Correlation between O-inputs and all neurons')
plt.legend()
# plt.savefig('C:/Users/Beheer/Documents/Studie/Artificial Intelligence/Skills for AI/Neural Network project/O_inputs.jpg')
plt.show()



# Make bar charts for S-inputs
A_values_input_S = [values[30], values[33],values[36],values[39],values[42]]
O_values_input_S = [values[31], values[34],values[37],values[40],values[43]]
S_values_input_S = [values[32], values[35],values[38],values[41],values[44]]

x_axis = np.arange(len(variants))

plt.bar(x_axis -0.2, A_values_input_S, width=0.2, label = 'A')
plt.bar(x_axis +0.0, O_values_input_S, width=0.2, label = 'O')
plt.bar(x_axis + 0.2, S_values_input_S, width =0.2, label = 'S')

plt.xticks(x_axis, variants)
plt.xlabel('Input variant of S')
plt.ylabel('Normalised correlation []')
plt.title('Correlation between S-inputs and all neurons')
plt.legend()
# plt.savefig('C:/Users/Beheer/Documents/Studie/Artificial Intelligence/Skills for AI/Neural Network project/S_inputs.jpg')
plt.show()