import pygame
from game import constants, utils, slider
class ImageSlider(slider.Slider):
    def __init__(self, x, y, width, height, min_val, max_val, current_val, label, bg_image, fill_image, size, color):
        super().__init__(x, y, width, min_val, max_val, current_val, label, size)
        self.height = height
        self.color = color
        self.size = size
        
        self.bg_image = bg_image
        self.fill_image = fill_image
        
        # scale images to slider size
        #self.bg_image = pygame.transform.scale(bg_image, (self.width, self.height))
        #self.fill_image = pygame.transform.scale(fill_image, (self.width, self.height))

    def draw(self, screen):
        # draw background
        screen.blit(self.bg_image, (self.x, self.y, self.width, self.height))

        # draw filled part
        fill_width = int(self.get_percentage() * self.width)
        screen.blit(self.fill_image, (self.x, self.y, self.width, self.height),
                    (0, 0, fill_width, self.height))

        # text (same as parent)
        if self.max_val <= 1:
            display_val = f"{int(self.value * 100)}%"
        else:
            display_val = f"{int(self.value)} ms"
        
        if self.label == "":
            text = utils.get_font(utils.scale_y(self.size)).render(f"[ {display_val} ]", True, self.color)
        else:
            text = utils.get_font(utils.scale_y(self.size)).render(f"{self.label}: {display_val}", True, self.color)
        
        screen.blit(text, (self.x - utils.scale_y(self.width / 4), self.y))