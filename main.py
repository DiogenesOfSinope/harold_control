import sys
from robot.leg import Leg
from control.policy import Policy
from utils.safety import SafetyMonitor
from utils.exceptions import HardwareIOError, ActuatorFault, HardwareError, SafetyLimitError
from config import JOINT_CONFIG, RS03_LIMITS, KP_GAIN, KD_GAIN, MODEL_PATH, NUM_JOINTS, HISTORY_LEN, DT, DEFAULT_POS,  ACTION_SCALE


def setup(leg, policy, safety_monitor):
    leg.init_leg() # Starts the CAN bus, enables all motors, and checks the enable was succesful.
    state_vector = leg.get_latest_state_vector(target_states={}, kp=0.0, kd=0.0) # Get the latest state vector directly from the actuators -> make sure to use a zero kd and kp here!
    safety_monitor.verify_measured_state(state_vector) # Ensure the current state vector is not out of bounds.
    physical_targets = policy.compute_action(state_vector)
    safety_monitor.validate_commanded_targets(physical_targets)
    leg.set_output_state_vector(physical_targets=physical_targets,kp=KP_GAIN,kd=KD_GAIN)
    # Delay
    return

def loop(leg, policy, safety_monitor):
    state_vector = leg.get_latest_state_vector(target_states={},kp=KP_GAIN,kd=KD_GAIN)
    safety_monitor.verify_measured_state(state_vector)
    physical_targets = policy.compute_action(state_vector)
    safety_monitor.validate_commanded_targets(physical_targets)
    leg.set_output_state_vector(physical_targets=physical_targets, kp=KP_GAIN, kd=KD_GAIN)
    # Delay.
    return

def shutdown(leg):
    leg.shutdown()
    # Anything else we should run here?
    return

def main():
    leg = Leg(limits=RS03_LIMITS)
    policy = Policy(model_path=MODEL_PATH, num_joints=NUM_JOINTS, history_len=HISTORY_LEN, period=DT, default_pos=DEFAULT_POS, direction_vector=[], action_scale=ACTION_SCALE)
    safety_monitor = SafetyMonitor(joint_limits=JOINT_CONFIG)

    try:
        setup(leg, policy, safety_monitor)
        while True:
            loop(leg, policy, safety_monitor)
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