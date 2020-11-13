import random
class Task:
    """Represent a task, each task has between 1-20 pages, and arrive once
    every 180 seconds"""
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 20)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        """When a task enters the printer, it will return how much time was
        between the task entered the queue and the task went to the printer"""
        return currenttime - self.timestamp

