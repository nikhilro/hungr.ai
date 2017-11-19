import numpy


class Ball(object):
    def __init__(self, p, radius, fps, resolution):
        """ Takes coordinates of center and radius of the ball """
        self.radius = radius
        self.lastPos = None
        self.pos = p
        self.lastVel = None
        self.vel = None
        self.acc = None
        self.fps = fps
        self.resolution = resolution
        self.exists = False

    def update(self, p):
        """ Takes new location of the ball as a vector """
        self.exists = True

        if self.pos:
            self.lastPos = self.pos
        self.pos = p

        if self.vel:
            self.lastVel = self.vel

        self.vel = self.vel - self.lastVel
        self.vel = self.vel * self.fps

        if self.lastVel:
            self.acc = self.vel - self.lastVel
            self.acc = self.acc * self.fps
        return

    def bool(self):
        """ Determines the predicted location to make a decision to move"""
        if self.acc:
            predict = self._div_(self.vel, self.fps)
            predict = predict + self._div_(self.acc, 0.5 * (pow(self.fps, 2)))
            predict = predict + self.pos

            if predict.x <= self.resolution / 3 and predict.y - (2 / 5 * self.resolution) <= (
                    1 / 5 * self.resolution) and predict.y >= 0:
                return True
        else:
            return False

    def endCheck(self):
        if self.exists:
            self.exists = False
            return True
        else:
            return False

    def lastSeen(self):
        a = numpy.array(self.pos.x, self.pos.y)
        arr = []

        b = numpy.array(0, self.resolution/2)
        arr.append(numpy.linalg.norm(a-b))

        b = numpy.array(self.resolution/2, 0)
        arr.append(numpy.linalg.norm(a - b))

        b = numpy.array(self.resolution, self.resolution/2)
        arr.append(numpy.linalg.norm(a - b))

        b = numpy.array(self.resolution/2, self.resolution)
        arr.append(numpy.linalg.norm(a - b))

        return arr.index(min(arr))
