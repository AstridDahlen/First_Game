# TODO: Game mechanics proposals
#  create an enemy
#  let the enemy start on the right side of the screen
#  let the enemy move to the left
#  if player and enemy collides, end game (for example use running = false))
#  if the enemy is outside of the screen, remove the enemy)
#  Summon one more enemy


# TODO: Add image assets folder
#  add an image_assets folder and move the pictures to the folder
#  handle errors (they wont be found by the program)
#  https://stackoverflow.com/questions/37366461/load-png-images-from-a-different-directory-python-pygame
#  for example self._standing_character_image = pygame.image.load(os.path.join('image_assets', 'standing.png'))
#  a more advanced solution would be to try to solve it in a way that demands less repetition

import pygame



class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.velocity = 10
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

        screen.blit(self._walk_right_animations[self._walk_counter], (self.x, self.y))
        self._walk_counter += 1
        self._direction = ''

    def move(self):
        self.x -= self.velocity
        self._walk_counter += 1


class Player:
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

        #TODO: have one counter for each animation

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

    def walk_left(self):
        self.x -= self.velocity
        self._walk_counter += 1
        self._direction = 'left'

    def walk_right(self):
        self.x += self.velocity
        self._walk_counter += 1
        self._direction = 'right'

    def jump(self):
        if self._jump_counter >= -10:

            #  Todo : is this gravity? Then maybe create gravity variable
            self.y -= (self._jump_counter * abs(self._jump_counter)) * 0.8
            self._jump_counter -= 2
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
        bg = pygame.image.load("bg.png")
        screen.blit(bg, (0, 0))


class GameHandler:
    def __init__(self):
        pass

    def check_if_collision(self):
        pass

    def collision(self, player, enemy):
        pass


class Game:
    def __init__(self):
        screen_width = 1200
        screen_height = 700
        self.player = Player(0, 500)
        self.enemy = Enemy(1100, 500)
        self.characters = [self.player, self.enemy]
        self.canvas = GameCanvas(screen_width)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        bg = pygame.image.load("bg.png")


    def run(self):

        running = True

        self.canvas.draw(self.screen)


        while running:

            self.clock.tick(10)
            pygame.init()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_LEFT] and self.canvas.check_if_inside_left_boundary(self.player):
                self.player.walk_left()

            elif pressed_keys[pygame.K_RIGHT] and self.canvas.check_if_inside_right_boundary(self.player):
                self.player.walk_right()

            elif pressed_keys[pygame.K_SPACE]:
                self.player.jump_state = True

            if self.player.jump_state:
                self.player.jump()

            self.canvas.draw(self.screen)
            self.enemy.move()

            for character in self.characters:
                character.draw(self.screen)

            pygame.display.update()


def main():
    game = Game()
    game.run()


if __name__ == '__main__':
    main()
