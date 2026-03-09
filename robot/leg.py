from robstride import Robstride


class Leg:
    # Strictly a hardware abstraction layer for the robstride actuators.
    # Does not contain previous state information -> this is handled in policy.py!
    def __init__(self):
        self.robstride = Robstride()
        return
    
    def init_Leg(self):
        self.robstride.init_CAN_bus()
        self.robstride.enable_and_verify_all()
    
    def get_latest_state_vector(self, target_states: dict, kp: float, kd: float, limits: dict):
        self.robstride.flush_CAN_bus()
        self.robstride.send_all_target_state_vectors(self, target_states=target_states, kp=kp, kd=kd, limits=limits)
        return self.robstride.wait_for_all_replies()
    
    def run_output_transform(self):
        # Scale actions.
        # Add default offset.
        # Apply direction/inversion.
        # Implement soft joints/limit in software.
        return
    
    def set_output_state_vector(self):
        # send_all_target_state_vectors()
        return