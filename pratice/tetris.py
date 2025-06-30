import pygame
import random

# --- 설정 상수 ---
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
BLOCK_SIZE = 30
COLUMNS = SCREEN_WIDTH // BLOCK_SIZE
ROWS = SCREEN_HEIGHT // BLOCK_SIZE
FPS = 60

# --- 색상 정의 ---
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # I
    (0, 0, 255),    # J
    (255, 165, 0),  # L
    (255, 255, 0),  # O
    (0, 255, 0),    # S
    (128, 0, 128),  # T
    (255, 0, 0)     # Z
]

# --- 테트로미노 정의 ---
TETROMINOES = {
    'I': [[1, 1, 1, 1]],
    'J': [[1, 0, 0],
          [1, 1, 1]],
    'L': [[0, 0, 1],
          [1, 1, 1]],
    'O': [[1, 1],
          [1, 1]],
    'S': [[0, 1, 1],
          [1, 1, 0]],
    'T': [[0, 1, 0],
          [1, 1, 1]],
    'Z': [[1, 1, 0],
          [0, 1, 1]],
}

# --- 도우미 함수 ---
def rotate(shape):
    return [[shape[y][x] for y in range(len(shape))] for x in range(len(shape[0]) - 1, -1, -1)]

def create_grid(locked_positions={}):
    grid = [[BLACK for _ in range(COLUMNS)] for _ in range(ROWS)]
    for y in range(ROWS):
        for x in range(COLUMNS):
            if (x, y) in locked_positions:
                grid[y][x] = locked_positions[(x, y)]
    return grid

# --- 블록 클래스 ---
class Tetromino:
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = TETROMINOES[shape]
        self.color = COLORS[list(TETROMINOES.keys()).index(shape)]
        self.rotation = 0

    def image(self):
        return rotate(self.shape) if self.rotation % 4 != 0 else self.shape

    def cells(self):
        return [(self.x + j, self.y + i) for i, row in enumerate(self.image()) for j, val in enumerate(row) if val]

# --- 충돌 검사 ---
def valid_position(shape, grid):
    for x, y in shape.cells():
        if x < 0 or x >= COLUMNS or y >= ROWS or (y >= 0 and grid[y][x] != BLACK):
            return False
    return True

# --- 줄 제거 ---
def clear_rows(grid, locked):
    full_rows = [i for i, row in enumerate(grid) if BLACK not in row]
    for row in full_rows:
        for x in range(COLUMNS):
            try:
                del locked[(x, row)]
            except:
                continue
    if full_rows:
        for key in sorted(list(locked.keys()), key=lambda k: k[1])[::-1]:
            x, y = key
            if y < min(full_rows):
                locked[(x, y + len(full_rows))] = locked.pop(key)
    return len(full_rows)

# --- 주 게임 루프 ---
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    grid = create_grid()
    locked_positions = {}

    change_piece = False
    run = True
    current_piece = Tetromino(3, 0, random.choice(list(TETROMINOES.keys())))
    next_piece = Tetromino(3, 0, random.choice(list(TETROMINOES.keys())))
    fall_time = 0
    fall_speed = 0.5
    score = 0

    while run:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick(FPS)

        if fall_time / 1000 >= fall_speed:
            current_piece.y += 1
            if not valid_position(current_piece, grid):
                current_piece.y -= 1
                change_piece = True
            fall_time = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_position(current_piece, grid):
                        current_piece.x += 1
                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_position(current_piece, grid):
                        current_piece.x -= 1
                elif event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not valid_position(current_piece, grid):
                        current_piece.y -= 1
                elif event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not valid_position(current_piece, grid):
                        current_piece.rotation -= 1

        for x, y in current_piece.cells():
            if y >= 0:
                grid[y][x] = current_piece.color

        if change_piece:
            for x, y in current_piece.cells():
                if y < 0:
                    run = False  # Game Over
                locked_positions[(x, y)] = current_piece.color
            current_piece = next_piece
            next_piece = Tetromino(3, 0, random.choice(list(TETROMINOES.keys())))
            change_piece = False
            score += clear_rows(grid, locked_positions) * 10

        screen.fill(BLACK)
        for y in range(ROWS):
            for x in range(COLUMNS):
                pygame.draw.rect(screen, grid[y][x],
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
                pygame.draw.rect(screen, GRAY,
                                 (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

        pygame.display.update()

main()