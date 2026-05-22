# Refer to https://beembedded.gitbook.io/behydra/automation-cli/python-apis for more details
from beHydra.beComms.be_usbAudio import USBAudio
from beHydra.beComms.be_codec import CODEC

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

   