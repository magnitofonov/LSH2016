#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import json
from collections import Counter


input_line = sys.stdin.readline()

data = json.loads(input_line)

adults = Counter()
kids = Counter()

num_of_progs = len(data)

for prog in range(num_of_progs):
	for cycle in range(len(data[prog]['dates'])):
		adults[data[prog]['dates'][cycle]['cycle_n']] += 1
		if data[prog]['accepts_underage'] == True:
			kids[data[prog]['dates'][cycle]['cycle_n']] += 1

for i in range(1,5):
	print ('Цикл %s: всего программ: %s, из них школьных: %s.' % (i, adults[i], kids[i]))