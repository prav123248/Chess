#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List

class Pawn(Piece):
	def __init__(self, position, colour, image, top):
		super(Pawn, self).__init__(position, colour, image)
		self.two_place = True
		self.top = top

	def promotion(self):
		pass

	def move(self, grid, check_mode=False):

		valid_moves = []
		top = self.top
		#when the piece is at the top of the board
		if self.colour == top and top == True: #top being false means white is at the top, true means black at the top of the board
			if self.position[1] == 0:
				return valid_moves
		else:
			if self.position[1] == 7:
				return valid_moves

		if self.colour == top and top == False:   #allows differentiation of who is at the top of the board (rn white)
			if (self.position[1]+1) <= 7 and (self.position[1]+1) >= 0 and grid[self.position[0]][self.position[1]+1].piece == None:	 #makes sure next row exists
				valid_moves.append([self.position[0], self.position[1]+1])
				
				if self.two_place and grid[self.position[0]][self.position[1]+2].piece == None:							#if pawn can move two pieces forward
					valid_moves.append([self.position[0], self.position[1]+2])

					#attack box
			if self.position[0]+1 <= 7 and self.position[1]+1 <= 7:
				pos_right = grid[self.position[0]+1][self.position[1]+1]
				if pos_right.piece and pos_right.piece.colour != self.colour:
					valid_moves.append([self.position[0]+1, self.position[1]+1])

			if self.position[0]-1 >= 0 and self.position[1]+1 <= 7:
				pos_left = grid[self.position[0]-1][self.position[1]+1]
				if pos_left.piece and pos_left.piece.colour != self.colour:
					valid_moves.append([self.position[0]-1, self.position[1]+1])


		else:
			
			if (self.position[1]-1) <= 7 and (self.position[1]-1) >= 0 and grid[self.position[0]][self.position[1]-1].piece == None:	 #makes sure next row exists and no blocking piece
				valid_moves.append([self.position[0], self.position[1]-1])
				
				if self.two_place and grid[self.position[0]][self.position[1]-2].piece == None:							#if pawn can move two pieces forward
					valid_moves.append([self.position[0], self.position[1]-2])

					#attack box
			if self.position[0]+1 <= 7 and self.position[1]-1 >= 0:
				pos_right = grid[self.position[0]+1][self.position[1]-1]
				if pos_right.piece and pos_right.piece.colour != self.colour:
					valid_moves.append([self.position[0]+1, self.position[1]-1])

			if self.position[0]-1 >= 0 and self.position[1]-1 >= 0:
				pos_left = grid[self.position[0]-1][self.position[1]-1]
				if pos_left.piece and pos_left.piece.colour != self.colour:
					valid_moves.append([self.position[0]-1, self.position[1]-1])

		if check_mode:
			initially_valid = valid_moves
			valid_moves = []
			for move in initially_valid:
				if Piece.check_legality(grid, move, self):
					valid_moves.append(move)
		return valid_moves

	def move_update(self, position):
		self.two_place = False	
		self.position = position
		return



