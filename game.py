import pgzrun 

WIDTH = 800
HEIGHT = 800

spaceship = Actor('spaceship2.png')
spaceship.pos = (400,650)
aliens = []
bullets = []
game = True

for x in range(5):
    for y in range(5):
        alien = Actor('alien3.png')
        alien.x = 200 + x*100
        alien.y = 50 + y*50
        aliens.append(alien)

speedx = 6
speedy = 3
def update():  
    global game 
    if keyboard.right:
        spaceship.x += 5
    if keyboard.left:
        spaceship.x -= 5
    for a in aliens:
        a.y+=0.7
        for b in bullets:
            if b.colliderect(a):
                bullets.remove(b)
                aliens.remove(a)
        if a.colliderect(spaceship):
            game = 'lost'
    for b in bullets:
        b.y-=5

    
    

    


def draw():
    global game
    screen.clear()
    screen.fill('black') 
    screen.blit('space.jpg',(0,0))
    spaceship.draw()
    for i in aliens:
        i.draw()
    for b in bullets:
        b.draw()
    if game == 'lost':
        screen.fill('black')
        screen.draw.text('You lost',(100,100),fontsize = 50)

def on_key_down(key):
    global bullets,aliens
    if key == keys.SPACE:
        bullet = Actor('bullet.png')
        bullet.x = spaceship.x
        bullet.y = spaceship.y
        bullets.append(bullet)




pgzrun.go()
    