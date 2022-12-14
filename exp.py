import pygame, numpy

def exp(screen, color, position):
    Blast = []
    for i in range(1, 6):
        Blast.append(pygame.image.load("exp/exp" + str(i) + ".png"))
    print(len(Blast))

    for i in range(1, 60, 1):
        screen.fill((255, 255, 255))
        if (i < 25):
            HalfWidth = int(Blast[int(i/5)].get_width()/2)
            HalfHeight = Blast[int(i/5)].get_height()/2
            screen.blit(Blast[int(i/5)], (position[0] - HalfWidth, int(position[1] - HalfHeight)))
        pygame.draw.circle(screen, (70, 163, 141), (250, 250), int(numpy.power(i, 2.2)), int(4/3*numpy.log2(i)))
        pygame.display.flip()
        pygame.time.delay(50)

pygame.init()

screen = pygame.display.set_mode([800, 600])
color = (70, 163, 141)
position = (250, 250)

screen.fill((255, 255, 255))

exp(screen, color, position)

pygame.quit()
