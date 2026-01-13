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


# Refer to https://beembedded.gitbook.io/behydra/automation-cli/python-apis for more details
from be_usbAudio import USBAudio
from be_codec import CODEC

if __name__ == "__main__":
    """
    This example uses beHydra to play audio from its analogue outputs as a 
    normal USB Audio souncards.
    A simplified audio stream diagram can be found below:
    USB Audio   ->  Analogue Output
    """
    
    # Configure the Audio Routing: USB Audio -> Analogue Output
    USBAudio.enable_input(1)
    CODEC.enable_output(1)

   