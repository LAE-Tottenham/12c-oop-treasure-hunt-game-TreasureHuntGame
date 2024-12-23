class locationsaver():
    def __init__(self):
        self.location = "Home"
        self.current_locations_unlocked = []

    # def change_location(self, changer):
    #     self.location = changer
    #     print("Your location is now" + changer)

    def placeselectionchooser(self, selectionchoice):
        doneselection = False
        while doneselection == False:
            if selectionchoice == "Home":
                self.location = "Home"
                doneselection = True
                print("Done")
            else:
                print("You have typed an invalid location")
                selectionchoice = input("Please enter a valid location you would like to travel to. ")

    def locationinitialisation(self,location):
        self.current_locations_unlocked.append(location)
            
    def location_unlocker(self, location):
        self.current_locations_unlocked.append(location)
        print("You have unlocked " + location)
    
    def showlocation(self):
        print("The current locations you can travel to are:")
        print(self.current_locations_unlocked)