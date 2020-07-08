class Player(object):
    def __init__(self,coords,width,height,vel=5,left=False,right=False,front=True,back=False,still=True,walkCount=0):
        self.coords = coords
        self.width = width
        self.height = height
        self.vel = vel
        #for animations
        self.left = left
        self.right = right
        self.back = back
        self.front = front
        self.walkCount = walkCount
        self.still = still
    def get_animations(self,walkLeft,walkRight,walkFront,walkBack):
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        self.walkFront = walkFront
        self.walkBack = walkBack
    def set_hit_box(self,xdif,ydif,width,height):
        self.hit_box_x_dif = xdif
        self.hit_box_y_dif = ydif
        self.hit_box_width = width
        self.hit_box_height = height
        self.hit_box = (self.coords[0]+self.hit_box_x_dif,self.coords[1]+self.hit_box_y_dif,self.hit_box_width,self.hit_box_height)
    def draw(self,window,hitbox=False):
        if self.walkCount + 1 >= 2:
            self.walkCount = 0
        if self.left:
            window.blit(self.walkLeft[walkcount],(self.coords[0],self.coords[1]))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount],(self.coords[0],self.coords[1]))
            self.walkCount += 1
        elif self.front:
            window.blit(self.walkFront[self.walkCount],(self.coords[0],self.coords[1]))
            self.walkCount += 1
        elif self.back:
            window.blit(walkBack[self.walkCount],(self.coords[0],self.coords[1]))
            self.walkCount += 1
        self.hitbox = (self.coords[0]+self.hit_box_x_dif,self.coords[1]+self.hit_box_y_dif,hit_box_width,hit_box_height)
        if hitbox:
            pg.draw.rect(win,(255,0,0),self.hitbox,2)
class Projectile(object):
    def __init__(self,coords,height,width,sprite,facing,vel=20):
        self.coords = coords
        self.height = height
        self.width = width
        self.sprite = sprite
        self.facing = facing
        self.vel = vel        
    def draw(self,window):
        window.blit(self.sprite,(self.coords[0],slef.coords[1]))
class Enemy(object):
    def __init__(self,coords,height,width,sprite,facing,vel=5):
        self.coords = coords
        self.height = height
        self.width = width
        self.height = height
        self.sprite = sprite
        self.facing = facing
        self.vel = vel
    def get_sprite(self,leftWalk,rightWalk,backWalk,frontWalk,left=False,right=False,back=False,front=True):
        self.left = left
        self.right = right
        self.back = back
        self.front = front
        self.leftWalk = leftWalk
        self.rightWalk = rightWalk
        self.backWalk = backWalk
        self.frontWalk = frontWalk
    def set_hit_box(self,tlx,tly,width,height):
        self.hit_box_x_dif = tlx - self.x
        self.hit_box_y_dif = tly - self.y
        self.hit_box_width = width
        self.hit_box_height = height
        self.hit_box = (self.x+self.hit_box_x_dif,self.y+self.hit_box_y_dif,hit_box_width,hit_box_height)
    def draw(self,window,hitbox=False):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            window.blit(self.walkLeft[walkcount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.right:
            window.blit(walkRight[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.front:
            window.blit(self.walkFront[walkcount//3],(self.x,self.y))
            self.walkCount += 1
        elif self.back:
            window.blit(walkBack[self.walkCount//3],(self.x,self.y))
            self.walkCount += 1
        self.hitbox = (self.x+self.hit_box_x_dif,self.y+self.hit_box_y_dif,hit_box_width,hit_box_height)
        if hitbox:
            pg.draw.rect(win,(255,0,0),self.hitbox,2)