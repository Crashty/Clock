import math
import pygame
import datetime as dt

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


class Game:

    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.center = (self.width / 2, self.height / 2)
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption("Clock! ")
        self.font = pygame.font.SysFont(None, 24)
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def loop(self):

        self.screen.fill(BLACK)

        s = dt.datetime.now().second
        m = dt.datetime.now().minute + s / 60
        h = dt.datetime.now().hour + m / 60

        pygame.display.set_caption("Clock! "+str(dt.datetime.now()))

        hour_scale = 12
        minute_scale = 60
        second_scale = 60

        ang_x_hour = math.cos(math.pi * 2 / hour_scale * (h - hour_scale / 4))
        ang_y_hour = math.sin(math.pi * 2 / hour_scale * (h - hour_scale / 4))

        ang_x_m = math.cos(math.pi * 2 / minute_scale * (m - minute_scale / 4))
        ang_y_m = math.sin(math.pi * 2 / minute_scale * (m - minute_scale / 4))

        ang_x_s = math.cos(math.pi * 2 / second_scale * (s - second_scale / 4))
        ang_y_s = math.sin(math.pi * 2 / second_scale * (s - second_scale / 4))

        main_dist = 320

        pygame.draw.circle(self.screen, WHITE, (self.width / 2, self.height / 2), 350, 3)

        # Draw numbers 1-12
        for i in range(1, 13):
            img = self.font.render(str(i), True, WHITE)
            ang_x = math.cos(math.pi * 2 / hour_scale * (i - hour_scale / 4))
            ang_y = math.sin(math.pi * 2 / hour_scale * (i - hour_scale / 4))
            pos_x = ang_x * main_dist
            pos_y = ang_y * main_dist
            img_rect = img.get_rect(center=(pos_x + self.width / 2, pos_y + self.height / 2))
            self.screen.blit(img, img_rect)

        # Draw small lines
        for i in range(60):
            width = 1
            if i % 5 == 0:
                width = 2
            ang_x = math.cos(math.pi * 2 / 60 * (i - 60 / 4))
            ang_y = math.sin(math.pi * 2 / 60 * (i - 60 / 4))
            pos_x1 = ang_x * (main_dist + 13)
            pos_y1 = ang_y * (main_dist + 13)
            pos_x2 = ang_x * (main_dist + 20)
            pos_y2 = ang_y * (main_dist + 20)

            pygame.draw.line(self.screen, WHITE, (self.width / 2 + pos_x1, self.height / 2 + pos_y1),
                             (self.width / 2 + pos_x2, self.height / 2 + pos_y2), width)

        # Hours line
        pygame.draw.line(self.screen, RED, (self.width / 2, self.height / 2),
                         (self.width / 2 + ang_x_hour * 150, self.height / 2 + ang_y_hour * 150), 2)
        # Minutes line
        pygame.draw.line(self.screen, WHITE, (self.width / 2, self.height / 2),
                         (self.width / 2 + ang_x_s * 280, self.height / 2 + ang_y_s * 280), 2)
        # Seconds line
        pygame.draw.line(self.screen, BLUE, (self.width / 2, self.height / 2),
                         (self.width / 2 + ang_x_m * 230, self.height / 2 + ang_y_m * 230), 2)

        pygame.display.update()


if __name__ == "__main__":
    pygame.init()
    game = Game(800, 800)

    while game.running:
        game.handle_events()
        game.loop()
