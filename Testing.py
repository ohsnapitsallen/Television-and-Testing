#Call the television python file
from Television import *

#Create a function to test the RV
def main():
    #TV1 will be used for increasing the volume and scrolling up the channels
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(28)
    tv1.channelUp()
    tv1.channelUp()
    tv1.volumeUp()
    tv1.volumeUp()
    #Print the final channel and volume of tv1
    print("tv1's channel is", tv1.getChannel(), "and volume level is", tv1.getVolume())

    #TV2 will be used for decreasing the volume and scrolling down the channels
    tv2 = TV()
    tv2.turnOn()
    tv2.setChannel(5)
    tv2.channelDown()
    tv2.channelDown()
    tv2.setVolume(5)
    tv2.volumeDown()
    tv2.volumeDown()
    tv2.volumeDown()
    #Print the final channel and volume of tv2
    print("tv2's channel is", tv2.getChannel(), "and volume level is", tv2.getVolume())
#Create a function to test the TV
#TV1 will be used for increasing the volume and scrolling up the channels
#Print the final channel and volume of tv1
#TV2 will be used for decreasing the volume and scrolling down the channels
#Print the final channel and volume of tv2
#Start the test function
