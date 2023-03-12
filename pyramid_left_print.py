# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:38:32 2023

@author: vijay_p
"""

n=int(input("Enter a number : " )) 
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()	