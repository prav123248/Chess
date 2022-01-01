#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List

class King(Piece):

	def __init__(self, position, colour, image):
		super(King, self).__init__(position, colour, image)
		self.check_att = False
		self.castling_potential = False
		
	def getCheck(self):
		return self.check

	def check(self, grid, setCheck=False):
		if self.colour:
			enemies = Piece.white_pieces
		else:
			enemies = Piece.black_pieces

		for enemy in enemies:
			if self.position in enemy.move(grid):
				if setCheck:
					self.check_state = True
					return True
				else:
					return True
		if setCheck:
			self.check_state = False
		return False
		

	def castling(self):
		pass

	def move(self, grid, check_mode=False):
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
			

		if check_mode:
			initially_valid = valid
			valid = []
			for move in initially_valid:
				if Piece.check_legality(grid, move, self):
					valid.append(move)

		return valid

	def check_state(grid, colour):

		if colour == True:
			king = Piece.black_pieces[len(Piece.black_pieces)-1] 
			pieces = Piece.black_pieces
			enemy = Piece.white_pieces
			winner = "Black"
		else:
			king = Piece.white_pieces[len(Piece.white_pieces)-1] 
			pieces = Piece.white_pieces
			enemy = Piece.black_pieces
			winner = "White"
		king.check(grid, True)

		if king.check_state:
			#Check if moves currently exist for checked player
			for piece in pieces:
				for move in piece.move(grid):
					temp = grid[move[0]][move[1]].piece
					grid[move[0]][move[1]].piece = piece
					if king.check(grid) == False:
						return True
					grid[move[0]][move[1]].piece = temp
			
			#Check if this is a stalemate
			for piece in enemy:
				if king.position in piece.move(grid):
					Piece.check_mate = winner
					return True
			Piece.check_mate = "Stalemate"

			return True
		else:
			return False		
