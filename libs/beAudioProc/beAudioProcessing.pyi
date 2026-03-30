##########################################################
################### PUBLIC API'S #########################
# For further documentation, check: https://beembedded.gitbook.io/behydra/tools/automation-cli/test-list
##########################################################

"""
Measure the Latency between the Left and the Right input channel (Analogue, I2S, PCM, etc) of beHydra.

Returns:
    list[float]: An array of latency values ms for each interval.
"""
def measure_latency(duration_s: int =10, sampleRate_Hz: int = 48000, samplingInterval_s: float = 0.5) -> list[float]: ...