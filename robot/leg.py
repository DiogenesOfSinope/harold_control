class Leg:
    def __init__():
        return
    
    def init_Leg():
        robstride.init_CAN_bus()
        robstride.enable_and_verify_all()
    
    def get_latest_state_vector(self, target_states: dict, kp: float, kd: float, limits: dict):
        robstride.flush_CAN_bus()
        robstride.send_all_target_state_vectors(self, target_states=target_states kp=kp, kd=kd, limits=limits)
        robstride.wait_for_all_replies()
        # Should return the latest state vector?
    
    def run_output_transform():
        # Scale actions.
        # Add default offset.
        # Apply direction/inversion.
        # Implement soft joints/limit in software.
        return
    
    def set_output_state_vector():
        # send_all_target_state_vectors()
        return