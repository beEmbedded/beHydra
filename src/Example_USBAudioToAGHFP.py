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
from be_bredr import BREDR
from be_usbAudio import USBAudio

if __name__ == "__main__":
    BREDR.set_sourceMode(1)
    
    # Configure the Audio Routing: USB Audio -> Bluetooth A2DP
    USBAudio.enable_input()
    BREDR.hfp.enable_output()
    
    # Pair with the first found Sink Device
    found_bdaddress = BREDR.start_scan()
    print(found_bdaddress[0]['bd_addr'])
    BREDR.pair_device_by_bdaddress(found_bdaddress[0]['bd_addr'])
    
    # Give time to the Sink device to settle
    time.sleep(15)

    # Initiate an incoming Call
    BREDR.hfp.call_initiate()

    # Accepts the incoming call
    BREDR.hfp.call_accept()

    # Play for 30 seconds the audio, before finishing the HFP call
    time.sleep(30)
    BREDR.hfp.call_terminate()