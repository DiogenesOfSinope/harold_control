import numpy as np
from utils.exceptions import SafetyLimitError

class SafetyMonitor:
    def __init__(self, joint_limits):
        """
        Initializes the safety monitor with strict zero-tolerance limits.
        Expected joint_limits structure:
        {
            'hip': {'id': 1, 'pos_limits': (-0.52, 1.57), 'vel_limits': (-15.0, 15.0)},
            ...
        }
        """
        self.joint_limits = joint_limits
        
        # Map motor IDs to their respective position and velocity limits for quick lookups
        self.id_to_limits = {
            config['id']: {
                'pos': config['pos_limits'],
                'vel': config['vel_limits']
            } 
            for config in joint_limits.values()
        }

        sorted_joints = sorted(joint_limits.items(), key=lambda item: item[1]['id'])
        
        # Ordered limits for array-based commanded state checks
        self.ordered_pos_limits = [config['pos_limits'] for name, config in sorted_joints]
        self.joint_names = [name for name, config in sorted_joints]

    def verify_measured_state(self, state_vector):
        """
        Checks the latest physical readings from the hardware against absolute limits. 
        Any deviation beyond the joint_limits triggers an immediate hard fault.
        """
        for motor_id, state in state_vector.items():
            pos = state.get('pos', 0.0)
            vel = state.get('vel', 0.0)
            
            limits = self.id_to_limits.get(motor_id)
            if limits:
                p_min, p_max = limits['pos']
                v_min, v_max = limits['vel']
                
                # Strict position bounds check
                if pos < p_min or pos > p_max:
                    raise SafetyLimitError(
                        f"Motor {motor_id} physically out of position bounds! "
                        f"Pos: {pos:.3f} rad. Limits: [{p_min}, {p_max}]"
                    )
                
                # Strict velocity bounds check
                if vel < v_min or vel > v_max:
                    raise SafetyLimitError(
                        f"Motor {motor_id} physically out of velocity bounds! "
                        f"Vel: {vel:.3f} rad/s. Limits: [{v_min}, {v_max}]"
                    )

    def validate_commanded_targets(self, physical_targets):
        """
        Validates the requested actions from the RL policy before transmission.
        Any deviation beyond the joint_limits is fatal.
        """
        for i, (joint_name, limits) in enumerate(zip(self.joint_names, self.ordered_pos_limits)):
            target = physical_targets[i]
            p_min, p_max = limits
            
            # Strict policy command bounds check
            if target < p_min or target > p_max:
                raise SafetyLimitError(
                    f"Rogue policy command! Requested {target:.3f} rad for {joint_name}. "
                    f"Limits: [{p_min}, {p_max}]"
                )