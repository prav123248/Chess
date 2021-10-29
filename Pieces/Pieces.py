#!/usr/bin/python
# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod
from typing import List

class Piece(object):
	id_count = 0
	__metaclass__ = ABCMeta
	@classmethod
	def __init__(self, position, colour, image):
		self.pieceID = Piece.id_count
		Piece.id_count += 1
		self.position = position
		self.captured = False
		self.pin = False
		self.colour = colour
		self.image = image

	@classmethod
	def getPosition(self):
		return self.position

	@classmethod
	def setPosition(self, aPosition) -> None:
		self.position = aPosition

	@classmethod
	def getCaptured(self):
		return self.captured

	@classmethod
	def setCaptured(self, aCaptured) -> None:
		self.captured = aCaptured

	@classmethod
	def getPin(self):
		return self.pin

	@classmethod
	def setPin(self, aPin) -> None:
		self.pin = aPin

	@classmethod
	def getColour(self):
		return self.colour

	@classmethod
	def setColour(self, aColour) -> None:
		self.colour = aColour

	@abstractmethod
	def move(self):
		pass

