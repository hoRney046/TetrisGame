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
# Генерация новой фигуры
def generate_tetromino():
    tetromino_index = random.randint(0, len(tetrominoes) - 1)
    tetromino = tetrominoes[tetromino_index]
    tetromino_color = tetromino_colors[tetromino_index]
    return tetromino, tetromino_color


# Проверка возможности размещения фигуры на игровом поле
def check_collision(tetromino, tetromino_x, tetromino_y, tetris_grid):
    for y in range(len(tetromino)):
        for x in range(len(tetromino[y])):
            if tetromino[y][x] and (
                    tetromino_x + x < 0 or tetromino_x + x >= tetris_width or tetromino_y + y >= tetris_height or
                    tetris_grid[tetromino_y + y][tetromino_x + x]):
                return True
    return False

