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
# Заполнение ячеек игрового поля
def draw_grid(tetris_grid, tetromino, tetromino_x, tetromino_y, tetromino_color):
    for y in range(tetris_height):
        for x in range(tetris_width):
            pygame.draw.rect(screen, BLACK, (tetris_x + x * cell_size, tetris_y + y * cell_size,
                                             cell_size, cell_size), 1)
            if tetris_grid[y][x]:
                pygame.draw.rect(screen, tetris_grid[y][x], (tetris_x + x * cell_size, tetris_y + y * cell_size,
                                                             cell_size, cell_size))
    for y in range(len(tetromino)):
        for x in range(len(tetromino[y])):
            if tetromino[y][x]:
                pygame.draw.rect(screen, tetromino_color, (tetris_x + (tetromino_x + x) * cell_size,
                                                           tetris_y + (tetromino_y + y) * cell_size,
                                                           cell_size, cell_size))


# Очистка заполненных линий и обновление счета
def clear_lines(tetris_grid):
    full_lines = []
    for y in range(tetris_height):
        if all(tetris_grid[y]):
            full_lines.append(y)
    for line in full_lines:
        del tetris_grid[line]
        tetris_grid.insert(0, [None] * tetris_width)
    return len(full_lines)
# Запуск игры
def run_game():
    tetromino, tetromino_color = generate_tetromino()
    tetromino_x, tetromino_y = tetris_width // 2 - len(tetromino[0]) // 2, 0
    tetris_grid = [[None] * tetris_width for _ in range(tetris_height)]

    score = 0
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if not check_collision(tetromino, tetromino_x - 1, tetromino_y, tetris_grid):
                        tetromino_x -= 1
                if event.key == pygame.K_RIGHT:
                    if not check_collision(tetromino, tetromino_x + 1, tetromino_y, tetris_grid):
                        tetromino_x += 1
                if event.key == pygame.K_DOWN:
                    if not check_collision(tetromino, tetromino_x, tetromino_y + 1, tetris_grid):
                        tetromino_y += 1
                if event.key == pygame.K_SPACE:
                    rotated_tetromino = [[tetromino[y][x] for y in range(len(tetromino))] for x in
                                         range(len(tetromino[0]) - 1, -1, -1)]
                    if not check_collision(rotated_tetromino, tetromino_x, tetromino_y, tetris_grid):
                        tetromino = rotated_tetromino

        if not check_collision(tetromino, tetromino_x, tetromino_y + 1, tetris_grid):
            tetromino_y += 1
        else:
            for y in range(len(tetromino)):
                for x in range(len(tetromino[y])):
                    if tetromino[y][x]:
                        tetris_grid[tetromino_y + y][tetromino_x + x] = tetromino_color
            cleared_lines = clear_lines(tetris_grid)
            if cleared_lines > 0:
                score += 10 * cleared_lines
            tetromino, tetromino_color = generate_tetromino()
            tetromino_x, tetromino_y = tetris_width // 2 - len(tetromino[0]) // 2, 0
            if check_collision(tetromino, tetromino_x, tetromino_y, tetris_grid):
                game_over = True
                end_screen()

        screen.fill(WHITE)
        draw_grid(tetris_grid, tetromino, tetromino_x, tetromino_y, tetromino_color)

        score_text = font.render("Score: " + str(score), True, BLACK)
        screen.blit(score_text, (20, 20))

        pygame.display.update()

        clock.tick(6)


def first_screen():
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_x <= mouse_pos[0] <= button_x + button_width and \
                        button_y <= mouse_pos[1] <= button_y + button_height:
                    # Переход в основную игру
                    run_game()

        # Очистка экрана
        screen.fill(WHITE)

        # Отрисовка изображения тетриса
        tetris_rect = tetris_image.get_rect(center=(200, 140))
        scale = pygame.transform.scale(
            tetris_image, (tetris_image.get_width() * 2 + 100,
                           tetris_image.get_height() * 2 + 100))
        screen.blit(scale, tetris_rect)

        # Отрисовка кнопки
        pygame.draw.rect(screen, BLACK, (button_x, button_y, button_width, button_height))
        screen.blit(button_text, (button_x + 15, button_y + 10))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)


def end_screen():
    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button_x <= mouse_pos[0] <= button_x + button_width and \
                        button_y <= mouse_pos[1] <= button_y + button_height:
                    # Переход в основную игру
                    run_game()

        # Очистка экрана
        screen.fill(WHITE)

        # Отрисовка изображения тетриса
        tetris_rect = tetris_image.get_rect(center=(200, 140))
        scale = pygame.transform.scale(
            tetris_image, (tetris_image.get_width() * 2 + 100,
                           tetris_image.get_height() * 2 + 100))
        screen.blit(scale, tetris_rect)

        # Отрисовка кнопки
        pygame.draw.rect(screen, BLACK, (button_x, button_y, button1_width, button1_height))
        screen.blit(button1_text, (button_x + 15, button_y + 10))

        # Обновление экрана
        pygame.display.flip()
        clock.tick(60)


first_screen()
pygame.quit()
sys.exit()
