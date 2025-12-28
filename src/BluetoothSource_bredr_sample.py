import sys
import os
import time

# Get the current directory: beAutoTesting
current_directory = os.path.dirname(os.path.abspath(__file__))
# Get the parent directory: beHydra_GUI
parent_directory = os.path.dirname(current_directory)
# Add the beUsbUtils directory
be_comms_dir = os.path.join(parent_directory, 'libs\\beComms')
# Append the parent directory to the sys.path to include in the search path
sys.path.append(parent_directory)
# Append the beComms directory
sys.path.append(be_comms_dir)


# Import BREDR Class. Refer to https://beembedded.gitbook.io/behydra/automation-cli/python-apis for more details
from be_bredr import BREDR
from be_codec import CODEC
from be_usbAudio import USBAudio


def initiateAndAcceptHfpCall():
    ### Configure the Audio Streams
    # Analogue (mic) -> SCO Tx (mic path)
    CODEC.enable_input(1)               # Configures Input 1 to be Analogue Input
    BREDR.hfp.enable_output(1)          # Configures Output 1, of Input 1, to be HFP Type
    # SCO Rx (speaker path) -> Analogue (Speaker)
    BREDR.hfp.enable_input(2)           # Configures Input 2 to be HFP Type
    CODEC.enable_output(2)              # Configures Output 1, of Input 2, to be Analogue Output
    ###
    

    # Initiate the Incoming Call
    BREDR.hfp.call_initiate()           # Triggers the call to start
    # Accept the call
    BREDR.hfp.call_accept()             # Accepts the call

def terminateHFPCall():
    BREDR.hfp.call_terminate()          # Ends the call

    # Clean-up the audio routing
    CODEC.disable_input()
    CODEC.disable_output()
    BREDR.hfp.disable_input()
    BREDR.hfp.disable_output()


def startA2DPStream():
    ### Configure the Audio Streams
    # Analogue (mic) -> A2DP (source)
    CODEC.enable_input(1)               # Configures Input 1 to be Analogue Input
    #USBAudio.enable_rx(1)
    BREDR.a2dp.enable_output(1)         # Configures Output 1, of Input 1, to be A2DP Type
    ###

    # Initiate the Call
    BREDR.a2dp.play()                   # Triggers the A2DP stream to start


def terminateA2DPStream():
    BREDR.a2dp.stop()                   # Stops the A2DP stream  

    # Clean-up the audio routing
    CODEC.disable_input()
    BREDR.a2dp.disable_output()


############################# Overview #############################
# beHydra routes audio from its inputs to its outputs.
# The protocols used at the inputs and outputs are user configurable.
# Each protocol can be individually configured to meeet the user requirements.
if __name__ == "__main__":
    # Set the device in Source Mode. Only needs to be done once after power-on.
    #BREDR.set_sourceMode(1)
    
    example_bd_address = '0x123456789123'                       # BD Address Example
    #found_bdaddress = BREDR.start_scan()                       # Scans for pairing devices nearby
    # Prints all the relevant information and prints the BD Address of the first device found
    #print("Info on found device:", found_bdaddress, "bd_addr:", found_bdaddress[0]['bd_addr'])   
    #BREDR.pair_device_by_bdaddress(example_bd_address)          # Requests beHydra to pair with a device with the given BD Address

    # Start an HFP Call
    #initiateAndAcceptHfpCall()                                  # Starts an HFP call and accepts it (terminate any A2DP stream before starting HFP)
    #time.sleep(10)
    #terminateHFPCall()                                         # Stops the HFP Call and cleans up the audio routing
    CODEC.enable_input(1)

    # Start an A2DP Stream
    #startA2DPStream()                                          # Starts an A2DP stream (terminate any HFP call before starting A2DP)
    #time.sleep(10)
    #terminateA2DPStream()                                      # Stops the A2DP Stream and cleans up the audio routing