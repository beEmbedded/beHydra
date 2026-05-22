import time

# Refer to https://beembedded.gitbook.io/behydra/automation-cli/python-apis for more details
from beHydra.beComms.be_bredr import BREDR
from beHydra.beComms.be_usbAudio import USBAudio

if __name__ == "__main__":
    BREDR.set_sourceMode(1)
    
    # Configure the Audio Routing: USB Audio -> Bluetooth A2DP
    USBAudio.enable_input()
    BREDR.a2dp.enable_output()

    # Configure the A2DP Codec support
    """ 
    Bit 0: SBC (Always Enabled)
    Bit 1: AAC
    Bit 2: aptX Classic
    Bit 3: aptX HD
    Bit 4: aptX Adaptive
    """
    BREDR.set_audioCodecs(0x1)
    
    # Pair with the Sink Device
    #found_bdaddress = BREDR.start_scan()
    #print(found_bdaddress[0]['bd_addr'])
    #BREDR.pair_device_by_bdaddress(found_bdaddress[0]['bd_addr'])
    BREDR.pair_device_by_bdaddress("0x00025B00FF00")
    
    # Give time to the Sink device to settle
    time.sleep(15)

    # Start the A2DP stream
    BREDR.a2dp.play()

    # Play for 30 seconds the audio, before stopping the A2DP
    time.sleep(30)
    BREDR.a2dp.stop()