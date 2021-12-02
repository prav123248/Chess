#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from typing import List
from PyQt5.QtCore import Qt
class Piece(object):
	id_count = 0

	def __init__(self, position, colour, image):
		self.pieceID = Piece.id_count
		Piece.id_count += 1
		self.position = position
		self.captured = False
		self.pin = False
		self.colour = colour
		self.image = image.scaledToHeight(480/5.5, Qt.SmoothTransformation)


	def getPosition(self):
		return self.position


	def setPosition(self, aPosition) -> None:
		self.position = aPosition

	def getX(self):
		return (self.position[0])

	def getY(self):
		return (self.position[1])
	
	def getImage(self):
		return self.image


	def getCaptured(self):
		return self.captured


	def setCaptured(self, aCaptured) -> None:
		self.captured = aCaptured


	def getPin(self):
		return self.pin


	def setPin(self, aPin) -> None:
		self.pin = aPin


	def getColour(self):
		return self.colour


	def setColour(self, aColour) -> None:
		self.colour = aColour

	@abstractmethod
	def move(self, grid):
		pass

	def infinite_move(self, grid, horizontal, vertical):

		def consecutive_spaces(grid, position):
			#valid[0] represents leftmost horizontal valid position
			#valid[1] represents rightmost horizontal valid position
			#valid[2] represents leftmost vertical valid position
			#valid[3] represents rightmost vertical valid position

			#set valid position default to current position
			valid = [position[0], position[0], position[0], position[0]]


			if horizontal:
				#checks leftmost valid horizontal position
				for x in range(position[0]-1, -1, -1):
					if grid[x][position[1]]:
						valid[0] = x
					else:
						break
				
				#checks rightmost valid horizotnal position
				for x in range(position[0] + 1, 8):
					if grid[x][position[1]]: #check legality here
						valid[1] = x
					else:
						break
			
			if vertical == None:
				#checks bottommost valid vertical position
				for x in range(position[1], 0, -1):
					if grid[position[0]][x]: # check legality here
						valid[2] = x
					else:
						break

				for x in range(position[1] + 1, 6):
					if grid[position[0]][x]: # check legality here
						valid[3] = x
					else:
						break
				
			print(valid)
			return valid

		valid_moves = []
		if horizontal or vertical:
			valid_moves.extend(consecutive_spaces(grid, self.position))
		else:
			valid_moves = [self.position[0],self.position[0],self.position[1],self.position[1]]

		"""
		if whitediag:
			valid_moves.extend(self.diagw_inf())

		if blackdiag:
			valid_moves.extend(self.diagb_inf())
		"""

		return valid_moves
			
		
		
