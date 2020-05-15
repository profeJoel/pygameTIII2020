# coding=utf-8

# imports the Pygame library
import pygame


def main():
    # initializes Pygame
    pygame.init()

    # sets the window title
    pygame.display.set_caption(u'Key repetition')

    # sets the window size
    pygame.display.set_mode((400, 400))

    # enables the key repetition
    pygame.key.set_repeat(400, 100)

    # gets the key repetition times
    delay, interval = pygame.key.get_repeat()

    # prints the key repetition times on the console
    print( u'delay: {}, inteval: {}'.format(delay, interval))

    # is the application running?
    is_running = True
    doubleClick = False
    timer = 100000

    # if the application is running
    while is_running:
        # gets events from the event queue
        for event in pygame.event.get():
            # if the 'close' button of the window is pressed
            if event.type == pygame.QUIT:
                # stops the application
                is_running = False

            # captures the 'KEYDOWN' and 'KEYUP' events
            if event.type in (pygame.KEYDOWN, pygame.KEYUP):
                # gets the key name
                key_name = pygame.key.name(event.key)

                # converts to uppercase the key name
                key_name = key_name.upper()

                # if any key is pressed
                if event.type == pygame.KEYDOWN and key_name == 'N':
                    # prints on the console that the key has been pressed
                    #print( u'Key "{}" pressed (time: {} ms)'.format(key_name, pygame.time.get_ticks()))
                    if doubleClick is True:
                        if timer > 0:
                            print("Doble click!!!")
                        doubleClick = False
                        timer = 100000
                    else:
                        doubleClick = True
                        timer = 100000

                # if any key is released
                elif event.type == pygame.KEYUP:
                    # prints on the console that the key has been released
                    print( u'Key "{}" released (time: {} ms)'.format(key_name, pygame.time.get_ticks()))
        timer -= 1
    # finalizes Pygame
    pygame.quit()


if __name__ == '__main__':
    main()
