#############################################################################################
#############################################################################################
# For further documentation, check:
# https://beembedded.gitbook.io/behydra/tools/automation-cli/python-apis/pdm
#############################################################################################
class PDM:
    """
    Interface for controlling the Pulse Density Modulation (PDM) digital audio protocol.
    Typically used for Digital Microphones (DMIC) and digital speaker interfaces.
    """
    pdmConfig: dict

    @classmethod
    def enable_input(cls, inputId: int = 0) -> bool:
        """
        Enables the PDM Input (Digital Microphone capture).

        Args:
            inputId (int): The Input Slot to allocate data to.
                0: Automatic allocation to any available slot.
                1: Force allocation to Input Slot 1.
                2: Force allocation to Input Slot 2.

        Returns:
            bool: True if enabled successfully. False if already enabled or no slots available.
        """
        ...

    @classmethod
    def enable_output(cls, inputId: int = 0) -> bool:
        """
        Enables the PDM Output.

        Args:
            inputId (int): The Output Slot to allocate data to.
                0: Automatic allocation to any available slot.
                1: Force allocation to Output Slot 1.
                2: Force allocation to Output Slot 2.

        Returns:
            bool: True if enabled successfully. False if already enabled or no slots available.
        """
        ...

    @classmethod
    def disable_input(cls) -> bool:
        """
        Disables the PDM Input.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...

    @classmethod
    def disable_output(cls) -> bool:
        """
        Disables the PDM Output.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...
        
    @classmethod
    def set_sampleRate(cls, rate_Hz: int, isSource: int = 0) -> bool:
        """
        Configures the PDM Input or Output to the requested audio sample rate.

        Args:
            rate_Hz (int): Sample rate in Hz (e.g., 16000, 44100, 48000).
            isSource (int): 0 for Input (Sink), 1 for Output (Source).

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_clockRate(cls, rate_Hz: int, isSource: int = 0) -> bool:
        """
        Configures the PDM Clock Rate (DMIC Clock).

        Args:
            rate_Hz (int): Clock frequency in Hz (e.g., 768000, 1536000, 3072000).
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_filter(cls, filterSel: int, isSource: int = 0) -> bool:
        """
        Selects the hardware decimation/interpolation filter for the PDM signal.

        Args:
            filterSel (int): Integer ID for the hardware filter preset.
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_gain(cls, gain_dB: float, isSource: int = 0) -> bool:
        """
        Sets the digital gain for the PDM channel.

        Args:
            gain_dB (float): Gain value in decibels (dB).
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_chanSwap(cls, chanSwap: int, isSource: int = 0) -> bool:
        """
        Configures the DMIC Channel Swap.

        Args:
            chanSwap (int): 
                0: Normal (Left/Right as defined by hardware edges).
                1: Swapped (Swap Left and Right data).
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...
    
    @classmethod
    def set_voltageLvl(cls, voltageLevel: int, isSource: int = 0) -> bool:
        """
        Sets the PDM interface voltage level.

        Args:
            voltageLevel (int): 
                0: 1.8V
                1: 3.3V
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_all(cls, pdmConfig: dict) -> bool:
        """
        Applies a complete configuration dictionary to the PDM module.

        Args:
            pdmConfig (dict): Complete configuration set.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def get_inputState(cls) -> bool:
        """Returns True if PDM Input is currently enabled."""
        ...

    @classmethod
    def get_outputState(cls) -> bool:
        """Returns True if PDM Output is currently enabled."""
        ...

    @classmethod
    def get_sampleRate(cls, isSource: int = 0) -> int:
        """Retrieves the current Sample Rate from the firmware."""
        ...

    @classmethod
    def get_clockRate(cls, isSource: int = 0) -> int:
        """Retrieves the current DMIC Clock Rate from the firmware."""
        ...

    @classmethod
    def get_chanSwap(cls, isSource: int = 0) -> int:
        """Returns the current channel swap status (0 or 1)."""
        ...

    @classmethod
    def get_voltageLvl(cls) -> int:
        """Reads the current PDM Voltage Level from the firmware."""
        ...
    
    @classmethod
    def get_all(cls) -> dict:
        """Retrieves all current PDM configurations as a dictionary."""
        ...