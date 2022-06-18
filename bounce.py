import simplegui
import random

width = 800
height = 400
ball_radius = 20
score = 0
highscore = 0
paddle_vel = 0
paddle_pos = width / 2
ball_pos = [width / 2, height / 2]
gravity = 0.5
ball_vel = [0, 0]
paddle_width = 160
drift = 0 # variabila care ofera directia aleatoare

def draw(canvas):
    global score, highscore, paddle_vel, ball_vel, paddle_pos, ball_pos, gravity, drift, paddle_width
    
    # desenarea mingii
    canvas.draw_circle(ball_pos, ball_radius, 2, "Red", "White")
  
    # desenarea paletei
    canvas.draw_polygon([ [paddle_pos, 350], [paddle_pos, 360], [paddle_pos + paddle_width, 360], [paddle_pos + paddle_width, 350]], 2,"Red", "White")
                    
    # actualizarea pozitiei paletei
    paddle_pos += paddle_vel
                   
    # actualizarea mingii
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]                
    ball_vel[0] += drift   # miscarea pe orizontala (aleatorie)              
    ball_vel[1] += gravity # miscarea pe verticala               
                    
    # cazul in care mingea atinge paleta                
    if (ball_pos[1] == 330):
        # daca poz bilei pe orizontala se afla intre intervalul:
        # mingea va atinge paleta
        if (paddle_pos <= ball_pos[0] <= paddle_pos + paddle_width):
            ball_vel[1] *= -1
            ball_vel[1] += 0.5        
            drift = random.choice([-0.1, -0.05, -0.07, -0.02, 0.1, 0.05, 0.07, 0.02])        
            score += 1        
                    
    # daca mingea atinge marginile laterale                
    if ( (ball_pos[0] + drift < 0) or (ball_pos[0] + drift > 800) ):
        ball_vel[0] *= -1 # viteza va reveni la valoarea initiala
                    
    # cazul in care mingea nu atinge paleta                
    ball_pos[1] > 400                
    if (ball_pos[1] > 380):                
        if (score > highscore):
            highscore = score
        new_game()        

    # desenare score / highscore                  
    canvas.draw_text("Score:", (300, 80), 44, "Gray", "serif") 
    canvas.draw_text(str(score), [440, 80], 44, "Green", "serif")                
    canvas.draw_text("Highcore:", (620, 50), 24, "Gray", "serif") 
    canvas.draw_text(str(highscore), [760, 50], 24, "Red", "serif")                

# functia de creare a mingii                    
def spawn_ball():                    
    global ball_pos, paddle_pos, ball_vel, gravity, drift                
    ball_pos = [width/2, 180]
    gravity = 0.5
    ball_vel = [0,0]
    drift = random.choice([-0.1, -0.05, -0.07, -0.02, 0.1, 0.05, 0.07, 0.02])                
    paddle_pos = 360                               
                    
def new_game():                    
    global score
    score = 0                
    spawn_ball()                
                    
def keydown(key):                    
    speed = 12
    global paddle_vel
    if key == simplegui.KEY_MAP["left"]:              
        paddle_vel -= speed                
    elif key == simplegui.KEY_MAP["right"]:                
        paddle_vel += speed 
                    
def keyup(key):                     
    speed = 12
    global paddle_vel
    if key == simplegui.KEY_MAP["left"]:              
        paddle_vel += speed                
    elif key == simplegui.KEY_MAP["right"]:                
        paddle_vel -= speed                    

# crearea frame-ului                    
frame = simplegui.create_frame("Bounce", width, height)                    
frame.set_draw_handler(draw)                    
frame.set_keydown_handler(keydown)     
frame.set_keyup_handler(keyup)                    
frame.set_canvas_background("Blue")                    
                    
# pornirea jocului                    
new_game()
frame.start()       