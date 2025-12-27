#############################################################################################
#############################################################################################
# For further documentation, check:
# https://beembedded.gitbook.io/behydra/tools/automation-cli/python-apis/usb-audio
#############################################################################################
class USBAudio:
    """
    Interface for controlling USB Audio Class (UAC) functionality.
    Allows the beHydra to act as a USB Soundcard for a Host PC or Mobile device.
    """
    usbAudioRx_config: dict
    usbAudioTx_config: dict

    @classmethod
    def enable_input(cls, inputId: int = 0) -> bool:
        """
        Enables the USB Rx Audio (Host to beHydra).

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
        Enables the USB Tx Audio (beHydra to Host).

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
        Disables the USB Input (Rx) Audio stream.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...

    @classmethod
    def disable_output(cls) -> bool:
        """
        Disables the USB Output (Tx) Audio stream.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...

    @classmethod
    def set_sampleRate(cls, rate_Hz: int, isSource: int = 0) -> bool:
        """
        Configures the USB interface to the requested sample rate.

        Args:
            rate_Hz (int): Supported rates typically include 44100, 48000, 96000.
            isSource (int): 0 for Rx (Host to Device), 1 for Tx (Device to Host).

        Returns:
            bool: True if configuration was successful.
        """
        ...

    @classmethod
    def set_bitDepth(cls, bitDepth: int) -> bool:
        """
        Configures the USB bit depth for audio samples.

        Args:
            bitDepth (int): Typically 16 or 24 bits.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_numChannels(cls, nChannels: int, isSource: int) -> bool:
        """
        Sets the number of audio channels for the USB stream.

        Args:
            nChannels (int): Number of channels (e.g., 1 for Mono, 2 for Stereo).
            isSource (int): 0 for Rx, 1 for Tx.

        Returns:
            bool: True if successful.
        """
        ...
    
    @classmethod
    def get_rxState(cls) -> bool:
        """
        Reads the current state of the USB Rx (Input) stream.

        Returns:
            bool: True if Rx is enabled/active.
        """
        ...

    @classmethod
    def get_txState(cls) -> bool:
        """
        Reads the current state of the USB Tx (Output) stream.

        Returns:
            bool: True if Tx is enabled/active.
        """
        ...

    @classmethod
    def get_sampleRate(cls, isSource: int = 0) -> int:
        """
        Reads the current LRCLK Sample Rate from the firmware.

        Args:
            isSource (int): 0 for Rx, 1 for Tx.

        Returns:
            int: Current sample rate in Hz.
        """
        ...

    @classmethod
    def get_bitDepth(cls) -> int:
        """
        Returns the current configured bit depth for USB Audio.

        Returns:
            int: 16 or 24.
        """
        ...
    
    @classmethod
    def get_numChannels(cls, isSource: int = 0) -> int:
        """
        Returns the number of audio channels currently in use.

        Args:
            isSource (int): 0 for Rx, 1 for Tx.

        Returns:
            int: Number of channels.
        """
        ...

    @classmethod
    def get_all(cls) -> dict:
        """
        Retrieves all USB Audio configurations from the firmware as a dictionary.

        Returns:
            dict: Configuration parameters for both Rx and Tx.
        """
        ...