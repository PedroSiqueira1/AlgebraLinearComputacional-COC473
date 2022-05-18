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

        return coordinate_y


    if ICOD == 2: # Regression 
 
        return False



print(main(ICOD = 1, points=[[-2,-27],[0,1],[1,0]], coordinate_x=2))
