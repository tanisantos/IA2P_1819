# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""



class Node():
    def __init__(self, prob, parents = []):
        if len(parents) == 0:
            self.prob = prob[0]   #valor
        else:
            self.prob = prob      #np.array - tabela
        self.parents = parents    #lista
    
    def computeProb(self, evid):
        '''calcula prob condicionada
        evid - tuplo c/ evidencias de tds os nodes da BN
        retorna tuplo com duas prob (False e True)'''
        probTrue = self.prob
        for i in range(len(self.parents)):
            probTrue = probTrue[evid[self.parents[i]]]

        return (1 - probTrue, probTrue)

    
class BN():
    def __init__(self, gra, prob):
        self.gra = gra            #lista de listas com pais do indice
        self.prob = prob          #lista de Nodes

    def computePostProb(self, evid):
        '''não sei
        evid - tuplo c/ evids de tds os nodes da BN
        retorna um valor'''
        pass
               
        return 0
        
        
    def computeJointProb(self, evid): 
        '''calcula prob conjunta
        evid - tuplo c/ evids de tds os nodes da BN
        retorna lista/tuplo com... (am confusion)'''
        prod = 1
        for i in range(len(self.gra)):
            prod *= self.prob[i].computeProb(evid)[evid[i]]

        return prod