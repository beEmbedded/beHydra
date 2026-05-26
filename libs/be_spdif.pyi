#############################################################################################
#############################################################################################
# For further documentation, check:
# https://beembedded.gitbook.io/behydra/tools/automation-cli/python-apis/spdif
#############################################################################################
class SPDIF:
    """
    Interface for Sony/Philips Digital Interface (SPDIF).
    Controls digital audio transmission over optical or coaxial hardware.
    """
    spdifConfig: dict

    @classmethod
    def enable_input(cls, inputId: int = 0) -> bool:
        """
        Enables the SPDIF Input (Receiver).

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
        Enables the SPDIF Output (Transmitter).

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
        Disables the SPDIF Input and stops active digital capture.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...

    @classmethod
    def disable_output(cls) -> bool:
        """
        Disables the SPDIF Output and stops active digital playback.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...

    @classmethod
    def set_sampleRate(cls, rate_Hz: int, isSource: int = 0) -> bool:
        """
        Configures the SPDIF input or output to the requested sample rate.

        Args:
            rate_Hz (int): Supported rates: 44100, 48000, 88200, 96000, 176400, 192000.
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if configuration was successful.
        """
        ...
    
    @classmethod
    def set_sampleSize(cls, sampleSize: int, isSource: int = 0) -> bool:
        """
        Configures the word length (bit depth) of the SPDIF stream.

        Args:
            sampleSize (int): Bit depth, typically 16 or 24 bits.
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_voltageLvl(cls, voltageLevel: int) -> bool:
        """
        Sets the SPDIF digital interface voltage level.

        Args:
            voltageLevel (int): 
                0: 1.8V
                1: 3.3V

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_all(cls, spdifConfig: dict) -> bool:
        """
        Applies a complete configuration dictionary to the SPDIF module.

        Args:
            spdifConfig (dict): Complete configuration set.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def get_inputState(cls) -> bool:
        """Reads the current enabled/disabled state of the SPDIF Input."""
        ...

    @classmethod
    def get_outputState(cls) -> bool:
        """Reads the current enabled/disabled state of the SPDIF Output."""
        ...

    @classmethod
    def get_sampleRate(cls, isSource: int = 0) -> int:
        """
        Reads the current Sample Rate from the firmware.

        Args:
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            int: Sample rate in Hz.
        """
        ...
    
    @classmethod
    def get_sampleSize(cls, isSource: int = 0) -> int:
        """
        Reads the current Sample Size (Bit Depth) from the firmware.

        Args:
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            int: 16 or 24.
        """
        ...

    @classmethod
    def get_voltageLvl(cls) -> int:
        """Reads the current SPDIF Voltage Level from the firmware (0 for 1.8V, 1 for 3.3V)."""
        ...

    @classmethod
    def get_all(cls) -> dict:
        """Retrieves all current SPDIF configurations from the firmware."""
        ...