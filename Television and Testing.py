#Create a class for the TV
class TV:
    #Make a constructor that has the default value of the channel and the volume which is 1 and an indicator which is turned off by default as its object.
    def __init__(self, channel = 1, volumeLevel = 1, on = False):
        self.channel = channel
        self.volumeLevel = volumeLevel
        self.on = on
    #Make a function when tv is turned on (Bool value changes)
    def turnOn(self, on):
        self.on = True
    #Make a function when tv is turned off (Bool value is still default)
    def turnOff(self, on):
        self.on = False
    #Make a function that retrieves the value of the variable "channel"  in order to get the Television Channel
    def getChannel(self, channel):
        return self.channel
    #Make a function to set the channel number that is equal or more than one and equal to or less than 120
    def setChannel(self, channel):
        if self.on and 1 <= channel <= 120:
            self.channel = channel
    #Make a function that retrieves the value of the variable "volumeLevel"  in order to get the volume of the television
    def getVolume(self, volumeLevel):
        return self.volumeLevel
    #Make a function to set the volume number that is equal or more than one and equal to or less than 7
    def setVolume(self, volumeLevel):
        if self.on and 1 <= volumeLevel <= 7:
            self.volumeLevel = volumeLevel
#Make a function to change to the next channel        
#Make a function to change to the previous channel    
#Make a function to make the volume higher      
#Make a function to lower the volume  
#Test the TV by creating a function with all of the function of the TV.
#Start the test function
