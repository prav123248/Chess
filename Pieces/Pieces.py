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
	def move(self, grid, top):
		pass

	def infinite_move(self, grid, horizontal, vertical, diag):

		def consecutive_spaces(grid, position):
			#valid[0] represents leftmost horizontal valid position
			#valid[1] represents rightmost horizontal valid position
			#valid[2] represents leftmost vertical valid position
			#valid[3] represents rightmost vertical valid position
			#valid[4] represents multiple of diagonal top left valid position
			#valid[5] represents multiple of diagonal top right valid position
			#valid[6] represents multiple of diagonal bottom left valid position
			#valid[7] represents multiple of diagonal bottom right valid position

			#set valid position default to current position
			#valid = [position[0], position[0], position[1], position[1], 0, 0, 0, 0]

			valid = []

			if horizontal:
				#checks leftmost valid horizontal position
				for x in range(position[0]-1, -1, -1):
					if grid[x][position[1]] and grid[x][position[1]].piece == None:
						valid.append([x, position[1]])
					elif grid[x][position[1]] and grid[x][position[1]].piece.colour != self.colour:
						valid.append([x, position[1]])
						break
					else:
						break
				
				#checks rightmost valid horizotnal position
				for x in range(position[0] + 1, 8):
					if grid[x][position[1]] and grid[x][position[1]].piece == None:
						valid.append([x, position[1]])
					elif grid[x][position[1]] and grid[x][position[1]].piece.colour != self.colour:
						valid.append([x, position[1]])
						break
					else:
						break
			
			if vertical:
				#checks bottommost valid vertical position
				for x in range(position[1]-1, -1, -1):
					if grid[position[0]][x] and grid[position[0]][x].piece == None:
						valid.append([position[0], x])
					elif grid[position[0]][x] and grid[position[0]][x].piece.colour != self.colour:
						valid.append([position[0], x])
						break
					else:
						break

				for x in range(position[1]+1, 8):
					if grid[position[0]][x] and grid[position[0]][x].piece == None:
						valid.append([position[0], x])
					elif grid[position[0]][x] and grid[position[0]][x].piece.colour != self.colour:
						valid.append([position[0], x])
						break
					else:
						break


			if diag:
			
				#calculating top left furthest valid position
				for x in range(1,8):
					if (position[0]-x) < 0 or (position[0]-x) > 7 or (position[1]-x) < 0 or (position[1]-x) > 7:
						break

					if grid[position[0]-x][position[1]-x] and grid[position[0]-x][position[1]-x].piece == None:
						valid.append([position[0]-x, position[1]-x])
					elif grid[position[0]-x][position[1]-x] and grid[position[0]-x][position[1]-x].piece.colour != self.colour:
						valid.append([position[0]-x, position[1]-x])
						break
					else:
						break

				#calculating top right furthest valid position
				for x in range(1,8):
					if (position[0]-x) < 0 or (position[0]-x) > 7 or (position[1]+x) < 0 or (position[1]+x) > 7:
						break

					if grid[position[0]-x][position[1]+x] and grid[position[0]-x][position[1]+x].piece == None:
						valid.append([position[0]-x, position[1]+x])
					elif grid[position[0]-x][position[1]+x] and grid[position[0]-x][position[1]+x].piece.colour != self.colour:
						valid.append([position[0]-x, position[1]+x])
						break
					else:
						break

				#calculating bottom left furthest valid position
				for x in range(1,8):
					if (position[0]+x) < 0 or (position[0]+x) > 7 or (position[1]-x) < 0 or (position[1]-x) > 7:
						break

					if grid[position[0]+x][position[1]-x] and grid[position[0]+x][position[1]-x].piece == None:
						valid.append([position[0]+x, position[1]-x])
					elif grid[position[0]+x][position[1]-x] and grid[position[0]+x][position[1]-x].piece.colour != self.colour:
						valid.append([position[0]+x, position[1]-x])
						break
					else:
						break

				#calculating bottom right furthest valid position
				for x in range(1,8):
					if (position[0]+x) < 0 or (position[0]+x) > 7 or (position[1]+x) < 0 or (position[1]+x) > 7:
						break

					if grid[position[0]+x][position[1]+x] and grid[position[0]+x][position[1]+x].piece == None:
						valid.append([position[0]+x, position[1]+x])
					elif grid[position[0]+x][position[1]+x] and grid[position[0]+x][position[1]+x].piece.colour != self.colour:
						valid.append([position[0]+x, position[1]+x])
						break
					else:
						break
			
			return valid



		valid_moves = []
		if horizontal or vertical or diag:
			valid_moves.extend(consecutive_spaces(grid, self.position))
	
		return valid_moves

	def move_update(self, position):
		self.position = position
		return
			
		
		
