#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List

class Knight(Piece):
	def __init__(self, position, colour, image):
		super(Knight, self).__init__(position, colour, image)

	def move(self, grid, top):
		valid = []
		possibilities = [[1,2], [-1,2], [1,-2], [-1,-2]]

		for x in range(4):
			horizontal_pos = possibilities[x][0] + self.position[0]
			vertical_pos = possibilities[x][1] + self.position[1]

			horizontal_pos_reverse = possibilities[x][1] + self.position[0]
			vertical_pos_reverse = possibilities[x][0] + self.position[1]




			if horizontal_pos > 0 and horizontal_pos < 8 and vertical_pos > 0 and vertical_pos < 8 and (grid[horizontal_pos][vertical_pos].piece == None or grid[horizontal_pos][vertical_pos].piece.colour != self.colour):
				valid.append([horizontal_pos, vertical_pos])

			if horizontal_pos_reverse > 0 and horizontal_pos_reverse < 8 and vertical_pos_reverse > 0 and vertical_pos_reverse < 8 and (grid[horizontal_pos_reverse][vertical_pos_reverse].piece == None or grid[horizontal_pos_reverse][vertical_pos_reverse].piece.colour != self.colour):
				valid.append([horizontal_pos_reverse, vertical_pos_reverse])
		
		return valid
