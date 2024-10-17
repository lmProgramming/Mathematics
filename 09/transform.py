import pygame

class Transform:
    def __init__(self, position) -> None:
        self.set_position(position)
        
    def get_position(self) -> pygame.Vector3:
        return self.position
    
    def set_position(self, position) -> None:
        self.position: pygame.math.Vector3 = pygame.math.Vector3(position)
        
    def move(self, vector) -> None:
        if vector is not pygame.math.Vector3:
            vector = pygame.math.Vector3(vector)
        self.position = self.position + vector
        
    def move_x(self, amount) -> None:
        self.position = pygame.math.Vector3(self.position.x + amount, self.position.y, self.position.z)
