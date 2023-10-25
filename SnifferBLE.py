import subprocess


def capture_packets(interface):
    # Create command
    command = ["tshark", "-i", interface, "-T", "json"]

    # Start a new process with the specified command and capture its output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
    
    
    print(f"🦈Capturing BLE on '{interface}'...")
    try:
        # Iterate through the lines of the captured output (captured packets)
        for line in process.stdout:
            # Print each line (captured packet) to the console without adding extra newlines
            print(line, end='')

    except KeyboardInterrupt:
        # Handle a KeyboardInterrupt (Ctrl+C) to terminate the process
        print("\n🐧Capturing stopped.")
        process.terminate()

if __name__ == "__main__":
    # Define the interface from which to capture packets, this willl be different, check in your wireshark interfaces
    interface = "nRF Sniffer for Bluetooth LE COM6"


    capture_packets(interface)
