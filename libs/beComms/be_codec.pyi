##########################################################
################### PUBLIC API'S #########################
# For further documentation, check: https://beembedded.gitbook.io/behydra/tools/automation-cli/python-apis/codec
##########################################################

class CODEC:
    """
    Interface for controlling the hardware CODEC (Analog-to-Digital and Digital-to-Analog Converters).
    """
    codecConfig: dict

    @classmethod
    def enable_adc(cls, inputId: int = 0) -> bool:
        """
        Enables the Analog-to-Digital Converter (ADC).

        Args:
            inputId (int): The Input Slot to allocate data to.
                0: Automatic allocation to any available slot.
                1: Force allocation to Slot 1.
                2: Force allocation to Slot 2.

        Returns:
            bool: True if enabled successfully. False if already enabled 
                  or if no slots are available.
        """
        ...

    # Enables the DAC (Digital-to-Analog Converter)
    # inputId: 0 for Line Out, 1 for Headphone Out (Hardware dependent)
    @classmethod
    def enable_dac(cls, inputId: int = 0) -> None: ...

    # Disables the ADC and stops any active analog capture
    @classmethod
    def disable_adc(cls) -> None: ...

    # Disables the DAC and stops any active analog playback
    @classmethod
    def disable_dac(cls) -> None: ...

    # Enables or disables the Noise Floor feature (Noise Gate)
    # enableNF: True to enable, False to disable
    @classmethod
    def enable_noiseFloor(cls, enableNF: bool) -> None: ...

    # Configures the ADC or DAC to the requested sample rate.
    # rate_Hz: Sample rate in Hz (e.g., 44100, 48000)
    # isSource: 0 for ADC (Input), 1 for DAC (Output)
    @classmethod
    def set_sampleRate(cls, rate_Hz: int, isSource: int = 0) -> None: ...

    # Sets the termination impedance/mode for the channel
    # termination: Value mapped to specific hardware impedance settings
    # isSource: 0 for ADC (Input), 1 for DAC (Output)
    @classmethod
    def set_termination(cls, termination: int, isSource: int = 0) -> None: ...

    # Sets the gain for the specified channel
    # gaindB: Gain value in decibels (dB)
    # isSource: 0 for ADC (Input), 1 for DAC (Output)
    @classmethod
    def set_gain(cls, gaindB: float, isSource: int = 0) -> None: ...
        
    # Selects the digital filter for the CODEC
    # filter: Integer ID representing the hardware filter preset
    # isSource: 0 for ADC (Input), 1 for DAC (Output)
    @classmethod
    def set_filter(cls, filter: int, isSource: int = 0) -> None: ...

    # Applies a full configuration dictionary to the CODEC
    # codecConfig: A dictionary containing all parameters (rate, gain, etc.)
    @classmethod
    def set_all(cls, codecConfig: dict) -> None: ...
    
    # Returns the current state (enabled/disabled) of the ADC
    @classmethod
    def get_inputState(cls) -> bool: ...
    
    # Returns the current state (enabled/disabled) of the DAC
    @classmethod
    def get_outputState(cls) -> bool: ...
    
    # Returns the current status of the Noise Floor configuration
    @classmethod
    def get_noiseFloorState(cls) -> bool: ...

    # Reads the current Sample Rate from the firmware
    # isSource: 0 for ADC (Input), 1 for DAC (Output)
    @classmethod
    def get_sampleRate(cls, isSource: int) -> int: ...

    # API to read the CODEC Gain from the FW
    # isSource: 0 for ADC (Input), 1 for DAC (Output)
    @classmethod
    def get_gain(cls, isSource: int) -> float: ...

    # API to read the CODEC Termination from the FW
    # isSource: 0 for ADC (Input), 1 for DAC (Output)
    @classmethod
    def get_termination(cls, isSource: int) -> int: ...

    # API to read the ADC Filter Selection from the FW
    # isSource: 0 for ADC (Input), 1 for DAC (Output)
    @classmethod
    def get_filter(cls, isSource: int) -> int: ...

    # API to read all current CODEC configurations from the FW as a dictionary
    @classmethod
    def get_all(cls) -> dict: ...
class CODEC:
    codecConfig dict

    # Enables the ADC
    @classmethod
    def enable_input(cls, inputId = 0): ...

    # Enables the DAC
    @classmethod
    def enable_output(cls, inputId = 0): ...

    # Disables the ADC
    @classmethod
    def disable_input(cls): ...

    # Disables the DAC
    @classmethod
    def disable_output(cls): ...

    @classmethod
    def enable_noiseFloor(cls, enableNF): ...

    # Configures the ADC or DAC to the requested sample rate.
    @classmethod
    def set_sampleRate(cls, rate_Hz, isSource = 0): ...

    @classmethod
    def set_termination(cls, termination, isSource = 0): ...

    @classmethod
    def set_gain(cls, gaindB, isSource = 0): ...
        
    @classmethod
    def set_filter(cls, filter, isSource = 0): ...

    @classmethod
    def set_all(cls, codecConfig): ...
    
    @classmethod
    def get_inputState(cls): ...
    
    @classmethod
    def get_outputState(cls): ...
    
    @classmethod
    def get_noiseFloorState(cls): ...

    @classmethod
    def get_sampleRate(cls, isSource): ...

    # API to read the CODEC Gain from the FW
    @classmethod
    def get_gain(cls, isSource): ...

    # API to read the CODEC Termination from the FW
    @classmethod
    def get_termination(cls, isSource): ...

    # API to read the ADC Filter Selection from the FW
    @classmethod
    def get_filter(cls, isSource): ...

    # API to read all the CODEC configurations from the FW
    @classmethod
    def get_all(cls): ...