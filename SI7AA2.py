import pygame, sys

pygame.init()
clock=pygame.time.Clock()

screen = pygame.display.set_mode((400,600))

background_image = pygame.image.load("bg.jpg").convert_alpha()
enemy_image = pygame.image.load("enemy.png").convert_alpha()
player_image = pygame.image.load("player.png").convert_alpha()

#creating objects of game
player=pygame.Rect(200,500,30,30)
playerSpeed=20
enemy=pygame.Rect(70,50,40,40)
enemyspeed= -2;
enemies=[]

for j in range(1,5): 
    for i in range(1,5):
        enemies.append( pygame.Rect(i*70,j*50,40,40) )

bullet=pygame.Rect(200,400,5,10)
bulletspeed=5 
bulletState="ready"
        
score=0
score_font=pygame.font.Font('freesansbold.ttf', 12)
over_font=pygame.font.Font('freesansbold.ttf', 25)

while True:    
    screen.fill((0,0,0))
    screen.blit(background_image,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.x -=playerSpeed
            if event.key ==pygame.K_RIGHT:
                player.x +=playerSpeed
            if event.key == pygame.K_SPACE:
                bulletState="fired"
    
    if bulletState == "ready":
        bullet.x=player.x+17
        bullet.y=player.y+12
    
    if bulletState =="fired":
       bullet.y=bullet.y-bulletspeed
       if bullet.y<0:
           bulletState="ready"
    
    
    for enemy in enemies:
        enemy.x= enemy.x + enemyspeed
        
        if enemy.x == 0 or enemy.x==380:
            enemyspeed=enemyspeed * -1
            for e in enemies:
                e.y=e.y+20
        
        if bullet.colliderect(enemy):
            enemy.y=-9000
            enemy.x=-10000
            bullet.y=-10000
            score=score+1
            
        
        if player.colliderect(enemy):
            player.y=-1000
            enemy.y=-1000
            enemyspeed=0
            screen.blit(over_text,[130,250])
            
        
        #pygame.draw.rect(screen,(123,200,100),enemy)
        screen.blit(enemy_image,enemy)
    
    if score==16:
       win_text=over_font.render("Winner!",False,(255,255,255))
       screen.blit(win_text,[160,250])
        
    pygame.draw.rect(screen,(225,225,15),bullet)         
    #pygame.draw.rect(screen,(23,100,100),player)
    screen.blit(player_image,player)
    score_text=score_font.render("Score : "+ str(score), False, (255,255,255))   
    screen.blit(score_text,[10,10]) 
    name_text=score_font.render("Your name", False, (000,200,255))   
    screen.blit(name_text,[300,10]) 
    
    over_text=over_font.render("GAME OVER", False, (255,255,255)) 
    
    pygame.display.update()
    clock.tick(30)
