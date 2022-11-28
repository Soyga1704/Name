import pygame
import sys
import random
import time
import os

mushroomImg = pygame.image.load(os.path.join('Downloads','mushroom.png'))
mushroomImg = pygame.transform.scale(mushroomImg, (10, 10))

from snake_food import Food
from snake_snake import Snake
from snake_game import Game

game = Game()
snake = Snake(game.green)
food = Food(game.screen_width, game.screen_height)

game.init_and_check_for_errors()
game.set_surface_and_title()

while True:
    snake.change_to = game.event_loop(snake.change_to)

    snake.validate_direction_and_change()
    snake.change_head_position()
    game.score, food.food_pos = snake.snake_body_mechanism(
        game.score, food.food_pos, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)

    food.draw_food(game.play_surface)

    snake.check_for_boundaries(
        game.game_over, game.screen_width, game.screen_height)

    game.show_score()
    game.refresh_screen()
