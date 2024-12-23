class locationsaver():
    def __init__(self, location):
        self.location = location

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