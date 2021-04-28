import pygame, sys, random

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000,1000))
pygame.display.set_caption('My Game')

Player_Width = 32
Player_Height = 32
Starting_X = 500/2 - Player_Width
Starting_Y = 15 + Player_Height
Starting_Gravity = 0.7
Starting_Margin = Player_Height * 0.8

Player_X = Starting_X
Player_Y = Starting_Y
Velocity = pygame.Vector2()
Velocity.xy = 3,-1
Gravity = Starting_Gravity
Friction = pygame.Vector2()
Friction.xy = -0.95,-0.8
Margin = Starting_Margin
Opposite_Gravity = False
Opposite_Gravity_Value = Gravity*-1


def draw_rect(screen, color, X, Y, width, height):
    pygame.draw.rect(screen, color, (X, Y, width, height))
def draw_image(screen, image, X, Y):
    screen.blit(image, (X,Y))

running = True

while running:
    pygame.time.clock.tick(60)
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:           
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        Gravity *= -1
    if keys[pygame.K_b]:
        Velocity.xy = 3,3
        Gravity = 0.9
        Friction.xy = -0.9,-0.8
        Margin = Starting_Margin
        Player_Y = Starting_X
        Player_X = Starting_X
    if keys[pygame.K_n]:
        Opposite_Gravity = True
    if keys[pygame.K_v]:
        Opposite_Gravity = False


    if Player_X + Player_Width > screen.get_width() - Margin: #right
        Velocity.x *= Friction.x
    if Player_X < Margin:
        Velocity.x *= Friction.x #left
    if Player_Y < Margin:
        Velocity.y *= Friction.y   #up
    if Player_Y + Player_Height > screen.get_height() - Margin:   #down
        Velocity.y *= Friction.y
    if Opposite_Gravity:
        Gravity = Opposite_Gravity_Value
    if not Opposite_Gravity:
        Gravity = Starting_Gravity
    
    Player_Y += round(Velocity.y, 0)
    Velocity.y += Gravity

    Player_X += Velocity.x


    draw_rect(screen, (255,0,0), Player_X, Player_Y, Player_Width, Player_Height)

    pygame.display.update()

    pygame.time.delay(10)

    print("X Vel: " + str(round(abs(Velocity.x), 1)) + "  |  Y Vel: " + str(round(abs(Velocity.y), 1)) + "  |  X Fri: " + str(round(abs(Friction.x), 1)) + "  |  Y Fric: " + str(round(abs(Friction.y),1)) + "  |  X Pos:  " + str(round(abs(Player_X),1)) + "  |  Y Pos:  " + str(round(abs(Player_Y),1)) + "  |  Opposite Gravity:   " + str(Opposite_Gravity))
