#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 17:53:12 2021

@author: arantt3
"""

from logic import *

rain = Symbol("rain")
hagrid = Symbol("hagrid")
dumbledore = Symbol("dumbledore")


#sentence = And(rain, hagrid)
#print (sentence.formula())
#print(rain.symbols())

#sentence = Not(rain)

#sentence2 = And(rain, hagrid)

#print (sentence.formula())
#print (sentence2.formula())

knowledge = And( Implication(Not(rain),hagrid), Or(hagrid,dumbledore), Not(And(hagrid,dumbledore)), dumbledore)

#sentence = And( Implication( Not(rain) , hagrid), dumbledore)

#sentence = Implication( Not(rain) , hagrid)

#sentence1 = Or(rain, rain)

#form1 = sentence1.formula()

#sentence2 = And(rain, sentence1)
               

print (knowledge.formula())

print( model_check(knowledge, rain) ) #saying when knowledge is true what is rain and in that world when knowledge is true, rain is true

