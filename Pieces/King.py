#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List

class King(Piece):

	def __init__(self, position, colour, image):
		super(King, self).__init__(position, colour, image)
		self.check = False
		self.castling_potential = False
		
	def getCheck(self):
		return self.check

	def setCheck(self, aCheck) -> None:
		self.check = aCheck

	def castling(self):
		pass

	def move(self):
		pass


