# TO DO:
- Define, add, and subtract absolut encoder offsets. We are not doing that right now!
- Implement spin-wait loop and thread priority to improve timing performance.
- Implement a time over- or under-run exception.
- Get an equivalent inverse-kinematics solution working.

- Plan for validating the code:
    - Test Leg class's set_output_state_vector().
        - First test with just holding the leg in place.
        - Run a basic IK trot or something like that.
    - Test Leg class's shutdown().
        - Test with both get_latest_state_vector() and set_output_state_vector().

- Write a function to validate that the hardware watchdogs did infact get set up properly.