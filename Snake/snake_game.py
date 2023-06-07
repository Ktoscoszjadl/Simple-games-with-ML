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
            y -= SNAKE_SEGMENT_SIZE
        elif self.direction == "DOWN":
            y += SNAKE_SEGMENT_SIZE
        elif self.direction == "LEFT":
            x -= SNAKE_SEGMENT_SIZE
        elif self.direction == "RIGHT":
            x += SNAKE_SEGMENT_SIZE

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

    def snake_eating_check(self,food_position):
        if self.snake_segments[0] == food_position:
            return True
        return False

    def draw(self):
        for segment in self.snake_segments:
            pygame.draw.rect(window,GREEN, (segment[0], segment[1], SNAKE_SEGMENT_SIZE, SNAKE_SEGMENT_SIZE))

class Food:
    def __init__(self) -> None:
        self.position = ((random.randint(0,(width-SNAKE_SEGMENT_SIZE)/SNAKE_SEGMENT_SIZE))*SNAKE_SEGMENT_SIZE,(random.randint(0,(height-SNAKE_SEGMENT_SIZE)/SNAKE_SEGMENT_SIZE))*SNAKE_SEGMENT_SIZE)

    def draw(self):
        pygame.draw.rect(window, RED, (self.position[0], self.position[1],SNAKE_SEGMENT_SIZE,SNAKE_SEGMENT_SIZE))

def draw_game():
    pass

snake = Snake()
food = Food()
running = True
while True:
    window.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.change_direction("UP")
            elif event.key == pygame.K_DOWN:
                snake.change_direction("DOWN")
            elif event.key == pygame.K_LEFT:
                snake.change_direction("LEFT")
            elif event.key == pygame.K_RIGHT:
                snake.change_direction("RIGHT")
    food.draw()
    snake.draw()
    snake.move()
    
    if snake.snake_eating_check(food.position):
        snake.size +=1
        food = Food()

    pygame.display.update()
    clock.tick(SNAKE_SPEED)

# pygame.quit()
