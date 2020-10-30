import pygame


class GameCharacter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.velocity = 50
        self.jump_state = False

        self._direction = ''
        self._jump_counter = 10
        self._walk_counter = 0
        self._total_animation_pictures = 6

        self._standing_character_image = pygame.image.load("standing.png")
        self._walk_right_animations = [pygame.image.load('walk_right_1.png'), pygame.image.load("walk_right_2.png"),
                                       pygame.image.load("walk_right_3.png"), pygame.image.load("walk_right_4.png"),
                                       pygame.image.load("walk_right_7.png"), pygame.image.load("walk_right_8.png")]

        self._walk_left_animations = [pygame.image.load("walk_left_1.png"), pygame.image.load("walk_left_2.png"),
                                      pygame.image.load("walk_left_3.png"), pygame.image.load("walk_left_4.png"),
                                      pygame.image.load("walk_left_7.png"), pygame.image.load("walk_left_8.png")]

    def draw(self, screen):
        if self._walk_counter > self._total_animation_pictures - 1:
            self._walk_counter = 0

        if self._direction == 'left':
            screen.blit(self._walk_left_animations[self._walk_counter], (self.x, self.y))
            self._walk_counter += 1
            self._direction = ''

        elif self._direction == 'right':
            screen.blit(self._walk_right_animations[self._walk_counter], (self.x, self.y))
            self._walk_counter += 1
            self._direction = ''
        else:
            screen.blit(self._standing_character_image, (self.x, self.y))
            self._walk_counter = 0

    def move_left(self):

        self.x -= self.velocity
        self._walk_counter += 1
        self._direction = 'left'

    def move_right(self):
        self.x += self.velocity
        self._walk_counter += 1
        self._direction = 'right'

    def jump(self):
        if self._jump_counter >= -10:
            self.y -= (self._jump_counter * abs(self._jump_counter)) * 0.5
            self._jump_counter -= 1
        else:
            self._jump_counter = 10
            self.jump_state = False


class GameCanvas:
    def __init__(self, screen_width):
        self.screen_width = screen_width
        self.canvas_color = [0, 0, 0]

    def check_if_inside_left_boundary(self, visual_object):
        return visual_object.x >= visual_object.width

    def check_if_inside_right_boundary(self, visual_object):
        return visual_object.x < (self.screen_width - visual_object.velocity - visual_object.width)

    def draw(self, screen):
        screen.fill(self.canvas_color)


class Game:
    def __init__(self):
        screen_width = 1200
        screen_height = 1000
        self.character = GameCharacter(0, 700)
        self.canvas = GameCanvas(screen_width)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_width, screen_height))

    def run(self):

        running = True
        self.canvas.draw(self.screen)
        self.character.draw(self.screen)
        pygame.display.update()

        while running:
            self.clock.tick(10)
            pygame.init()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT] and self.canvas.check_if_inside_left_boundary(self.character):
                self.character.move_left()

            elif keys[pygame.K_RIGHT] and self.canvas.check_if_inside_right_boundary(self.character):
                self.character.move_right()

            elif keys[pygame.K_SPACE]:
                self.character.jump_state = True

            if self.character.jump_state:
                self.character.jump()

            self.canvas.draw(self.screen)
            self.character.draw(self.screen)

            pygame.display.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
