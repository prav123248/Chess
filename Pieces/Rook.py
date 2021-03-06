#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List


class Rook(Piece):

	def __init__(self, position, colour, image):
		super(Rook, self).__init__(position, colour, image)
		
	def move(self, grid):
		return self.infinite_move(grid, True, True, False)
		
	def move_update(self, position):
		self.position = position
		return



