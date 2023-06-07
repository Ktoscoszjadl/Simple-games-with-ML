import pygame
import random
import time
from sys import exit
#initialize game
pygame.init()
width,height = 640, 480
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
#colors
BLACK = (0,0,0)
RED = (200,0,0)
GREEN = (0, 255, 0)

SNAKE_SEGMENT_SIZE = 20
SNAKE_SPEED = 10

#snake
class Snake:
    def __init__(self) -> None:
        self.size = 1
        self.snake_segments = [(width // 2, height // 2)]
        self.direction = 'RIGHT'

    def move(self):
        x, y = self.snake_segments[0]
        if self.direction == "UP":
            y -= 10
        elif self.direction == "DOWN":
            y += 10
        elif self.direction == "LEFT":
            x -= 10
        elif self.direction == "RIGHT":
            x += 10

        self.snake_segments.insert(0, (x, y))

        if len(self.snake_segments) > self.size:
            self.snake_segments.pop()

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction

    def draw(self):
        for segment in self.snake_segments:
            pygame.draw.rect(window,GREEN, (segment[0], segment[1], SNAKE_SEGMENT_SIZE, SNAKE_SEGMENT_SIZE))

class Food:
    def __init__(self) -> None:
        self.position = ((random.randint(0,(width-SNAKE_SEGMENT_SIZE)/10))*10,(random.randint(0,(height-SNAKE_SEGMENT_SIZE)/10))*10)

    def draw(self):
        pygame.draw.rect(window, RED, (self.position[0], self.position[1],SNAKE_SEGMENT_SIZE,SNAKE_SEGMENT_SIZE))

def draw_game():
    pass

snake = Snake()
food = Food()
while True:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    snake.draw()
    food.draw()
    pygame.display.update()
    clock.tick(SNAKE_SPEED)

# pygame.quit()
