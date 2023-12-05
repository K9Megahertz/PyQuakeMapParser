class MapBrushFace:
	__slots__ = ['plane', 'texname', 'texoffsetu', 'texoffsetv', 'texangle', 'uscale', 'vscale']



	def __init__ (self, plane, texname, texoffsetu, texoffsetv, texangle, uscale, vscale):
		self.plane = plane
		self.texname = texname
		self.texoffsetu = texoffsetu
		self.texoffsetv = texoffsetv
		self.texangle = texangle
		self.uscale = uscale
		self.vscale = vscale

		
