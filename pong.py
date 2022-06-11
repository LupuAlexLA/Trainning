import simplegui
import random

# Initializare variabile
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = 300,200
ball_vel = 2,-7
paddle1_pos= 200
paddle2_pos = 200
paddle1_vel =  0
paddle2_vel =  0
PADDLE_VEL = 7
score1 = 0
score2 = 0

# initializarea pozitia bilei si viteza din mijlocul mesei
# daca directia e dreapta, sensul mingii este dreapta sus, altfel stanga sus
def spawn_ball(direction):
    global ball_pos, ball_vel # sunt vectori stocati ca liste
    ball_pos = 300,200 # pozitia in sistem ox, oy
    direction_sign = 1 # semnul directiei
    if direction == LEFT:
        direction_sign = -1
    ball_vel = direction_sign * random.randrange(3, 6), -random.randrange(3, 6) # sensul miscarii mingii

# functia care decide ce se intampla cand bila loveste unul dintre pereti sau paleta
def ball_bounce():
    global ball_pos, ball_vel, BALL_RADIUS, HEIGHT, WIDTH, paddle1_pos, paddle2_pos, HALF_PAD_HEIGHT, score1, score2
    
    # cand bila loveste peretele
    # daca atinge sus sau jos se schimba sensu deplasari adica oy
    if ball_pos[1] - BALL_RADIUS < 0 or ball_pos[1] + BALL_RADIUS > HEIGHT:
        # se schimba viteza mingii la lovire
        ball_vel = ball_vel[0], -ball_vel[1] 
    
    # daca mingea atinge atinge peretele stang (sau atinge paleta stanga)
    if ball_pos[0] - BALL_RADIUS < 0 + PAD_WIDTH:
        # verifica daca mingea atinge paleta, schimba sensul random
        if paddle1_pos - HALF_PAD_HEIGHT < ball_pos[1] < paddle1_pos + HALF_PAD_HEIGHT:
            # round - rotunjeste (aproximeaza)
            ball_vel = round(-ball_vel[0] * 1.1), round(ball_vel[1] * 1.1)
        # daca nu atinge paleta, celalalt castiga
        else:
            spawn_ball(RIGHT) # se spawneaza mingea, cu sensul spre dreapta
            score2 = score2 + 1
    # daca atinge atinge peretele drept  (sau atinge paleta dreapta)       
    if ball_pos[0] + BALL_RADIUS > WIDTH - PAD_WIDTH:
        # verifica daca mingea atinge paleta, schimba sensul random
        if paddle2_pos - HALF_PAD_HEIGHT < ball_pos[1] < paddle2_pos + HALF_PAD_HEIGHT:
            ball_vel = -ball_vel[0] * 1.1, ball_vel[1] * 1.1
        else:
            spawn_ball(LEFT) # se spawneaza mingea, cu sensul spre stanga
            score1 = score1 + 1
   
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball(LEFT)
    score1 = 0
    score2 = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
     
    # desenam linia de pe mijloc
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "Red")
    # desenam peretele stang
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "Red")
    # desenam peretele drept
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # updatam mingea
    ball_pos = ball_pos[0] + ball_vel[0], ball_pos[1] + ball_vel[1] 
    ball_bounce()
    
    # desenam mingea
    canvas.draw_circle(ball_pos, BALL_RADIUS, 10, 'White', 'White')
    
    # updatam pozitia verticala a paletei, o mentinem in ecran ( sa nu depaseasca limita ecranului )
    paddle1_pos = paddle1_pos + paddle1_vel
    paddle2_pos = paddle2_pos + paddle2_vel
    # seteaza limita de deplasare pentru paleta intre capetele peretilor
    if paddle1_pos - HALF_PAD_HEIGHT < 0:
        paddle1_pos = 0 + HALF_PAD_HEIGHT
        
    if paddle1_pos + HALF_PAD_HEIGHT > HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    
    if paddle2_pos - HALF_PAD_HEIGHT < 0:
        paddle2_pos = 0 + HALF_PAD_HEIGHT
        
    if paddle2_pos + HALF_PAD_HEIGHT > HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
       
    # desenam paletele
    canvas.draw_line((HALF_PAD_WIDTH, (paddle1_pos - HALF_PAD_HEIGHT)), (HALF_PAD_WIDTH, (paddle1_pos + HALF_PAD_HEIGHT)), PAD_WIDTH, 'White')
    canvas.draw_line((WIDTH - HALF_PAD_WIDTH, (paddle2_pos - HALF_PAD_HEIGHT)), (WIDTH - HALF_PAD_WIDTH, (paddle2_pos + HALF_PAD_HEIGHT)), PAD_WIDTH, 'White')    
    
    # desenam scorurile
    canvas.draw_text(str(score1), (230, 50), 40, 'Red')
    canvas.draw_text(str(score2), (350, 50), 40, 'Red')
   
    # functia care se aplica atunci cand tinem apasat un buton
def keydown(key):
    global paddle1_vel, paddle2_vel, PADDLE_VEL
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -PADDLE_VEL
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = PADDLE_VEL
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -PADDLE_VEL
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = PADDLE_VEL
   
    # functia care se aplica atunci cand luam degetul de pe buton
def keyup(key):
    global paddle1_vel, paddle2_vel, PADDLE_VEL
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

# cream frame-ul (fereastra) 
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button1 = frame.add_button('Reset', new_game)

# start frame
new_game()
frame.start()