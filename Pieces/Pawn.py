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

	def move(self, grid, top):

		valid_moves = []

		#when the piece is at the top of the board
		if self.colour == top: #top being false means white is at the top, true means black at the top of the board
			if self.position[1] == 0:
				return valid_moves
		else:
			if self.position[1] == 7:
				return valid_moves

		if self.colour == top:   #allows differentiation of who is at the top of the board
			if (self.position[1]+1) <= 7 and (self.position[1]+1) >= 0:	 #makes sure next row exists
				 valid_moves.append([self.position[0], self.position[1]-1])

			if self.two_place:							#if pawn can move two pieces forward
				valid_moves.append([self.position[0], self.position[1]+2])

					#attack box
			if self.position[0]+1 <= 7 and self.position[1]+1 <= 7:
				if grid[self.position[0]+1][self.position[1]+1].piece and grid[self.position[0]+1][self.position[1]+1].piece.colour != self.colour:
					valid_moves.append([self.position[0]+1, self.position[1]+1])

			if self.position[0]-1 >= 0 and self.position[1]+1 <= 7:
				if grid[self.position[0]-1][self.position[1]+1].piece and grid[self.position[0]+1][self.position[1]+1].piece.colour != self.colour:
					valid_moves.append([self.position[0]+1, self.position[1]+1])
				

		else:
			if (self.position[1]-1) <= 7 and (self.position[1]-1) >= 0:	 #makes sure next row exists
				 valid_moves.append([self.position[0], self.position[1]-1])
			

			if self.two_place:							#if pawn can move two pieces forward
				valid_moves.append([self.position[0], self.position[1]-2])

					#attack box
			if self.position[0]-1 <= 7 and self.position[1]-1 <= 7:
				if grid[self.position[0]-1][self.position[1]-1].piece and grid[self.position[0]-1][self.position[1]-1].piece.colour != self.colour:
					valid_moves.append([self.position[0]-1, self.position[1]-1])

			if self.position[0]+1 >= 0 and self.position[1]-1 <= 7:
				if grid[self.position[0]+1][self.position[1]-1].piece and grid[self.position[0]-1][self.position[1]-1].piece.colour != self.colour:
					valid_moves.append([self.position[0]+1, self.position[1]-1])
		return valid_moves
