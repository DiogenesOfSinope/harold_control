"""
Private protocol definitions.

This file contains the constants defined by the RobStride user manual.

Copied directly from SeeedStudio's RobStride_Control library, with thanks.
https://github.com/Seeed-Projects/RobStride_Control/tree/master
"""

import numpy as np


class CommunicationType:
    """
    Private communication type definitions
    """

    GET_DEVICE_ID       = 0
    """Gets the device's ID and 64-bit MCU unique identifier."""

    OPERATION_CONTROL   = 1
    """Sets target angle, angular velocity, torque, Kp, and Kd."""

    OPERATION_STATUS    = 2
    """Motor feedback frame reporting current angle, angular velocity, torque, and temperature."""

    ENABLE              = 3
    """Enables the motor to run."""

    DISABLE             = 4
    """Stops the motor from running."""

    SET_ZERO_POSITION   = 6
    """Sets the motor's mechanical zero position."""

    SET_DEVICE_ID       = 7
    """Sets the motor's CAN ID (takes effect immediately)."""

    READ_PARAMETER      = 17
    """Reads a single parameter."""

    WRITE_PARAMETER     = 18
    """Writes a single parameter (changes are lost on power failure unless saved)."""

    FAULT_REPORT        = 21
    """Fault feedback frame."""

    SAVE_PARAMETERS     = 22
    """Saves motor data/parameters."""

    SET_BAUDRATE        = 23
    """Sets the motor's baud rate (requires a re-power-on to take effect)."""

    ACTIVE_REPORT       = 24
    """Enables/disables the motor actively reporting frames."""

    SET_PROTOCOL        = 25
    """Sets the motor protocol type (requires a re-power-on to take effect)."""

    READ_VERSION_NUMBER = 26
    """Reads the motor's version number."""

class ParameterType:
    """
    Parameter type definitions for RobStride RS03
    """
    # ==========================================
    # 0x20XX Parameters (Configuration R/W)
    # ==========================================
    ECHO_PARA1              = (0x2000, np.uint16,   "echoPara1")
    ECHO_PARA2              = (0x2001, np.uint16,   "echoPara2")
    ECHO_PARA3              = (0x2002, np.uint16,   "echoPara3")
    ECHO_PARA4              = (0x2003, np.uint16,   "echoPara4")
    ECHO_FRE_HZ             = (0x2004, np.uint32,   "echoFreHz")
    MECHANICAL_OFFSET       = (0x2005, np.float32,  "MechOffset")
    CHASU_OFFSET            = (0x2006, np.float32,  "Chasu_offset")
    STATUS1                 = (0x2007, np.float32,  "Status1")
    I_FW_MAX                = (0x2008, np.float32,  "I_FW_MAX")
    CAN_ID_2009             = (0x2009, np.uint8,    "CAN_ID")
    CAN_MASTER              = (0x200A, np.uint8,    "CAN_MASTER")
    CAN_TIMEOUT_200B        = (0x200B, np.uint8,    "CAN_TIMEOUT")
    STATUS2                 = (0x200C, np.uint32,   "status2")
    STATUS3                 = (0x200D, np.int16,    "status3")
    STATUS4                 = (0x200E, np.uint32,   "Status4")
    STATUS5                 = (0x200F, np.float32,  "Status5")
    STATUS6                 = (0x2010, np.uint8,    "Status6")
    CUR_FILT_GAIN_2011      = (0x2011, np.float32,  "cur_filt_gain")
    CUR_KP_2012             = (0x2012, np.float32,  "cur_kp")
    CUR_KI_2013             = (0x2013, np.float32,  "cur_ki")
    SPD_KP_2014             = (0x2014, np.float32,  "spd_kp")
    SPD_KI_2015             = (0x2015, np.float32,  "spd_ki")
    LOC_KP_2016             = (0x2016, np.float32,  "loc_kp")
    SPD_FILT_GAIN_2017      = (0x2017, np.float32,  "spd_filt_gain")
    LIMIT_SPD_2018          = (0x2018, np.float32,  "limit_spd")
    LIMIT_CUR_2019          = (0x2019, np.float32,  "limit_cur")
    LIMIT_A                 = (0x201A, np.float32,  "limit a")
    FAULT1_201B             = (0x201B, np.float32,  "fault1")
    FAULT2_201C             = (0x201C, np.float32,  "fault2")
    FAULT3_201D             = (0x201D, np.float32,  "fault3")
    FAULT4_201E             = (0x201E, np.float32,  "fault4")
    FAULT5_201F             = (0x201F, np.float32,  "fault5")
    FAULT6_2020             = (0x2020, np.float32,  "fault6")
    FAULT7_2021             = (0x2021, np.float32,  "fault7")
    BAUD                    = (0x2022, np.uint8,    "baud")
    ZERO_STA_2023           = (0x2023, np.uint8,    "zero_sta")
    POSITION_OFFSET_2024    = (0x2024, np.uint8,    "position_offset")
    PROTOCOL_1              = (0x2025, np.uint8,    "protocol_1")
    DAMPER_2026             = (0x2026, np.uint8,    "damper")
    ADD_OFFSET_2027         = (0x2027, np.float32,  "add_offset")

    # ==========================================
    # 0x30XX Parameters (Diagnostic Read-Only)
    # ==========================================
    TIME_USE_0              = (0x3000, np.uint16,   "timeUse0")
    TIME_USE_1              = (0x3001, np.uint16,   "timeUse1")
    TIME_USE_2              = (0x3002, np.uint16,   "timeUse2")
    TIME_USE_3              = (0x3003, np.uint16,   "timeUse3")
    ENCODER_RAW             = (0x3004, np.int16,    "encoderRaW")
    MCU_TEMP                = (0x3005, np.int16,    "mcuTemp")
    MOTOR_TEMP              = (0x3006, np.int16,    "motorTemp")
    VBUS_MV                 = (0x3007, np.uint16,   "vBus(mv)")
    ADC1_OFFSET             = (0x3008, np.int32,    "adc1Offset")
    ADC2_OFFSET             = (0x3009, np.int32,    "adc2Offset")
    ADC1_RAW                = (0x300A, np.uint16,   "adc1Raw")
    ADC2_RAW                = (0x300B, np.uint16,   "adc2Raw")
    VBUS_300C               = (0x300C, np.float32,  "VBUS")
    CMD_ID                  = (0x300D, np.float32,  "cmdId")
    CMD_IQ                  = (0x300E, np.float32,  "cmdIq")
    CMD_LOC_REF             = (0x300F, np.float32,  "cmdlocref")
    CMD_SPD_REF             = (0x3010, np.float32,  "cmdspdref")
    CMD_TORQUE              = (0x3011, np.float32,  "cmdTorque")
    CMD_POS                 = (0x3012, np.float32,  "cmdPos")
    CMD_VEL                 = (0x3013, np.float32,  "cmdVel")
    ROTATION                = (0x3014, np.int16,    "rotation")
    MOD_POS                 = (0x3015, np.float32,  "mod Pos")
    MEASURED_POSITION_3016  = (0x3016, np.float32,  "mechPos")
    MEASURED_VELOCITY_3017  = (0x3017, np.float32,  "mechVel")
    ELEC_POS                = (0x3018, np.float32,  "elecPos")
    IA                      = (0x3019, np.float32,  "ia")
    IB                      = (0x301A, np.float32,  "ib")
    IC                      = (0x301B, np.float32,  "ic")
    TIMEOUT                 = (0x301C, np.uint32,   "timeout")
    PHASE_ORDER             = (0x301D, np.uint8,    "phaseOrder")
    IQF_301E                = (0x301E, np.float32,  "iqf")
    BOARD_TEMP              = (0x301F, np.int16,    "boardTemP")
    IQ                      = (0x3020, np.float32,  "iq")
    ID                      = (0x3021, np.float32,  "id")
    FAULT_STA               = (0x3022, np.uint32,   "faultSta")
    WARN_STA                = (0x3023, np.uint32,   "warnSta")
    DRV_FAULT               = (0x3024, np.uint16,   "drv_fault")
    DRV_TEMP                = (0x3025, np.int16,    "drv_temp")
    UQ                      = (0x3026, np.float32,  "Uq")
    AS_ANGLE                = (0x3027, np.float32,  "as_angle")
    CS_ANGLE                = (0x3028, np.float32,  "cs_angle")
    CHASU_ANGLE             = (0x3029, np.float32,  "chasu_angle")
    V_BUS_302A              = (0x302A, np.float32,  "v bus")
    ELEC_OFFSET             = (0x302B, np.float32,  "ElecOffset")
    MEASURED_TORQUE         = (0x302C, np.float32,  "torque_fdb")
    RATED_I                 = (0x302D, np.float32,  "rated i")
    MECH_POS_INIT           = (0x302E, np.float32,  "MechPos_init")
    INSTEP                  = (0x302F, np.float32,  "instep")
    STATUS                  = (0x3030, np.uint8,    "status")
    CMD_LOC_REF_3031        = (0x3031, np.float32,  "cmdlocref")
    VEL_MAX_3032            = (0x3032, np.float32,  "vel max")
    FAULT1_3033             = (0x3033, np.float32,  "fault1")
    FAULT2_3034             = (0x3034, np.float32,  "fault2")
    FAULT3_3035             = (0x3035, np.float32,  "fault3")
    FAULT4_3036             = (0x3036, np.float32,  "fault4")
    FAULT5_3037             = (0x3037, np.float32,  "fault5")
    FAULT6_3038             = (0x3038, np.uint32,   "fault6")
    FAULT7_3039             = (0x3039, np.uint32,   "fault7")
    FAULT8_303A             = (0x303A, np.uint32,   "fault8")
    MC_OVER_TEMP            = (0x303B, np.int16,    "mcOverTemp")
    KT_NM_AMP               = (0x303C, np.float32,  "Kt_Nm/Amp")
    TQCALI_TYPE             = (0x303D, np.uint8,    "Tqcali_Type")
    THETA_MECH1             = (0x303E, np.float32,  "theta_mech1")
    ADC_OFFSET_1            = (0x303F, np.uint32,   "adcoffset 1")
    ADC_OFFSET_2            = (0x3040, np.uint32,   "adcOffset 2")
    CAN_STATUS              = (0x3041, np.uint8,    "can_status")
    POSITION_3042           = (0x3042, np.float32,  "position")
    CHASU_ANGLE_INIT        = (0x3043, np.float32,  "chasu_angle_init")
    CHASU_ANGLE_OUT         = (0x3044, np.float32,  "chasu_angle_out")
    MOTOR_MECH_INIT         = (0x3045, np.float32,  "motormechinit")
    MECH_ANGLE_INIT2        = (0x3046, np.float32,  "mech_angle_init2")
    MECH_ANGLE_ROTAT        = (0x3047, np.int16,    "mech_angle_rotat")
    CODER_REG               = (0x3048, np.uint16,   "coder_reg")
    POS_CNT1                = (0x3049, np.uint16,   "pos_cnt1")

    # ==========================================
    # 0x70XX Parameters (Control R/W)
    # ==========================================
    MODE                    = (0x7005, np.uint8,    "run_mode")
    IQ_TARGET               = (0x7006, np.float32,  "iq_ref")
    VELOCITY_TARGET         = (0x700A, np.float32,  "spd_ref")
    TORQUE_LIMIT            = (0x700B, np.float32,  "limit_torque")
    CURRENT_KP              = (0x7010, np.float32,  "cur_kp")
    CURRENT_KI              = (0x7011, np.float32,  "cur_ki")
    CURRENT_FILTER_GAIN     = (0x7014, np.float32,  "cur_filt_gain")
    POSITION_TARGET         = (0x7016, np.float32,  "loc_ref")
    VELOCITY_LIMIT          = (0x7017, np.float32,  "limit_spd")
    CURRENT_LIMIT           = (0x7018, np.float32,  "limit_cur")
    MECHANICAL_POSITION     = (0x7019, np.float32,  "mechPos")
    IQ_FILTERED             = (0x701A, np.float32,  "iqf")
    MECHANICAL_VELOCITY     = (0x701B, np.float32,  "mechVel")
    VBUS                    = (0x701C, np.float32,  "VBUS")
    # ROTATION                = (0x701D, np.float32,  "rot_cnt")
    POSITION_KP             = (0x701E, np.float32,  "loc_kp")
    VELOCITY_KP             = (0x701F, np.float32,  "spd_kp")
    VELOCITY_KI             = (0x7020, np.float32,  "spd_ki")
    VELOCITY_FILTER_GAIN    = (0x7021, np.float32,  "spd_filt_gain")
    VEL_ACCELERATION_TARGET = (0x7022, np.float32,  "acc_rad")
    PP_VELOCITY_MAX         = (0x7024, np.float32,  "vel_max")
    PP_ACCELERATION_TARGET  = (0x7025, np.float32,  "acc_set")
    EPSCAN_TIME             = (0x7026, np.uint16,   "EPScan_time")
    CAN_TIMEOUT             = (0x7028, np.uint32,   "canTimeout")
    ZERO_STATE              = (0x7029, np.uint8,    "zero_sta")
    DAMPER                  = (0x702A, np.uint8,    "damper")
    ADD_OFFSET              = (0x702B, np.float32,  "add_offset")