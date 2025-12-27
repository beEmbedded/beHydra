import sys
import os

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


# Import CODEC Class. Refer to https://beembedded.gitbook.io/behydra/automation-cli/python-apis for more details
from be_codec import CODEC

if __name__ == "__main__":
    CODEC.enable_input()