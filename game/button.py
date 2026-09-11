class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color, h_image=None):
		self.image = image
		self.h_image = h_image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None: 
			self.image = self.text 
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
        
		# for mouse hover
		self.highlighted = False
        
        
	def update(self, screen):
		if self.h_image is not None:
			if self.highlighted == True:
				screen.blit(self.h_image, self.rect)
			else:
				screen.blit(self.image, self.rect)

		if self.text != "":
			screen.blit(self.text, self.text_rect)

	# Check if mouse is on the button
	def check_for_input(self, position):
		return self.rect.collidepoint(position)
	
	def change_color(self, position):
		if self.h_image is not None:
			if self.rect.collidepoint(position):
				self.highlighted = True
			else:
				self.highlighted = False

		if self.rect.collidepoint(position) and self.text != "":
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

	def change_image(self, new_image):
		self.image = new_image

	def set_position(self, center):
		self.rect.center = center
		self.text_rect.center = center
	
   