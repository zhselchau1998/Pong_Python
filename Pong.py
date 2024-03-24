from codecs import backslashreplace_errors
from KeyListener import KeyListener
from GameObject import GameObject
from GUI import GUI
from time import sleep
from random import randint

HEIGHT,WIDTH = 300, 400

MAX_BALL_SPEED = 30
MAX_PADDLE_SPEED = 30

PADDLE_ACCEL = 3


class Pong:
    def __init__(self):
        self.keyboard = KeyListener()
        self.ball = GameObject((2,2), (WIDTH/2, HEIGHT/2), (5,3), MAX_BALL_SPEED)
        self.player = GameObject((2,30), (20,HEIGHT/2), (0,0), MAX_PADDLE_SPEED)
        self.opponent = GameObject((2,30), (WIDTH-20,HEIGHT/2), (0,0), MAX_PADDLE_SPEED)
        self.score = [0,0]
    
    def resetBall(self, newV):
        self.ball.x = WIDTH/2
        self.ball.y = HEIGHT/2
        self.ball.velocity = newV

    def startGame(self):
        self.GUI = GUI()
        inGame = True
        while(inGame):
            inGame = self.gameCycle()
            sleep(0.1)

    def gameCycle(self):
        self.GUI.update(self.score, self.player, self.opponent, self.ball)

        # Player Controls
        inputs = self.keyboard.getKeys()
        if 's' in inputs: self.player.changeVelocity((0,max(1,PADDLE_ACCEL*self.player.getYVelocity()/MAX_PADDLE_SPEED)))
        if 'w' in inputs: self.player.changeVelocity((0,min(-1,-PADDLE_ACCEL*self.player.getYVelocity()/MAX_PADDLE_SPEED)))

        # Opponent AI
        if self.ball.y > self.opponent.y: self.opponent.changeVelocity((0,max(1,PADDLE_ACCEL*
                                                                              (self.ball.y-self.opponent.y-self.opponent.getYVelocity()/PADDLE_ACCEL)*
                                                                              self.opponent.getYVelocity()/(MAX_PADDLE_SPEED/2))))
        if self.ball.y < self.opponent.y: self.opponent.changeVelocity((0,min(-1,-PADDLE_ACCEL*
                                                                               (self.ball.y-self.opponent.y-self.opponent.getYVelocity()/PADDLE_ACCEL)*
                                                                              self.opponent.getYVelocity()/(MAX_PADDLE_SPEED/2))))

        # Move all objects
        self.player.move((WIDTH, HEIGHT), True)
        self.opponent.move((WIDTH, HEIGHT), True)
        self.ball.move((WIDTH, HEIGHT), False)

        # Check for collisions
        ballPos = (self.ball.x,self.ball.y)
        nextBallPos = self.ball.nextPos()
        if (self.player.checkCollision(nextBallPos, ballPos)):
            self.ball.reverse()
            self.ball.changeVelocity((2, self.player.velocity[1]))
        if (self.opponent.checkCollision(ballPos, nextBallPos)):
            self.ball.reverse()
            self.ball.changeVelocity((-2, self.player.velocity[1]))

        # Check for points
        if self.ball.x <= 10: 
            self.score[1] += 1
            self.resetBall((-5,randint(-5,5)))

        if self.ball.x >= WIDTH-10: 
            self.score[0] += 1
            self.resetBall((5,randint(-5,5)))

        return True

if __name__ == "__main__":
    game = Pong()
    game.startGame()
