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
	def move(self):
		pass

