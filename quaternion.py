#create quaternion class and implement quaternion multiplication
import numpy as np

# Quaternion class

 # Initialize a quaternion a + b*i + c*j + d*k with quaternion(a, b, c, d)

class quaternion():
    
    def __init__(self, a, i, j, k):
        
        self.list_of_numbers = [a, i, j, k]
        self.a = a
        self.i = i
        self.j = j
        self.k = k
        self.string_representation = f'{a} + {i}i + {j}j + {k}k'
    
    #display quaternion in string format
    def print(self):
        print(self.string_representation)

    # Multiply two quaternions, return product quaternion
    def multiply(self, q2):
        
        a = self.a
        b = q2.a
        
        x1 = self.i
        x2 = self.j
        x3 = self.k
        
        y1 = q2.i
        y2 = q2.j
        y3 = q2.k
        
        prod_a = a*b - x1*y1 - x2*y2 - x3*y3
        prod_i = x1*b + a*y1 - x3*y2 + y3*x2
        prod_j = x3*y1 - x1*y3 + a*y2 + x2*b
        prod_k = a*y3 + x3*b - y1*x2 + x1*y2
        
        return quaternion(prod_a, prod_i, prod_j, prod_k)
    
    def inverse(self):
        
        return quaternion(self.a, -self.i, -self.j, -self.k)
        

# 3d rotation operation using quaternion representation
def rotate_vector(vector, angle, axis_of_rot):

    #rotate a vector by a given angle around a given axis using quaternion representation

    rot_angle = angle/2

    #get the quaternion representation of the rotation
    rot_quaternion = quaternion(np.cos(rot_angle), np.sin(rot_angle)*axis_of_rot[0], np.sin(rot_angle)*axis_of_rot[1], np.sin(rot_angle)*axis_of_rot[2])
    
    #get the quaternion representation of the vector to be rotated
    quaternion_rep_orig_vector = quaternion(0, vector[0], vector[1], vector[2])
    
    rotated_vector_quaternion_rep = rot_quaternion.multiply(quaternion_rep_orig_vector.multiply(rot_quaternion.inverse()))
    
    #return the rotated vector 
    return [rotated_vector_quaternion_rep.i, rotated_vector_quaternion_rep.j, rotated_vector_quaternion_rep.k]
