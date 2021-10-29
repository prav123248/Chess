#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List

class Pawn(Piece):
	def __init__(self, position, colour, image):
		super(Pawn, self).__init__(position, colour, image)
		

	def promotion(self):
		pass

	def move(self):
		
		return [[2,4],[4,7],[3,6]]

