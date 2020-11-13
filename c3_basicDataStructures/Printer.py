class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        """Decreases by a second each call. Resets to None when reaches 0."""
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        """Returns if the printer is busy."""
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        """Starts a new task from the queue, setting a remaining time."""
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate

