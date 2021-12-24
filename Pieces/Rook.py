#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List


class Rook(Piece):

	def __init__(self, position, colour, image):
		super(Rook, self).__init__(position, colour, image)
		
	def move(self, grid, top):
		valid = self.infinite_move(grid, True, True)
		valid_moves = []

		#collecting horizontal data
		if valid[0] != self.position[0] or valid[1] != self.position[0]:
			for x in range(valid[0], valid[1]+1):
				if x != self.position[0]:
					valid_moves.append([x,self.position[1]])
		


		#collecting vertical data
		if valid[2] != self.position[1] or valid[3] != self.position[1]:
			for x in range(valid[2], valid[3]+1):
				if x != self.position[1]:
					valid_moves.append([self.position[0],x])

		#print(valid_moves)
		return valid_moves

	def move_update(self, position):
		self.position = position
		return



