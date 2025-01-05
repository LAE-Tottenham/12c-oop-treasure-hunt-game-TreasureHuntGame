from Locationsaver import locationsaver
from main import locationsaverentity

class Storysaver:
    def __init__(self):
        pass

    def progressmarker(self,percentage):
        self.percentage = percentage
        if self.percentage == 100:
            print("You have completed the story quest at this location")
            locationsaverentity.location_unlocker()
            