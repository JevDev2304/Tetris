class Colors:
	dark_grey = (26, 31, 40)
	green = (47, 230, 23)
	red = (232, 18, 18)
	orange = (226, 116, 17)
	yellow = (237, 234, 4)
	purple = (166, 0, 247)
	cyan = (21, 204, 209)
	blue = (13, 64, 216)
	white = (255, 255, 255)
	dark_blue = (44, 44, 127)
	light_blue = (59, 85, 162)
	lila = ( 0, 0, 0)

	background_grid2 = (174, 182, 191)
	lila2 = (232, 218, 239)
	green2 = (162, 217, 206)
	cyan2 = (174, 214, 241)
	orange2 = (250, 215, 160)
	yellow2 = (249, 231, 159)
	salmon2 = (245, 183, 177)
	pink=  (211, 250, 247)

	@classmethod
	def get_cell_colors(cls):
		return [cls.white, cls.lila2, cls.green2, cls.cyan2, cls.orange2, cls.yellow2, cls.salmon2, cls.pink]
