#print(-3)%3 = 0
#print(-2)%3 = 1
#print(-1)%3 = 2
#print 0%3 = 0
#print(1)%3 = 1
#print(2)%3 = 2
#print(3)%3 = 0


import random
import simplegui

scor_pc = 0
scor_om = 0
selectie_om = ""
selectie_pc = ""

# o sa ne treaca selectia noastra din string in int
def selectie_in_nr(selectie):
    if selectie == "piatra":
        selectie = 0
    elif selectie == "hartie":
        selectie = 1
    elif selectie == "foarfeca":
        selectie = 2
        
    return selectie

# ajuta pc ul sa aleaga una dintre piatra hartie sau foarfeca
def selectie_comp():
    # functia ne ajuta sa alegem o val random dintr-o lista
    return random.choice(['piatra', 'hartie', 'foarfeca'])

# care ne returneaza rez unei runde
def rezultat_selectie(selectie_pc, selectie_om):
    global scor_pc
    global scor_om
    
    nr_selectie_pc = selectie_in_nr(selectie_pc)
    nr_selectie_om = selectie_in_nr(selectie_om)
    
    if selectie_om == selectie_pc:
        print("Egalitate")
        
    elif (nr_selectie_pc - nr_selectie_om)%3 == 1:
        print("Calculatorul castiga!")
        scor_pc += 1
        
    else:
        print("Ai castigat!")
        scor_om += 1
        
#cream functia din spatele butonului pt piatra / hartie / foarfeca
def piatra():
    global selectie_om, selectie_pc
    global scor_om, scor_pc
    
    selectie_om = 'piatra'
    selectie_pc = selectie_comp()
    rezultat_selectie(selectie_pc, selectie_om)
    
def hartie():
    global selectie_om, selectie_pc
    global scor_om, scor_pc
    
    selectie_om = 'hartie';
    selectie_pc = selectie_comp()
    rezultat_selectie(selectie_pc, selectie_om)
    
def foarfeca():
    global selectie_om, selectie_pc
    global scor_om, scor_pc
    
    selectie_om = 'foarfeca';
    selectie_pc = selectie_comp()
    rezultat_selectie(selectie_pc, selectie_om)
    
# ne ajuta sa desenam pe ecran si dam ca param canvas
def draw(canvas):
    #deseneaza text, scrie pe ecran
    # param: 1 - textul care apare pe ecran
    # param: 2 - locul in care vrem sa pozitionam textul
    # param: 3 - dimensiunea textului
    # param: 4 - culoarea
    canvas.draw_text("Tu: " + selectie_om, [10,40], 48, "Green")
    canvas.draw_text("PC: " + selectie_pc, [10,80], 48, "Red")
    # text pentru scorul nostru
    canvas.draw_text("Scorul tau: " + str(scor_om), [10,150], 30, "Green") # trece scorul meu din int in string
    canvas.draw_text("Scorul PC: " + str(scor_pc), [10,190], 30, "Red")
    
# care ne ajuta sa rulam tot acest cod
def play_pfh():
    # cream ecranul / fereastra
    frame = simplegui.create_frame("PFH", 300, 200)
    # cream butoane
    frame.add_button("Piatra", piatra) # numele butonului, functia din spatele lui
    frame.add_button("Hartie", hartie)
    frame.add_button("Foarfeca", foarfeca)
    # se ocupa cu desenul
    frame.set_draw_handler(draw) 
    # ne creaza animatia
    frame.start()
    
play_pfh()
