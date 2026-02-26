class HardwareError(Exception):
    """Base class for all physical hardware failures."""

class HardwareIOError(HardwareError):
    """Raised when reading/writing to a physical bus fails (e.g., CAN socket crashes)."""

class ActuatorFault(HardwareError):
    """Raised when a motor reports an internal hardware fault (e.g., overtemp)."""
    pass