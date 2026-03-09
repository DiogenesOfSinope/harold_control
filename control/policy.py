import onnxruntime as ort
import numpy as np
from collections import deque
import time
import sys

class Policy:
    def __init__(self, model_path, num_joints, history_len, period, default_pos, direction_vector):
        print(f"[INFO] Loading model: {model_path}")
        try:
            self.session = ort.InferenceSession(model_path)
            self.input_name = self.session.get_inputs()[0].name
        except Exception as e:
            print(f"[ERROR] Model load failed: {e}")
            sys.exit(1)
            
        self.period = period
        self.default_pos = np.array(default_pos)
        self.direction_vector = np.array(direction_vector)
        
        self.pos_hist = deque([np.zeros(num_joints)] * history_len, maxlen=history_len)
        self.vel_hist = deque([np.zeros(num_joints)] * history_len, maxlen=history_len)
        self.start_time = time.perf_counter() # For phase signal.
    
    def compute_action(self, state_vector):
        # Extract and sort raw hardware states
        sorted_keys = sorted(state_vector.keys())
        raw_pos = np.array([state_vector[k]['pos'] for k in sorted_keys])
        raw_vel = np.array([state_vector[k]['vel'] for k in sorted_keys])

        # Sim-to-Real Transformations
        sim_pos = raw_pos * self.direction_vector
        sim_vel = raw_vel * self.direction_vector
        rel_pos = sim_pos - self.default_pos

        # Update history with normalized values
        self.pos_hist.appendleft(rel_pos)
        self.vel_hist.appendleft(sim_vel)

        # Phase signal
        elapsed_time = time.perf_counter() - self.start_time
        phase = 2 * np.pi * elapsed_time / self.period
        phase_signal = [np.sin(phase), np.cos(phase)]

        # Flatten and build observation
        flat_pos = [val for step in self.pos_hist for val in step]
        flat_vel = [val for step in self.vel_hist for val in step]
        obs = np.array(flat_pos + flat_vel + phase_signal, dtype=np.float32).reshape(1,-1)

        # Inference
        raw_actions = self.session.run(None, {self.input_name: obs})[0][0]
        return raw_actions