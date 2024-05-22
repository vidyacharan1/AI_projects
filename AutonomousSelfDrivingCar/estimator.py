import util 
from util import Belief, pdf 
from engine.const import Const
import math, collections, random

# Class: Estimator
#----------------------
# Maintain and update a belief distribution over the probability of a car being in a tile.
class Estimator(object):
    NUM_PARTICLES = 3000
    def __init__(self, numRows: int, numCols: int):
        self.belief = util.Belief(numRows, numCols) 
        self.transProb = util.loadTransProb()
        self.transProbDict = dict()
        for (x, y), prob in self.transProb.items():
            if x not in self.transProbDict:
                self.transProbDict[x] = collections.Counter()
            self.transProbDict[x][y] = prob

        self.particles = collections.Counter()
        part = list(self.transProbDict.keys())
        for i in range(self.NUM_PARTICLES):
            j = random.randint(0, len(part) - 1)
            self.particles[part[j]] += 1

        self.changeBelief()

    def changeBelief(self):
        self.belief = util.Belief(self.belief.getNumRows(), self.belief.getNumCols(), 0)
        for tile in self.particles:
            self.belief.setProb(tile[0], tile[1], self.particles[tile])
        self.belief.normalize()
    
    def randomWeighted(self, dict):
        total = sum(dict.values())
        r = random.uniform(0, total)
        curr = 0
        for k, v in dict.items():
            if curr + v >= r:
                return k
            curr += v
    
    ##################################################################################
    # [ Estimation Problem ]
    # Function: estimate (update the belief about a StdCar based on its observedDist)
    # ----------------------
    # Takes |self.belief| -- an object of class Belief, defined in util.py --
    # and updates it *inplace* based onthe distance observation and your current position.
    #
    # - posX: x location of AutoCar 
    # - posY: y location of AutoCar 
    # - observedDist: current observed distance of the StdCar 
    # - isParked: indicates whether the StdCar is parked or moving. 
    #             If True then the StdCar remains parked at its initial position forever.
    # 
    # Notes:
    # - Carefully understand and make use of the utilities provided in util.py !
    # - Remember that although we have a grid environment but \
    #   the given AutoCar position (posX, posY) is absolute (pixel location in simulator window).
    #   You might need to map these positions to the nearest grid cell. See util.py for relevant methods.
    # - Use util.pdf to get the probability density corresponding to the observedDist.
    # - Note that the probability density need not lie in [0, 1] but that's fine, 
    #   you can use it as probability for this part without harm :)
    # - Do normalize self.belief after updating !!

    ###################################################################################
    def estimate(self, posX: float, posY: float, observedDist: float, isParked: bool) -> None:
        # BEGIN_YOUR_CODE
            
        dct = collections.defaultdict(float)
        newParticles = collections.Counter()
        for tile in self.particles:
            for i in range(self.particles[tile]):  # if on that tile there're more particles, that tile is
            # an important start point
                newTile = self.randomWeighted(self.transProbDict[tile])
            # wherever newTile it lands, increase that counter.
                newParticles[newTile] += 1
        self.particles = newParticles

        for row, col in self.particles:
            dist = math.sqrt((util.colToX(col) - posX) ** 2 + (util.rowToY(row) - posY) ** 2)
            prob_distr = util.pdf(dist, Const.SONAR_STD, observedDist)
            dct[(row, col)] = self.particles[(row, col)] * prob_distr

        resampling = collections.Counter()
        for i in self.particles:
            for j in range(self.particles[i]):
                newtile = self.randomWeighted(dct)
                resampling[newtile] += 1
        self.particles = resampling
        self.changeBelief()
            
        # END_YOUR_CODE
        return

    def getBelief(self) -> Belief:
        return self.belief