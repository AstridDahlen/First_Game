import os

import pygame


class GameCharacter:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 0
        self.y = 700
        self.is_jumping = False

        self._direction = ''
        self._jumpCounter = 10
        self._walk_counter = 0
        self._velocity = 50
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

        self.x -= self._velocity
        self._walk_counter += 1
        self._direction = 'left'

    def move_right(self):
        self.x += self._velocity
        self._walk_counter += 1
        self._direction = 'right'

    def jump(self):
        if self._jumpCounter >= -10:
            self.y -= (self._jumpCounter * abs(self._jumpCounter)) * 0.5
            self._jumpCounter -= 1
        else:
            self._jumpCounter = 10
            self.is_jumping = False


class GameCanvas:
    def __init__(self):
        self.screen_size = 1500

    def check_if_inside_left_boundary(self, visual_object):
        return visual_object.x >= visual_object.width

    def check_if_inside_right_boundary(self, visual_object):
        return visual_object.x < (self.screen_size - visual_object._velocity - visual_object.width)


def main():
    character = GameCharacter()
    canvas = GameCanvas()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1500, 1500))

    run = True

    while run:
        clock.tick(10)
        pygame.init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and canvas.check_if_inside_left_boundary(character):
            character.move_left()

        elif keys[pygame.K_RIGHT] and canvas.check_if_inside_right_boundary(character):
            character.move_right()

        elif keys[pygame.K_SPACE]:
            character.is_jumping = True

        if character.is_jumping:
            character.jump()

        BLACK = [0, 0, 0]
        screen.fill(BLACK)
        character.draw(screen)

        pygame.display.update()


if __name__ == '__main__':
    main()
