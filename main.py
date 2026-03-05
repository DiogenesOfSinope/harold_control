import sys
import onnxruntime as ort
from robot.leg import Leg
from utils.exceptions import HardwareIOError, ActuatorFault, HardwareError

# ADD IN FUNCTIONALITY TO CHECK THAT WE ARE WITHIN THE ACTUATOR BOUNDS ON STARTUP!!!
#   IF WE ARE SAY 2*PI RADIANS OFF (calibration wrong) we will destroy the robot!!

def setup(leg):
    # Run leg.init_leg()
    # Get latest state vector. -> is this baked into leg.init_leg()?
        # This serves to ensure we have a pre-filled state vector that is accurate when we start running the policy.
            # Otherwise it will set the positions to some crazy far away position on the first loop() iteration for
            # a fraction of a second until the policy runs on the returned data.
    # Run output transformer.
    # Set state vector.
    # Delay
    return

def loop(leg, policy):
    # Refresh the state vector from the actuators.
    state_vector = leg.get_latest_state_vector()
    # Compute policy.
    # Perhaps we should define our policy class which inherits from the previous OnnxPolicy, so we can include
    # a function for input vector formation/stacking?
    # Run output transformer.
    # Send output state vector.
    # Delay.
    return

def shutdown(leg):
    # Call leg.shutdown()?
    # Anything else we should run here?
    return

def main():
    leg = Leg()
    policy = OnnxPolicy(MODEL_PATH)

    try:
        setup(leg)
        while True:
            loop(leg, policy)
    except HardwareIOError as e:
        print(f"\n[CRITICAL] Communication Failure: {e}")
        print("Initiating emergency shutdown...")
    except ActuatorFault as e:
        print(f"\n[CRITICAL] Actuator Fault Detected: {e}")
        print("Initiating emergency shutdown...")
    except HardwareError as e:
        print(f"\n[CRITICAL] Unknown Hardware Failure: {e}")
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