import pygame
import Image
import Console

pygame.init()
Console.Clear()

window = pygame.display.set_mode((480, 480), pygame.RESIZABLE)
clock = pygame.time.Clock()

imgs: list[Image.Image] = []

shreck = pygame.image.load(r"C:\Users\Админ\Downloads\Untitled_11-09-2023_05-01-31.png").convert_alpha()
x = -5

for i in range(5):
    img = Image.Image(window,
                    x, # x
                    0, # y
                    64, # width
                    64, # height
                    (160, 160, 160), # color
                    shreck, # image
                    0, # fill size
                    15, # border radius
                    anchor = (Image.Anchor.RIGHT, Image.Anchor.CENTER),
                    screen_resolution = window.get_size(),
                    scale = pygame.Vector2(1, 1)
                    )
    imgs.append(img)
    x -= 64 + 5

while 1:
    window.fill((60, 60, 60))
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        elif event.type == pygame.WINDOWSIZECHANGED:
            for img in imgs:
                img.hash()
    
    for img in imgs:
        img.update()

    pygame.display.update()