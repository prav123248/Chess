#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List


class Bishop(Piece):

	def __init__(self, position, colour, image):
		super(Bishop, self).__init__(position, colour, image)


	def move(self, grid):
		return self.infinite_move(grid, False, False, True)

	def move_update(self, position):
		self.position = position
		return

