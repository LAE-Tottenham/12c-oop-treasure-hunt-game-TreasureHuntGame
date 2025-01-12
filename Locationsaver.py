class locationsaver():
    def __init__(self):
        self.location = "Home"
        self.current_locations_unlocked = []
        self.all_locations = []
        self.currentlocation = ""
    
    def currentlocationlogger(self, location_instance):
        self.currentlocation = location_instance

    def placeselectionchooser(self, selectionchoice):
        doneselection = False
        while doneselection == False:
            if selectionchoice in self.current_locations_unlocked:
                self.location = selectionchoice
                self.currentlocation = selectionchoice  # Update both
                doneselection = True
                print("You are now at " + selectionchoice)
            else:
                print("You have typed an invalid location.")
                selectionchoice = input("Please enter a valid location you would like to travel to. ")

    def locationinitialisation(self, location):
        self.current_locations_unlocked.append(location)
        self.currentlocation = location
            
    def location_unlocker(self, location, currentlocation):
        self.current_locations_unlocked.append(location.name)
        currentlocation = location
        print("You have unlocked " + location.name)
        return currentlocation
    
    def showlocation(self):
        print("The current locations you can travel to are:")
        print(self.current_locations_unlocked)

    def all_location_append(self, location_instance):
        self.all_locations.append(location_instance)