from utils.exceptions import HardwareIOError, ActuatorFault, HardwareError

def setup():
    return

def loop():
    return

def shutdown():
    return

def main():
    # We want the entire script to be contained in our high-level try-catch block for error-handling purposes.
    try:
        setup()
        loop()
    except HardwareIOError:
        break
    except ActuatorFault:
        break
    except HardwareError:
        break
    except KeyboardInterrupt:
        print("\n[INFO] Interrupted by user.")
    finally:
        shutdown()

if __name__ == "__main__":
    main()