# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 15:51:49 2018

@author: mlopes
"""

import itertools

class Node():
    def __init__(self, prob, parents = []):
        if len(parents) == 0:
            self.prob = prob[0]   #valor
        else:
            self.prob = prob      #np.array - tabela
        self.parents = parents    #lista
    
    def computeProb(self, evid):
        probTrue = self.prob
        for i in range(len(self.parents)):
            probTrue = probTrue[evid[self.parents[i]]]
        return (1 - probTrue, probTrue)


class BN():
    def __init__(self, gra, prob):
        self.gra = gra            #lista de listas com pais do indice
        self.prob = prob          #lista de Nodes

    def computePostProb(self, evid):
        trueJointProb  = self.computeUnknownJointProb(evid[:evid.index(-1)] + (1,) + evid[evid.index(-1) + 1:])
        falseJointProb = self.computeUnknownJointProb(evid[:evid.index(-1)] + (0,) + evid[evid.index(-1) + 1:])
        return trueJointProb / (trueJointProb + falseJointProb)

    def computeUnknownJointProb(self, evid):
        sum = 0
        for v in itertools.product((0,1), repeat = evid.count([])):
            sum += self.computeJointProb(self.substituteUnknowns(evid, v))
        return sum

    def substituteUnknowns(self, evid, subs):
        for i in range(len(subs)):
            evid = evid[:evid.index([])] + (subs[i],) + evid[evid.index([]) + 1:]
        return evid

    def computeJointProb(self, evid): 
        prod = 1
        for i in range(len(self.gra)):
            prod *= self.prob[i].computeProb(evid)[evid[i]]
        return prod