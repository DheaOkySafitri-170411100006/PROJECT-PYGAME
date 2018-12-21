import pygame
class Sprite():
    """A SIMPLE SPRITE CLASSES WITH SOME UTILITY FUNCTIONS """

    
    """ SETUP THE CONSTANTS USED IN THE MOVE FUNCTION """
    LEFT = "left"
    RIGHT = "right"
    UP = "up"
    DOWN = "down"
    def __init__(self, img, position): 
        self.img = img
        self.img_rect = self.img.get_rect()
        self.s_pos = position
        self.img_rect.topleft = self.s_pos #posisi awal
        self.speed =0

    # speed pergerakan control dari player.
    def set_speed(self, s):
        if(s > 0 and s <=  50):
            self.speed = s
        else:
            raise ValueError("the speed must be between one and 50")
    def update(self):
        surface = pygame.display.get_surface()
        surface.blit(self.img,self.img_rect)

    # control pergerakan player
    def move(self, const):#Make movement in four directions(up, down, left, right) based on const value
        size = pygame.display.get_surface().get_rect().size
        if(const == "left"):
            self.img_rect.move_ip(-1 *self.speed, 0)
        if(const=="right"):
            self.img_rect.move_ip(self.speed, 0)
        if(const == "up"):
            self.img_rect.move_ip(0, -1*self.speed)
        if(const == "down"):
            self.img_rect.move_ip(0, self.speed)

   
   


    
