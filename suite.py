# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#TP1 : 
    
#Fonction Factorielle Récursive 

def factorielle(valeur):
    if valeur == 0:
        return 1
    else:
         return valeur * factorielle(valeur - 1);
     
#Fonction Factorielle en Boucle for
def factorielle(n):
      F = 1
      for k in range(2,n+1):
         F = F * k
      return F
  
# Suite

def suite():
    n = 0
    u = 0
    while u > 7:
        n = n+1
        u = #La suite en num.
    return n