class GameObject:
    def __init__(self, dimentions, position, velocity, maxSpeed):
        self.x,self.y = position
        self.xSize,self.ySize = dimentions
        self.velocity = velocity
        self.MAXSPEED = maxSpeed
    
    def move(self, bounds, hardStop):
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        collisions = [self.x > bounds[0],self.x < 0,self.y > bounds[1],self.y < 0]
        if collisions[0]: self.x = bounds[0]
        if collisions[1]: self.x = 0
        if collisions[2]: self.y = bounds[1]
        if collisions[3]: self.y = 0

        if True in collisions: 
            if hardStop: self.velocity = (0,0)
            else: self.velocity = (self.velocity[0], -self.velocity[1])

        return collisions

    def changeVelocity(self, diff):
        self.velocity = (self.velocity[0] + diff[0], self.velocity[1] + diff[1])
        if self.velocity[0] > self.MAXSPEED: self.velocity = (self.MAXSPEED, self.velocity[1])
        if self.velocity[0] < -self.MAXSPEED: self.velocity = (-self.MAXSPEED, self.velocity[1])
        if self.velocity[1] > self.MAXSPEED: self.velocity = (self.velocity[0], self.MAXSPEED)
        if self.velocity[1] < -self.MAXSPEED: self.velocity = (self.velocity[0], -self.MAXSPEED)
    
    def getYVelocity(self):
        if self.velocity[1] < 0: return -self.velocity[1]
        return self.velocity[1]

    def checkCollision(self, pos1, pos2):
        if pos1[0] <= self.x+self.xSize and pos2[0] >= self.x-self.xSize: 
            crossPoint = pos1[1] + (self.x - pos1[0])*(pos1[1]-pos2[1])/(pos1[0]-pos2[0])
            if crossPoint >= self.y-self.ySize/2 and crossPoint <= self.y+self.ySize/2:
                return True
        return False

    def nextPos(self):
        return (self.x + self.velocity[0], self.y + self.velocity[1])
    
    def reverse(self):
        self.velocity = (-self.velocity[0], self.velocity[1])

    def toString(self):
        return f"Size: {(self.xSize, self.ySize)} Position: {(self.x, self.y)} Velocity: {self.velocity}"
