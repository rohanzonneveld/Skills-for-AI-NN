import numpy as np
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

correlation=[[np.dot(A1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A2,A1), np.dot(A2,A2,),np.dot(A2,A3), np.dot(A2,A4,),np.dot(A2,O1), np.dot(A2,O2,),np.dot(A2,O3), np.dot(A2,O4,),np.dot(A2,S1), np.dot(A2,S2,),np.dot(A2,S3), np.dot(A2,S4,)],
            [np.dot(A3,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A4,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(B1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)],
            [np.dot(A1,A1), np.dot(A1,A2,),np.dot(A1,A3), np.dot(A1,A4,),np.dot(A1,O1), np.dot(A1,O2,),np.dot(A1,O3), np.dot(A1,O4,),np.dot(A1,S1), np.dot(A1,S2,),np.dot(A1,S3), np.dot(A1,S4,)]]