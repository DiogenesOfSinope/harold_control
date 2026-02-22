import can

class Robstride:
    def __init__(self):
        self.bus = None
    
    def flush_CAN_bus(self):
        while self.bus.recv(timeout=0.0): pass
    
    def enable_hardware_watchdog(self):
        # Send hardware watchdog enable messages to all actuators.
        return
    
    def verify_hardware_watchdog(self):
        # Flush the CAN bus.
        # Send a specific data read command to all actuators for hardware watchdog state.
        # Wait for responses, with timeout, checking the message type of each message, and verifying hardware watchdog state for all actuators.
        # Raise an appropriate exception if there is an error.
        return

    def init_CAN_bus(self):
        # Bring up the CAN bus.
        # enable_hardware_watchdog()
        # verify_hardware_watchdog()
        return
    
    def enable_MIT_all(self):
        # Send the correct message to all actuators to enter MIT mode with a zero-torque passive state.
        return
    
    def verify_MIT_all(self):
        # Flush the CAN bus.
        # Send a specific data read command to all actuators for MIT state.
        # Wait for responses, with timeout, checking the message type of each message, and verifying MIT state for all actuators.
        # Raise an appropriate exception if there is an error.
        return

    def send_target_state_vector(self):
        # Send the correct command to set the target state vector of a given motor in MIT control mode.
        return
    
    def send_all_target_state_vectors(self):
        # Call send_target_state_vector() for all actuators.
        return
    
    # Requires flush_CAN_bus() to be appropriately called before the original outbound messages were sent that we are listening for replies.
    def wait_for_all_replies(self):
        # Attempt to receive CAN messages of the expected reply type until either the correct number have been been accounted for, or raise an exception.
        # Raise an exception if timeout passes a specific threshold.
        # Return the received messages.
        return
    
    def shutdown(self):
        # If the CAN bus has been enabled, send disable commands to all motors.
        return