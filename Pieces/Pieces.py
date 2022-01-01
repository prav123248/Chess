#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from typing import List
from PyQt5.QtCore import Qt
class Piece(object):
	id_count = 0
	all_pieces = []
	black_pieces = []
	white_pieces = []
	check_mate = "White"

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
	def move(self, grid, check_mode=False):
		pass

	def infinite_move(self, grid, horizontal, vertical, diag, check_mode = False):

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

		
		if check_mode:
			initially_valid = valid_moves
			valid_moves = []
			for move in initially_valid:
				if Piece.check_legality(grid, move, self):
					valid_moves.append(move)

		return valid_moves

	def move_update(self, position):
		self.position = position
		return

	#Checks if a piece is pinned against their own king so can't move
	def legality(self, grid):
				
		if self.colour == True:
			king = Piece.black_pieces[len(Piece.black_pieces)-1]
		else:
			king = Piece.white_pieces[len(Piece.white_pieces)-1]
		
		grid[self.position[0]][self.position[1]].piece = None

		if king.check(grid):
			grid[self.position[0]][self.position[1]].piece = self
			return False
		else:
			grid[self.position[0]][self.position[1]].piece = self
			return True
	
	#Check if a move can be made during King's check
	def check_legality(grid, position, piece):

		if piece.colour == True:
			enemies = Piece.white_pieces
			king = Piece.black_pieces[len(Piece.black_pieces)-1]
		else:
			enemies = Piece.black_pieces
			king = Piece.white_pieces[len(Piece.white_pieces)-1]

		grid[piece.position[0]][piece.position[1]].piece = None
		temp = grid[position[0]][position[1]]
		grid[position[0]][position[1]].piece = piece

		if king.check():
			grid[position[0]][position[1]].piece = temp
			grid[piece.position[0]][piece.position[1]].piece = piece
			return False
		else:
			grid[position[0]][position[1]].piece = temp
			grid[piece.position[0]][piece.position[1]].piece = piece
			return True
