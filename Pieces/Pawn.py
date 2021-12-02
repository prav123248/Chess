#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List

class Pawn(Piece):
	def __init__(self, position, colour, image):
		super(Pawn, self).__init__(position, colour, image)
		self.two_place = True

	def promotion(self):
		pass

	def move(self, grid):

		valid_moves = []

		limit = 0
		if self.colour:
			limit = 0
		else:
			limit = 7

		if self.position[1] == limit:
			return valid_moves

		if grid[self.position[1]+1]: #check legality
			valid_moves.append([self.position[0], self.position[1]+1])
			if self.two_place:
				valid_moves.append([self.position[0], self.position[1]+2])

		#attack box
		if self.position[0]+1 <= 7 and self.position[1]+1 <= 7:
			if grid[self.position[0]+1][self.position[1]+1].piece and grid[self.position[0]+1][self.position[1]+1].piece.colour != self.colour:
				valid_moves.append([self.position[0]+1, self.position[1]+1])

		if self.position[0]-1 >= 0 and self.position[1]+1 <= 7:
			if grid[self.position[0]-1][self.position[1]+1].piece and grid[self.position[0]+1][self.position[1]+1].piece.colour != self.colour:
				valid_moves.append([self.position[0]+1, self.position[1]+1])
		print(self.position, valid_moves)
		return valid_moves
