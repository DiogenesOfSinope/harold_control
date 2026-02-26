import can
import struct
from utils.exceptions import HardwareIOError, ActuatorFault, HardwareError

class Robstride:
    def __init__(self):
        self.bus = None
    
    # Function completed.
    def flush_CAN_bus(self):
        try:
            while self.bus.recv(timeout=0.0): pass
        except can.CanError as e:
            raise HardwareIOError(f"I/O failure while flushing CAN bus: {e}")
        
    def transmit(self, comm_type, extra_data, destination_id, data=b'\x00'*8):
        arb_id = (comm_type << 24) | (extra_data << 8) | destination_id
        msg = can.Message(arbitration_id=arb_id, data=data, is_extended_id=True, dlc=len(data))
        try:
            self.bus.send(msg)
        except can.CanError as e:
            raise HardwareIOError(f"Failed to transmit CommType {comm_type} to ID {destination_id}: {e}")

    def receive(self, timeout=0.001):
        try:
            msg = self.bus.recv(timeout=timeout)
            if msg is None:
                return None
            
            # 1. Unpack the raw arbitration ID
            comm_type = (msg.arbitration_id >> 24) & 0x1F
            extra_data = (msg.arbitration_id >> 8) & 0xFFFF
            destination_id = msg.arbitration_id & 0xFF
            
            # 2. Extract the actual sending Motor ID from the extra_data
            motor_id = extra_data & 0xFF 
            
            return comm_type, motor_id, destination_id, extra_data, msg.data
            
        except can.CanError as e:
            raise HardwareIOError(f"I/O failure while receiving from bus: {e}")
        
    def write_parameter(self, target_id, param_index, value, value_format='<I'):
        """Pipelines a parameter write to the CAN bus without blocking."""
        index_bytes = struct.pack('<HH', param_index, 0x0000)
        data_bytes = struct.pack(value_format, value)
        self.transmit(18, self.host_id, target_id, data=index_bytes + data_bytes)

    def read_parameter(self, target_id, param_index, value_format='<I', timeout=0.1):
        """
        Reads a single parameter from a motor's memory.
        """
        # CommType 17 (Read), request payload sets data bytes to 0
        req_data = struct.pack('<HHL', param_index, 0x0000, 0x00000000)
        self.transmit(17, self.host_id, target_id, data=req_data)
        
        start_t = time.perf_counter()
        while (time.perf_counter() - start_t) < timeout:
            reply = self.receive(timeout=0.01)
            if reply is None:
                continue
            
            # Unpack all 5 variables perfectly
            c_type, motor_id, dest_id, extra_data, r_data = reply
            
            # Filter for a CommType 17 reply from the specific motor, sent to our host
            if c_type == 17 and motor_id == target_id and dest_id == self.host_id:
                # Unpack exactly bytes 4 through 7 using the provided format string
                return struct.unpack(value_format, r_data[4:8])[0]
                
        raise HardwareIOError(f"Timeout waiting for parameter {hex(param_index)} read from Motor {target_id}")
    
    def enable_hardware_watchdog(self, timeout_ms=100):
        print(f"[INFO] Setting hardware watchdogs to {timeout_ms}ms...")
        timeout_units = int(timeout_ms * 20)
        
        for mid in self.motor_ids:
            # 0x7028 is the CAN_TIMEOUT parameter index, expecting an unsigned 32-bit int ('<I')
            self.write_parameter(mid, 0x7028, timeout_units, '<I')
            
    def verify_hardware_watchdog(self, expected_timeout_ms=100):
        print("[INFO] Verifying hardware watchdogs...")
        expected_units = int(expected_timeout_ms * 20)
        
        self.flush_CAN_bus() # Always flush before reading to drop stale frames
        
        for mid in self.motor_ids:
            returned_val = self.read_parameter(mid, 0x7028, '<I')
            
            if returned_val != expected_units:
                raise HardwareIOError(
                    f"Motor {mid} watchdog mismatch! Expected {expected_units}, got {returned_val}"
                )
            
            print(f"  -> Motor {mid}: Watchdog VERIFIED at {expected_timeout_ms}ms.")

    # Function completed.
    def init_CAN_bus(self):
        print(f"[INFO] Initializing CAN bus on channel: {self.channel}...")
        try:
            self.bus = can.interface.Bus(channel=self.channel, interface='socketcan', bitrate=1000000)
        except can.CanError as e:
            raise HardwareIOError(f"CAN library error while initializing {self.channel}: {e}")
        except OSError as e:
            raise HardwareIOError(f"OS error connecting to {self.channel}. Is the interface physically up? {e}")
        self.enable_hardware_watchdog()
        self.verify_hardware_watchdog()
        print("[INFO] CAN bus initialized and watchdogs verified.")
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