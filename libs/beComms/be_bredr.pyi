#############################################################################################
#############################################################################################
# For further documentation, check:
# https://beembedded.gitbook.io/behydra/tools/automation-cli/python-apis/bluetooth-br-edr
#############################################################################################

class BREDR:
    """
    Interface for Bluetooth Basic Rate/Enhanced Data Rate (Classic) operations.
    Requires the Consumer Audio Module to work.
    """
    bredr_config: dict

    @classmethod
    def enable(cls) -> bool:
        """
        Enables the Bluetooth Classic (BR/EDR) stack.

        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    @classmethod
    def disable(cls) -> bool:
        """
        Disables the Bluetooth Classic (BR/EDR) stack.

        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    @classmethod
    def get_state(cls) -> bool:
        """
        Returns the current power state of the Bluetooth stack.

        Returns:
            bool: True if powered on, False if powered off.
        """
        ...

    @classmethod
    def start_pairing(cls) -> bool:
        """
        Puts the device into pairing mode.
        
        - If Source: Automatically pairs with the device with the highest RSSI.
        - If Sink: Enters discoverable mode for other devices to find.

        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    @classmethod
    def stop_pairing(cls) -> bool:
        """
        Exits the device from its pairing mode.

        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    @classmethod
    def pair_device_by_bdaddress(cls, bdaddress: str) -> bool:
        """
        Pairs with a specific device using its Bluetooth Address.
        The device must be in Source Mode for this to succeed.

        Args:
            bdaddress (str): Hexadecimal string (e.g., '0x123456789123').

        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    @classmethod
    def set_sourceMode(cls, sourceMode: int) -> bool:
        """
        Sets the device role to either Source or Sink.

        Args:
            sourceMode (int): 
                0: Sink (Receiver Mode)
                1: Source (Transmitter Mode)

        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    @classmethod
    def connectDevices(cls) -> bool:
        """
        Attempts to connect to any previously paired/trusted device.

        Returns:
            bool: True if connection request sent successfully.
        """
        ...

    @classmethod
    def disconnectDevices(cls) -> bool:
        """
        Disconnects from all currently connected Bluetooth devices.

        Returns:
            bool: True if disconnection successful.
        """
        ...

    @classmethod
    def delete_allPairings(cls) -> bool:
        """
        Deletes all previously paired devices from the trusted device list.

        Returns:
            bool: True if successful.
        """
        ...

    @classmethod
    def set_audioCodecs(cls, codecConfig: int) -> bool:
        """
        Configures supported audio codecs via a bitmask.
        Note: Changes only apply to newly paired devices.

        Args:
            codecConfig (int): Bitmask values:
                Bit 0: SBC (Always Enabled)
                Bit 1: AAC
                Bit 2: aptX Classic
                Bit 3: aptX HD
                Bit 4: aptX Adaptive

        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    @classmethod
    def set_profiles(cls, profilesConfig: int) -> bool:
        """
        Configures the supported Bluetooth profiles via a bitmask.

        Args:
            profilesConfig (int): Bitmask values:
                Bit 0: HFP
                Bit 1: A2DP
                Bit 2: AVRCP
                Bit 14: LE Audio

        Returns:
            bool: True if successful, False otherwise.
        """
        ...

    @classmethod
    def start_scan(cls) -> dict:
        """
        Starts scanning for nearby devices in pairing mode.

        Returns:
            dict: Dictionary containing found device addresses and RSSI details.
        """
        ...

    @classmethod
    def get_beHydra_bdAddress(cls) -> str:
        """
        Retrieves the local beHydra hardware Bluetooth Device Address.

        Returns:
            str: The BD Address (e.g., '0x123456789123').
        """
        ...

    @classmethod
    def get_connectionStatus(cls) -> bool:
        """
        Checks if beHydra is currently ACL connected to any other Bluetooth device.

        Returns:
            bool: True if connected, False otherwise.
        """
        ...

    class avrcp:
        """Audio/Video Remote Control Profile - Playback and Metadata Control."""

        @classmethod
        def connect(cls) -> bool:
            """Connects the AVRCP profile with the paired device."""
            ...

        @classmethod
        def disconnect(cls) -> bool:
            """Disconnects the AVRCP profile from the paired device."""
            ...

        @classmethod
        def play(cls) -> bool:
            """Sends an AVRCP 'Play' command to the paired device."""
            ...
        
        @classmethod
        def pause(cls) -> bool:
            """Sends an AVRCP 'Pause' command to the paired device."""
            ...
        
        @classmethod
        def stop(cls) -> bool:
            """Sends an AVRCP 'Stop' command to the paired device."""
            ...

        @classmethod
        def toggle(cls) -> bool:
            """Toggles the music stream state between Play and Pause."""
            ...

        @classmethod
        def forward(cls) -> bool:
            """Sends an AVRCP command to skip to the next track."""
            ...

        @classmethod
        def back(cls) -> bool:
            """Sends an AVRCP command to return to the previous track."""
            ...

        @classmethod
        def fastforward(cls) -> bool:
            """Initiates fast-forwarding of the current track."""
            ...

        @classmethod
        def rewind(cls) -> bool:
            """Initiates rewinding of the current track."""
            ...

    class a2dp:
        """Advanced Audio Distribution Profile - Streaming High Quality Audio."""

        @classmethod
        def connect(cls) -> bool:
            """Connects the A2DP profile with the paired device."""
            ...
        
        @classmethod
        def disconnect(cls) -> bool:
            """Disconnects the A2DP profile from the paired device."""
            ...

        @classmethod
        def play(cls) -> bool:
            """Requests to start the A2DP stream playback."""
            ...

        @classmethod
        def stop(cls) -> bool:
            """Requests to stop the A2DP stream playback."""
            ...
        
        @classmethod
        def enable_input(cls, inputId: int = 0) -> bool:
            """
            Enables A2DP as an audio input source.

            Args:
                inputId (int): The Input Slot to allocate data to.
                    0: Automatic allocation to any available slot.
                    1: Force allocation to Slot 1.
                    2: Force allocation to Slot 2.

            Returns:
                bool: True if successful. False if already enabled or no slots available.
            """
            ...
            
        @classmethod
        def disable_input(cls) -> bool:
            """Disables A2DP as an input."""
            ...
        
        @classmethod
        def enable_output(cls, inputId: int = 0) -> bool:
            """
            Enables A2DP as an audio output.

            Args:
                inputId (int): The Output Slot to allocate data to.
                    0: Automatic allocation to any available slot.
                    1: Force allocation to Slot 1.
                    2: Force allocation to Slot 2.

            Returns:
                bool: True if successful. False if already enabled or no slots available.
            """
            ...
            
        @classmethod
        def disable_output(cls) -> bool:
            """Disables A2DP as an output."""
            ...

    class hfp:
        """Hands-Free Profile - Voice calls and Bidirectional Mono Audio."""

        @classmethod
        def connect(cls) -> bool:
            """Connects the HFP profile with the paired device."""
            ...

        @classmethod
        def disconnect(cls) -> bool:
            """Disconnects the HFP profile from the paired device."""
            ...

        @classmethod
        def call_initiate(cls) -> bool:
            """Initiates an outgoing call to the last dialed number or specified target."""
            ...

        @classmethod
        def call_accept(cls) -> bool:
            """Accepts an incoming phone call."""
            ...

        @classmethod
        def call_reject(cls) -> bool:
            """Rejects an incoming phone call."""
            ...

        @classmethod
        def call_terminate(cls) -> bool:
            """Terminates the current ongoing phone call."""
            ...

        @classmethod
        def isCallIncoming(cls) -> bool:
            """Checks if there is currently an active incoming call."""
            ...

        @classmethod
        def isCallActive(cls) -> bool:
            """Checks if there is an active ongoing call."""
            ...

        @classmethod
        def isCallOutgoing(cls) -> bool:
            """Checks if there is an outgoing call currently being placed."""
            ...

        @classmethod
        def enable_input(cls, inputId: int = 0) -> bool:
            """Enables HFP as an audio input (Microphone)."""
            ...
                
        @classmethod
        def disable_input(cls) -> bool:
            """Disables HFP as an input."""
            ...
            
        @classmethod
        def enable_output(cls, inputId: int = 0) -> bool:
            """Enables HFP as an audio output (Speaker)."""
            ...
                
        @classmethod
        def disable_output(cls) -> bool:
            """Disables HFP as an output."""
            ...