import os

import pygame


class GameCharacter:
    def __init__(self):
        self.width = 50
        self.height = 50
        self.x = 0
        self.y = 700
        self.is_jumping = False
        self.jumpCounter = 10
        self.direction = ''
        self.walk_counter = 0
        self.velocity = 50
        self.total_animation_pictures = 6

        self.standing_character_image = pygame.image.load("standing.png")
        self.walk_right_animations = [pygame.image.load('walk_right_1.png'), pygame.image.load("walk_right_2.png"),
                                      pygame.image.load("walk_right_3.png"), pygame.image.load("walk_right_4.png"),
                                      pygame.image.load("walk_right_7.png"), pygame.image.load("walk_right_8.png")]

        self.walk_left_animations = [pygame.image.load("walk_left_1.png"), pygame.image.load("walk_left_2.png"),
                                     pygame.image.load("walk_left_3.png"), pygame.image.load("walk_left_4.png"),
                                     pygame.image.load("walk_left_7.png"), pygame.image.load("walk_left_8.png")]

    def draw(self, screen):
        if self.walk_counter > self.total_animation_pictures - 1:
            self.walk_counter = 0

        if self.direction == 'left':
            screen.blit(self.walk_left_animations[self.walk_counter], (self.x, self.y))
            self.walk_counter += 1
            self.direction = ''

        elif self.direction == 'right':
            screen.blit(self.walk_right_animations[self.walk_counter], (self.x, self.y))
            self.walk_counter += 1
            self.direction = ''
        else:
            screen.blit(self.standing_character_image, (self.x, self.y))
            self.walk_counter = 0

    def move_left(self):

        self.x -= self.velocity
        self.walk_counter += 1
        self.direction = 'left'

    def move_right(self):
        self.x += self.velocity
        self.walk_counter += 1
        self.direction = 'right'

    def jump(self):
        if self.jumpCounter >= -10:
            self.y -= (self.jumpCounter * abs(self.jumpCounter)) * 0.5
            self.jumpCounter -= 1
        else:
            self.jumpCounter = 10
            self.is_jumping = False


class GameCanvas:
    def __init__(self):
        self.screen_size = 1500

    def check_if_inside_left_boundary(self, visual_object):
        return visual_object.x >= visual_object.width

    def check_if_inside_right_boundary(self, visual_object):
        return visual_object.x < (self.screen_size - visual_object.velocity - visual_object.width)



def main():
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((1500, 1500))
    BLACK = [0, 0, 0]

    screen.fill(BLACK)

    def redrawGameWindow():
        screen.fill(BLACK)

        character.draw(screen)

        pygame.display.update()

    run = True
    character = GameCharacter()

    while run:
        clock.tick(10)

        canvas = GameCanvas()
        pygame.init()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    is_running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and canvas.check_if_inside_left_boundary(character):
            character.move_left()

        elif keys[pygame.K_RIGHT] and canvas.check_if_inside_right_boundary(character):
            character.move_right()

        elif keys[pygame.K_SPACE]:
            character.is_jumping = True

        if character.is_jumping:
            character.jump()

        redrawGameWindow()

        pressed_keys = pygame.key.get_pressed()

        pygame.display.update()


if __name__ == '__main__':
    main()
