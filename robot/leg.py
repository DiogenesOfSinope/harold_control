class Leg:
    def __init__():
        return
    
    def init_Leg():
        robstride.init_CAN_bus()
        robstride.enable_and_verify_all()
    
    def get_latest_state_vector():
        robstride.flush_CAN_bus()
        robstride.send_all_target_state_vectors()
        robstride.wait_for_all_replies()
    
    def run_output_transform():
        # Scale actions.
        # Add default offset.
        # Apply direction/inversion.
        # Implement soft joints/limit in software.
        return
    
    def set_output_state_vector():
        # send_all_target_state_vectors()
        return