import sounddevice as sd
import numpy as np
from scipy.fft import fft, fftfreq
from scipy.signal.windows import hann
import matplotlib.pyplot as plt

# Refer to https://beembedded.gitbook.io/behydra/automation-cli/python-apis for more details
from libs.beComms.be_codec import CODEC
from libs.beComms.be_usbAudio import USBAudio
from libs.beAudioProc import beAudioProcessing


def setup_AnalogTestPath():
    ### Input 1
    # Enable USB Audio as input to beHydra
    USBAudio.enable_input(1)
    # Enable Analogue as output to beHydra
    CODEC.enable_output(1)

    ### Input 2
    # Enable Analogue as input to beHydra
    CODEC.enable_input(2)
    # Enable USB Audio as output to beHydra
    USBAudio.enable_output(2)

def cleanUp_AnalogTestPath():
    # Disable all inputs and outputs
    USBAudio.disable_input()
    USBAudio.disable_output()
    CODEC.disable_input()
    CODEC.disable_output()
    


if __name__ == "__main__":
    print("Start Analogue Latency Measurement")

    # Setup the audio path for the test
    setup_AnalogTestPath()

    # Start the audio latency measurement test
    beAudioProcessing.measure_latency(duration_s=10, sampleRate_Hz=48000, samplingInterval_s=0.5)

    # Clean-up the audio path
    cleanUp_AnalogTestPath()