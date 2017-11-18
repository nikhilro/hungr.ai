import math

class Ball(object):
    def __init__(self, p, radius, fps, reso):
        """ Takes coordinates of center and radius of the ball """
        self.radius = radius
        self.lastPos = None
        self.pos = p
        self.lastVel = None
        self.vel = None
        self.acc = None
        self.fps = fps
        self.reso = reso

    def update(self, p):
        """ Takes new location of the ball as a vector """
        if self.pos:
            self.lastPos = self.pos
        self.pos = p

        if self.vel:
            self.lastVel = self.vel

        self.vel = self.__sub__(self.vel,self.lastVel)
        self.vel = self._rmul_(self.vel,self.fps)

        if self.lastVel:
            self.acc = self._sub_(self.vel,self.lastVel)
            self.acc = self._rmul_(self.acc, self.fps)
        return

    def bool(self):
        """Determines the predicted location to make a decision to move"""
        if  self.acc:
            predict = self._div_(self.vel, ffs)
            predict = self._add_(predict, self._div_(self.acc,0.5*(pow(ffs,2))))
            predict = self._add_(self.pos, predict)

            if predict.x <= reso/3 && predict.y - (2/5*reso) <= (1/5*reso) && predict.y >= 0:
                return true
        else:
            return false

