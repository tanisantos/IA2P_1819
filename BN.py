# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        self.prob = prob          #np.array len(prob)==len(parents)
        self.parents = parents    #lista
    
    def computeProb(self, evid):
    ''' calculo prob condicionada
        evid - tuplo c/ probs de tds os nodes da BN
        retorna tuplo(?) com duas prob (False e True)'''
        pass

        return 0
    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra            #lista de listas com pais do indice
        self.prob = prob          #lista de Nodes

    def computePostProb(self, evid):
    ''' não sei
        evid - tuplo c/ probs de tds os nodes da BN
        retorna um valor'''
        pass
               
        return 0
        
        
    def computeJointProb(self, evid): 
    ''' calcula prob conjunta (tabela)
        evid - tuplo c/ probs de tds os nodes da BN
        retorna lista/tuplo com... (am confusion)'''
        pass
        
        return 0