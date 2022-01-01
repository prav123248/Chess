#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Pieces import Piece
from typing import List

class Queen(Piece):
	def __init__(self, position, colour, image):
		super(Queen, self).__init__(position, colour, image)
		
	def move(self, grid, top):
		return self.infinite_move(grid, True, True, True)

