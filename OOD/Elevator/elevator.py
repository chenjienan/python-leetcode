class Direction:
    UP = 'UP'
    DOWN = 'DOWN'

class Status:
    UP = 'UP'
    DOWN = 'DOWN'
    IDLE = 'IDLE'

class Request:
    def __init__(self,l = 0):
        self.level = l
        
    def getLevel(self):
        return self.level

class ElevatorButton:
    def __init__(self,level,e):
        self.level = level
        self.elevator = e
        
    def pressButton(self):
        request = InternalRequest(self.level)
        self.elevator.handleInternalRequest(request);

class ExternalRequest(Request):
    def __init__(self,l = 0,d = None):
        Request.__init__(self,l)
        self.direction = d

    def getDirection(self):
        return self.direction

class InternalRequest(Request):
    def __init__(self,l = None):
        Request.__init__(self,l)

class Elevator:
    def __init__(self, n):
        # Keep them, don't modify.
        self.buttons = []
        self.upStops = []
        self.downStops = []
        for i in xrange(n):
            self.upStops.append(False)
            self.downStops.append(False)
        self.currLevel = 0
        self.status = Status.IDLE

    def insertButton(self,eb):
        self.buttons.append(eb)

    def handleExternalRequest(self,r):
        # Write your code here  
    	if r.getDirection() == Direction.UP:
			self.upStops[r.getLevel() - 1] = True
			if self.noRequests(self.downStops):
				self.status = Status.UP
        else:
			self.downStops[r.getLevel() - 1] = True
			if self.noRequests(self.upStops):
				self.status = Status.DOWN
        
    def handleInternalRequest(self,r):
		# Write your code here
		if self.status == Status.UP:
			if r.getLevel() >= self.currLevel + 1:
				self.upStops[r.getLevel() - 1] = True

		elif self.status == Status.DOWN:
			if r.getLevel() <= self.currLevel + 1:
				self.downStops[r.getLevel() - 1] = True
        
    def openGate(self):
		# Write your code here
		if self.status == Status.UP:
		    for i in xrange(len(self.upStops)):
		        checkLevel = (self.currLevel + i) % len(self.upStops)
		        if self.upStops[checkLevel]:
		            self.currLevel = checkLevel
		            self.upStops[checkLevel] = False
		            break

		elif self.status == Status.DOWN:
			for i in xrange(len(self.downStops)):
			    checkLevel = (self.currLevel + len(self.downStops) - i) % len(self.downStops)
			    if self.downStops[checkLevel]:
			        self.currLevel = checkLevel
			        self.downStops[checkLevel] = False
			        break
        
    def closeGate(self):
		# Write your code here  
		if self.status == Status.IDLE:
			if self.noRequests(self.downStops):
				self.status = Status.UP
				return
			
			if self.noRequests(self.upStops):
				self.status = Status.DOWN
				return

		elif self.status == Status.UP:
			if self.noRequests(self.upStops):
				if self.noRequests(self.downStops):
					self.status = Status.IDLE
				else:
				    self.status = Status.DOWN
		else:
			if self.noRequests(self.downStops):
				if self.noRequests(self.upStops):
					self.status = Status.IDLE
				else:
				    self.status = Status.UP

    def noRequests(self, stops):
		for stop in stops:
		    if stop:
		        return False
		return True
	
    def elevatorStatusDescription(self):
        description = "Currently elevator status is : " + self.status + \
                      ".\nCurrent level is at: " + str(self.currLevel + 1) + \
                      ".\nup stop list looks like: " + self.toString(self.upStops) + \
                      ".\ndown stop list looks like:  " + self.toString(self.downStops) + \
                      ".\n*****************************************\n"
        return description
        
    @classmethod
    def toString(cls, stops):
        return str(stops).replace("False", "false").replace("True", "true")