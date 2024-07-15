from tkinter import messagebox

import pygame

from main import Board


class Gui:
    def __init__(self) -> None:
        pygame.init()
        self.gameboard = Board()
        self.width = 600
        self.height = 600
        self.window = pygame.display.set_mode((self.width, self.height))
        self.FPS = 60
        self.pieces_font = pygame.font.Font('freesansbold.ttf', 130)
        pygame.display.set_caption("Tic Tac Toe")

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                text = self.pieces_font.render(self.gameboard.board[i][j].__str__(), True, 'White')
                prnt = pygame.Rect(j * 200, i * 200, 200, 200)
                if i % 2 == 0:
                    if j % 2 == 0:
                        pygame.draw.rect(self.window, '#C0DD11', prnt)
                    else:
                        pygame.draw.rect(self.window, '#74B01A', prnt)
                else:
                    if j % 2 == 0:
                        pygame.draw.rect(self.window, '#74B01A', prnt)
                    else:
                        pygame.draw.rect(self.window, '#C0DD11', prnt)
                self.window.blit(text, text.get_rect(center=prnt.center))
                pygame.draw.line(self.window, '#FFFFFF', (j * 200, i * 200), (j * 200, 600), width=4)
                pygame.draw.line(self.window, '#FFFFFF', (j * 200, i * 200), (600, i * 200), width=4)

    def make_move(self, row, col):
        return self.gameboard.place_piece(row, col)


if __name__ == "__main__":
    GUI = Gui()
    status = True
    clock = pygame.time.Clock()
    placement = [False, False]
    while status:
        GUI.window.fill('#FFFFFF')
        clock.tick(GUI.FPS)
        GUI.draw_board()
        for event in pygame.event.get():
            if placement[1]:
                messagebox.showinfo('GG', 'Player 1 won!' if GUI.gameboard.turn == 'X' else 'Player 2 won!')
                exit()
            if event.type == pygame.QUIT:
                status = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                location = pygame.mouse.get_pos()
                placement = GUI.gameboard.place_piece(location[1] // 200, location[0] // 200)
        pygame.display.flip()
    pygame.quit()
