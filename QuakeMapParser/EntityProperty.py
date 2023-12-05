class EntityProperty:
	__slots__ = ['propertyName', 'propertyValue']

	def __init__ (self, propertyName= "", propertyValue=""):
		self.propertyName = propertyName
		self.propertyValue = propertyValue
		