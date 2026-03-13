import sys
import time
from robot.leg import Leg
from control.policy import Policy
from utils.safety import SafetyMonitor
from utils.exceptions import HardwareIOError, ActuatorFault, HardwareError, SafetyLimitError
from config import JOINT_CONFIG, RS03_LIMITS, KP_GAIN, KD_GAIN, MODEL_PATH, NUM_JOINTS, HISTORY_LEN, DT, DEFAULT_POS, ACTION_SCALE

def format_targets(target_array):
    """
    Helper function to convert the policy's flat array output into the 
    dictionary structure expected by the robstride leg commands.
    """
    # Sort motor configs by ID to match the sorting in policy.py
    sorted_configs = sorted(JOINT_CONFIG.values(), key=lambda x: x['id'])
    return {
        config['id']: {'pos': float(target_array[i]), 'vel': 0.0, 'torque': 0.0} 
        for i, config in enumerate(sorted_configs)
    }

def setup(leg, policy, safety_monitor):
    leg.init_leg() # Starts the CAN bus, enables all motors, and checks the enable was succesful.
    start_time  = time.perf_counter()
    state_vector = leg.get_latest_state_vector(target_states={config['id']: {'pos': 0.0, 'vel': 0.0, 'torque': 0.0} for config in JOINT_CONFIG.values()}, kp=0.0, kd=0.0) # Get the latest state vector directly from the actuators -> make sure to use a zero kd and kp here!
    safety_monitor.verify_measured_state(state_vector) # Ensure the current state vector is not out of bounds.
    physical_targets = policy.compute_action(state_vector)
    safety_monitor.validate_commanded_targets(physical_targets)
    target_dict = format_targets(physical_targets)
    leg.set_output_state_vector(physical_targets=target_dict,kp=KP_GAIN,kd=KD_GAIN)
    elapsed = time.perf_counter - start_time
    if elapsed < DT:
        time.sleep(DT - elapsed)
    return target_dict

def loop(leg, policy, safety_monitor, prev_targets):
    start_time = time.perf_counter()
    state_vector = leg.get_latest_state_vector(target_states=prev_targets,kp=KP_GAIN,kd=KD_GAIN)
    safety_monitor.verify_measured_state(state_vector)
    physical_targets = policy.compute_action(state_vector)
    safety_monitor.validate_commanded_targets(physical_targets)
    target_dict = format_targets(physical_targets)
    leg.set_output_state_vector(physical_targets=target_dict, kp=KP_GAIN, kd=KD_GAIN)
    elapsed = time.perf_counter() - start_time
    if elapsed < DT:
        time.sleep(DT - elapsed)
    return target_dict

def shutdown(leg):
    leg.shutdown()
    return

def main():
    leg = Leg(limits=RS03_LIMITS)
    direction_vector = [config['direction'] for config in sorted(JOINT_CONFIG.values(), key=lambda x: x['id'])]
    policy = Policy(model_path=MODEL_PATH, num_joints=NUM_JOINTS, history_len=HISTORY_LEN, period=DT, default_pos=DEFAULT_POS, direction_vector=[], action_scale=ACTION_SCALE)
    safety_monitor = SafetyMonitor(joint_limits=JOINT_CONFIG)

    try:
        current_targets = setup(leg, policy, safety_monitor)
        while True:
            current_targets =  loop(leg, policy, safety_monitor, current_targets)
    except SafetyLimitError as e:
        print(f"\n[EMERGENCY STOP] Safety Interlock Tripped: {e}")
    except (HardwareIOError, ActuatorFault, HardwareError) as e:
        print(f"\n[CRITICAL] Hardware Failure: {e}")
        print("Initiating emergency shutdown...")
    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user. Shutting down gracefully...")
    except Exception as e:
        print(f"\n[FATAL] Unexpected software error: {e}")
    finally:
        shutdown(leg)
        sys.exit(0)

if __name__ == "__main__":
    main()