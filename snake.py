import tkinter
import random


ROWS = 25
COL = 25
TITLE_SIZE = 25

WINDOW_WIDTH = TITLE_SIZE*ROWS
WINDOW_HEIGHT = TITLE_SIZE*COL

class Title:
    def __init__(self, x, y):
      self.x = x
      self.y = y

#game window
TITLE_SIZE = 20
window=tkinter.Tk()
window.title("snake")
window.resizable(False, False) 


canvas=tkinter.Canvas(window, bg="black", width=WINDOW_WIDTH, height=WINDOW_HEIGHT, borderwidth=0, highlightthickness=0)
canvas.pack()
window.update()

#center the window


screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_width = window.winfo_width()
window_height = window.winfo_height()

window_x = int((screen_width / 2) - (window_width / 2))
window_y = int((screen_height / 2) - (window_height / 2))
#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initialize game
snake = Title(5*TITLE_SIZE, 5*TITLE_SIZE)
food = Title(10*TITLE_SIZE, 10*TITLE_SIZE)
snake_body = [] #multiple bodyparts
velocityX = 0
velocityY = 0
game_over = False
score = 0

def change_direction(e): #e = event
    #print(e)
    #print(e.keysym)
    global velocityX, velocityY, game_over
    if (game_over):
        return


    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0
    
def move():
    global snake, food, snake_body, game_over, score
    if (game_over):
        return
    
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        return
    
    for title in snake_body:
        if (snake.x == title.x and snake.y == title.y):
            game_over = True
            return
        
    #collision
    if (snake.x == food.x and snake.y == food.y):
        snake_body.append(Title(food.x, food.y))
        food.x = random.randint(0, COL-1) * TITLE_SIZE
        food.y = random.randint(0, ROWS-1) * TITLE_SIZE
        score += 1
    #update snake body
    for i in range(len(snake_body)-1, -1, -1):
        title = snake_body[i]
        if (i == 0):
            title.x = snake.x
            title.y = snake.y
        else:
            prev_title = snake_body[i-1]
            title.x = prev_title.x
            title.y = prev_title.y

    snake.x += velocityX * TITLE_SIZE
    snake.y += velocityY * TITLE_SIZE
 # start drawing loop
def draw():
    global snake, food, snake_body, game_over
    move()

    canvas.delete("all")

    # draw food
    canvas.create_rectangle(food.x, food.y, food.x + TITLE_SIZE, food.y + TITLE_SIZE, fill="red")

    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TITLE_SIZE, snake.y + TITLE_SIZE, fill="green")

    for title in snake_body:
        canvas.create_rectangle(title.x, title.y, title.x + TITLE_SIZE, title.y + TITLE_SIZE, fill="green")
     
    if (game_over):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_WIDTH/2, font = "Arial 20", text = f"Game Over: {score}", fill="white")
    else:
        canvas.create_text(30, 20, font = "Arial 10", text = f"score: {score}", fill = "white")
    window.after(100, draw)

draw()

window.bind("<KeyRelease>", change_direction)
window.mainloop()