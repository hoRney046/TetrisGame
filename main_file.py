import random
import sys
import pygame

# Инициализация Pygame
pygame.init()
clock = pygame.time.Clock()

# Размеры окна игры
screen_width, screen_height = 800, 600

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Загрузка изображения тетриса
tetris_image = pygame.image.load('tetris_image.png')

# Создание текста для кнопки
font = pygame.font.Font(None, 36)
button_text = font.render('Начать игру', True, WHITE)

font = pygame.font.Font(None, 36)
button1_text = font.render('Начать новую игру', True, WHITE)

# Определение координат кнопки
button_width = button_text.get_width() + 30
button_height = button_text.get_height() + 20
button_x = 300
button_y = 500
button1_width = button_text.get_width() + 100
button1_height = button_text.get_height() + 20
# Инициализация звука для перемещения и удаления линии

# Инициализация окна игры
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Тетрис")

# Инициализация шрифта для отображения счета
font = pygame.font.Font(None, 36)

# Размер игрового поля
tetris_width, tetris_height = 10, 20

# Размер ячейки игрового поля
cell_size = min(screen_width // tetris_width, screen_height // tetris_height)

# Позиция игрового поля на экране
tetris_x = (screen_width - tetris_width * cell_size) // 2
tetris_y = (screen_height - tetris_height * cell_size) // 2

# Фигуры тетриса
tetrominoes = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]
tetromino_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (0, 255, 255), (255, 0, 255), (255, 165, 0)]

