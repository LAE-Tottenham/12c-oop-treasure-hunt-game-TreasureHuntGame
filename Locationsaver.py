from place import Place

class locationsaver():
    def __init__(self):
        self.location = "Home"
        self.current_locations_unlocked = []
        self.all_locations = []
        self.currentlocation = ""
    
    def currentlocationlogger(self, location_instance):
        self.currentlocation = location_instance

    def placeselectionchooser(self, selectionchoice):
        for location in self.all_locations:
            if location.name.lower() == selectionchoice.lower():
                if location.name in self.current_locations_unlocked:
                    self.location = location.name
                    self.currentlocation = location
                    print(f"You have arrived at {location.name}.")
                    if not location.storycompletion and hasattr(location, "story"):
                        location.story()
                        location.storycompletion = True
                    return location
                else:
                    print(f"{location.name} is currently locked.")
                    return self.currentlocation
        print(f"Invalid selection: {selectionchoice}")
        return self.currentlocation
    
    def locationinitialisation(self, location):
        self.current_locations_unlocked.append(location)
        self.currentlocation = location
            
    def location_unlocker(self, location, currentlocation):
        if not isinstance(location, Place):  # Check if location is a Place object
            raise TypeError(f"Expected a Place object, but got {type(location).__name__}.")
        
        self.current_locations_unlocked.append(location.name)
        currentlocation = location
        print(f"You have unlocked {location.name}.")
        return currentlocation

    
    def showlocation(self):
        print("The current locations you can travel to are:")
        print(self.current_locations_unlocked)

    def all_location_append(self, location_instance):
        self.all_locations.append(location_instance)