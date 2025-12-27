#############################################################################################
#############################################################################################
# For further documentation, check:
# https://beembedded.gitbook.io/behydra/tools/automation-cli/python-apis/i2s
#############################################################################################

class I2S:
    """
    Interface for controlling the Inter-IC Sound (I2S) digital audio protocol.
    Provides methods to configure sample rates, word widths, and hardware modes.
    """
    i2sConfig: dict

    @classmethod
    def enable_input(cls, inputId: int = 0) -> bool:
        """
        Enables the I2S Input.

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
        Enables the I2S Output.

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
        Disables the I2S Input and stops active digital capture.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...

    @classmethod
    def disable_output(cls) -> bool:
        """
        Disables the I2S Output and stops active digital playback.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...

    @classmethod
    def set_sampleRate(cls, rate_Hz: int, isSource: int = 0) -> bool:
        """
        Configures the I2S input or output to the requested sample rate.

        Args:
            rate_Hz (int): Sample rate in Hz (e.g., 44100, 48000, 96000).
            isSource (int): 0 for Input (Sink), 1 for Output (Source).

        Returns:
            bool: True if configuration was successful.
        """
        ...

    @classmethod
    def set_mode(cls, controller_mode: int, isSource: int = 0) -> bool:
        """
        Configures the I2S interface for Controller or Peripheral mode.

        Args:
            controller_mode (int): 
                0: Peripheral Mode (External Clock).
                1: Controller Mode (beHydra provides Clock).
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_wordWidth(cls, wordWidth: int, isSource: int = 0) -> bool:
        """
        Configure the word width (frame size) of the I2S interface.

        Args:
            wordWidth (int): Frame width in bits (e.g., 16, 24, 32, 48, 64).
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_bitDepth(cls, bitDepth: int, isSource: int = 0) -> bool:
        """
        Configure the actual audio data bit depth.

        Args:
            bitDepth (int): 16 or 24 bits.
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...
    
    @classmethod
    def set_lrJustify(cls, lrJustMode: int, isSource: int = 0) -> bool:
        """
        Sets the Left/Right Justification alignment.

        Args:
            lrJustMode (int): 
                0: I2S Standard (Left justified, delayed by 1 BCLK).
                1: Left Justified (No delay).
                2: Right Justified.
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...
    
    @classmethod
    def set_polarity(cls, polarity: int, isSource: int = 0) -> bool:
        """
        Sets the clock polarity (BCLK/LRCLK edge).

        Args:
            polarity (int): 0 for Normal, 1 for Inverted.
            isSource (int): 0 for Input, 1 for Output.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_voltageLvl(cls, voltageLevel: int) -> bool:
        """
        Sets the I2S digital interface voltage level.

        Args:
            voltageLevel (int): Typically 0 for 1.8V or 1 for 3.3V (Hardware dependent).

        Returns:
            bool: True if successful.
        """
        ...
    
    @classmethod
    def set_all(cls, i2sConfig: dict) -> bool:
        """
        Applies a complete configuration dictionary to the I2S module.

        Args:
            i2sConfig (dict): Dictionary containing all I2S parameters.

        Returns:
            bool: True if all settings were applied.
        """
        ...

    @classmethod
    def get_inputState(cls) -> bool:
        """Reads the current enabled/disabled state of the I2S Input."""
        ...

    @classmethod
    def get_outputState(cls) -> bool:
        """Reads the current enabled/disabled state of the I2S Output."""
        ...

    @classmethod
    def get_sampleRate(cls, isSource: int = 0) -> int:
        """Returns the current Sample Rate in Hz."""
        ...

    @classmethod
    def get_mode(cls, isSource: int = 0) -> int:
        """Returns 1 for Controller Mode, 0 for Peripheral Mode."""
        ...
    
    @classmethod
    def get_bitDepth(cls, isSource: int = 0) -> int:
        """Returns the current bit depth (16 or 24)."""
        ...

    @classmethod
    def get_voltageLvl(cls) -> int:
        """Reads the current I2S Voltage Level from the firmware."""
        ...

    @classmethod
    def get_all(cls) -> dict:
        """Retrieves all current I2S configurations as a dictionary."""
        ...