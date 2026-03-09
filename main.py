import sys
from robot.leg import Leg
from utils.exceptions import HardwareIOError, ActuatorFault, HardwareError, SafetyLimitError

# ADD IN FUNCTIONALITY TO CHECK THAT WE ARE WITHIN THE ACTUATOR BOUNDS ON STARTUP!!!
#   IF WE ARE SAY 2*PI RADIANS OFF (calibration wrong) we will destroy the robot!!

def setup(leg):
    leg.init_leg() # Starts the CAN bus, enables all motors, and checks the enable was succesful.
    state_vector = leg.get_latest_state_vector()
    # CHECK THAT OUR POSITION IS WITHIN THE BOUNDS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

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
    # Compute policy.W
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
        setup(leg, policy)
        while True:
            loop(leg, policy)
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