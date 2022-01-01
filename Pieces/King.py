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

	def move(self, grid, top):
		valid = []

		#Horizontal movements

		hori_array = [self.position[0]-1,self.position[0]+1]

		for x in range(2):
			hori = hori_array[x]
			if hori >= 0 and hori < 8 and (grid[hori][self.position[1]].piece == None or grid[hori][self.position[1]].piece.colour != self.colour):
				valid.append([hori, self.position[1]])


		#Vertical movements
		verti_array = [self.position[1]-1, self.position[1]+1]

		for x in range(2):
			verti = verti_array[x]
			if verti >= 0 and verti < 8 and (grid[self.position[0]][verti].piece == None or grid[self.position[0]][verti].piece.colour != self.colour):
				valid.append([self.position[0], verti])

		#Diagonal movements
		diagonals = [[self.position[0]+1, self.position[1]+1], [self.position[0]-1, self.position[1]+1], [self.position[0]+1, self.position[1]-1], [self.position[0]-1, self.position[1]-1]]
		for x in range(4):
			horizontal = diagonals[x][0]
			vertical = diagonals[x][1]

			if horizontal >= 0 and horizontal < 8:

				if vertical >= 0 and vertical < 8 and (grid[horizontal][vertical].piece == None or grid[horizontal][vertical].piece.colour != self.colour):
					valid.append([horizontal, vertical])
			

		return valid


