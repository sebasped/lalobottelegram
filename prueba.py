#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:15:24 2019

@author: sebas
"""

from datetime import date
from dateutil.relativedelta import relativedelta

now = date.today()
birthdate = date(2018, 1, 1)
rdelta = relativedelta(now, birthdate)
print('Soy Lalo y tengo', rdelta.years,'año y',rdelta.months,'meses')
#print 'Age in days - ', rdelta.days

bla = 'Soy Lalo y tengo '+str(rdelta.years)+' año, '+str(rdelta.months)+' meses y '+str(rdelta.days)+u' días'
print(str(bla))