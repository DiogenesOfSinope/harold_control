### HARDWARE CONFIG ###
CAN_CHANNEL = "can0"
HOST_ID = 0xFD # 0xFD is generally the preferred default CAN ID for the host. Lower ID numbers have priority, ensuring that the motors' feedback wins. 0xFD (253 in decimal) is unlikely to clash with commonly used motor CAN IDs.
JOINT_CONFIG = {
    'hip':   {'id': 1, 'direction': -1.0, 'limits': (-0.52, 1.57)},
    'thigh': {'id': 2, 'direction': -1.0, 'limits': (-1.83, 0.0)},
    'knee':  {'id': 3, 'direction': -1.0, 'limits': (-1.57, 0.0)}
}
KP_GAIN = 60.0
KD_GAIN = 4.0

### MODEL CONFIG ###
MODEL_PATH = "policy.onnx"
LOOP_RATE_HZ = 50
DT = 1.0 / LOOP_RATE_HZ
HISTORY_LEN = 10
ACTION_SCALE = 0.25
DEFAULT_POS = [0.0, 0.0, 0.0]