import numpy as np

import operations as op


def main(ICOD=1, N = 0,  points=None, coordinate_x=None):
    
    if ICOD == 1:  # Interpolation
        coordinate_y = 0
        for i in range(len(points)):
            numerator = 1
            denominator = 1
            for k in range(len(points)): 
                if i != k :
                    numerator*= (coordinate_x - points[k][0]) # Product of (x - x_k)
                    denominator*= (points[i][0] - points[k][0]) # Product of (x1 - x_k)
            coordinate_y += (numerator/denominator) * points[i][1] # f(x) = Φ1 * (y1) + ... + Φn * (yn) 

        return {"coordinateY": coordinate_y}


    if ICOD == 2: # Regression 

        A = []
        C = []

        sum_ones = 0 
        sum_x = 0
        sum_squarex = 0
        sum_y = 0
        sum_xy = 0
        for i in range(len(points)):
            sum_ones += 1
            sum_x += points[i][0]
            sum_squarex += (points[i][0])**2
            sum_y += (points[i][1])
            sum_xy += (points[i][0]) * (points[i][1])

        A.append([sum_ones, sum_x])
        A.append([sum_x, sum_squarex]) # A is symmetric
        

        C.append(sum_y)
        C.append(sum_xy) 

        B = op.lu(A,C)

        b0 = B[0]
        b1 = B[1]

        coordinate_y = b0 + b1 * coordinate_x
        return {"coordinateY": coordinate_y}




