class Entity:
	__slots__ = ['propertyCount', 'mapBrushCount', 'propertySet', 'mapBrushSet', 'bspBrushSet']

	def __init__ (self):
		self.propertyCount = 0
		self.mapBrushCount = 0
		self.propertySet = []
		self.mapBrushSet = []
		self.bspBrushSet = []