import tkinter as tk
from GameObject import GameObject
from PIL import ImageTk, Image

PLAYER = 0
OPPONENENT = 1
BALL = 2

class GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Pong")
        self.frame = tk.Frame(self.window)
        self.frame.pack()
        self.canvas = tk.Canvas(self.frame, width=400, height=300, background="black")
        self.canvas.pack()

    def update(self, score, playerObj, opponentObj, ballObj):
        self.canvas.delete('all')

        self.canvas.create_rectangle(playerObj.x-playerObj.xSize/2, playerObj.y-playerObj.ySize/2,playerObj.x+playerObj.xSize/2,playerObj.y+playerObj.ySize/2,
                                     outline="white", fill="white", width=2)
        self.canvas.create_rectangle(opponentObj.x-opponentObj.xSize/2, opponentObj.y-opponentObj.ySize/2,opponentObj.x+opponentObj.xSize/2,opponentObj.y+opponentObj.ySize/2,
                                     outline="white", fill="white", width=2)
        self.canvas.create_rectangle(ballObj.x-ballObj.xSize/2, ballObj.y-ballObj.ySize/2,ballObj.x+ballObj.xSize/2,ballObj.y+ballObj.ySize/2,
                                     outline="white", fill="white", width=2)
        
        self.canvas.create_text(200, 20, text=f"{score[0]}:{score[1]}",fill="white", font="Helvetica 32")

        self.window.update()
    
    def gameOver(self, score):
        self.canvas.create_text(200, 200, text="GAME OVER\nSCORE: {}:{}".format(score[0],score[1]), fill="white", font="Helvetica 20")
        self.window.update()

    def gameStart(self):
        arrowKeys = ImageTk.PhotoImage(self.arrowKeysImg)
        self.canvas.create_text(200, 100, text="PONG", fill="white", font="Helvetica 20")
        self.canvas.create_image((200, 200), image=arrowKeys)
        self.canvas.create_text(200, 300, text="UP and DOWN to move paddle\nSPACE to pause\nDon't let the ball get past you", fill="white", font="Helvetica 16")
        self.window.update()


if __name__ == "__main__":
    gui = GUI()
    gui.window.mainloop()