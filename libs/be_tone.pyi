#############################################################################################
#############################################################################################
# For further documentation, check:
# https://beembedded.gitbook.io/behydra/tools/automation-cli/python-apis/tone-generator
#############################################################################################
class TONE:
    """
    Interface for the internal Tone Signal Generator.
    Used for testing audio paths, verifying hardware connections, or generating UI feedback.
    """
    toneConfig: dict

    @classmethod
    def enable(cls, inputId: int = 0) -> bool:
        """
        Enables the Tone Signal Generator.

        Args:
            inputId (int): The Input Slot to allocate the tone data to.
                0: Automatic allocation to any available slot.
                1: Force allocation to Input Slot 1.
                2: Force allocation to Input Slot 2.

        Returns:
            bool: True if enabled successfully. False if already enabled or no slots available.
        """
        ...

    @classmethod
    def disable(cls) -> bool:
        """
        Disables the Tone Signal Generator.

        Returns:
            bool: True if disabled successfully, False otherwise.
        """
        ...

    @classmethod
    def set_signalType(cls, signalType: int) -> bool:
        """
        Configures the type of waveform to be generated.

        Args:
            signalType (int): 
                0: Sine Wave
                1: Square Wave
                2: White Noise
                3: Pink Noise

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_octave(cls, octave: int) -> bool:
        """
        Sets the frequency of the tone based on an octave/note index.

        Args:
            octave (int): Frequency index (refer to beHydra frequency table for mapping).

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_amplitude(cls, amplitudedB: float) -> bool:
        """
        Sets the signal level of the generated tone.

        Args:
            amplitudedB (float): Level in decibels relative to full scale (dBFS).
                Standard range is typically 0.0 to -90.0 dB.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_all(cls, toneConfig: dict) -> bool:
        """
        Applies a complete configuration dictionary to the Tone Generator.

        Args:
            toneConfig (dict): Complete configuration set for the generator.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def get_state(cls) -> bool:
        """
        Reads the current state of the Tone Generator.

        Returns:
            bool: True if currently enabled and generating signal.
        """
        ...
    
    @classmethod
    def get_signalType(cls) -> int:
        """Returns the currently selected signal type ID."""
        ...
 
    @classmethod
    def get_octave(cls) -> int:
        """Returns the current octave/frequency index."""
        ...

    @classmethod
    def get_amplitude(cls) -> float:
        """Returns the current amplitude setting in dB."""
        ...
    
    @classmethod
    def get_all(cls) -> dict:
        """Retrieves all current Tone Generator configurations from the firmware."""
        ...