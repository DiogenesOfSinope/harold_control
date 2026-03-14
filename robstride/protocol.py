"""
Private protocol definitions.

This file contains the constants defined by the RobStride user manual.

Copied directly from SeeedStudio's RobStride_Control library, with thanks.
https://github.com/Seeed-Projects/RobStride_Control/tree/master
"""

import numpy as np

# Map numpy types to struct format characters (Little Endian)
FORMAT_MAP = {
    np.uint8: '<B',
    np.uint16: '<H',
    np.int16: '<h',
    np.uint32: '<I',
    np.int32: '<i',
    np.float32: '<f'
}

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
    ECHO_PARA1              = (0x2000, np.uint16)
    ECHO_PARA2              = (0x2001, np.uint16)
    ECHO_PARA3              = (0x2002, np.uint16)
    ECHO_PARA4              = (0x2003, np.uint16)
    ECHO_FRE_HZ             = (0x2004, np.uint32)
    MECHANICAL_OFFSET       = (0x2005, np.float32)
    CHASU_OFFSET            = (0x2006, np.float32)
    STATUS1                 = (0x2007, np.float32)
    I_FW_MAX                = (0x2008, np.float32)
    CAN_ID_2009             = (0x2009, np.uint8)
    CAN_MASTER              = (0x200A, np.uint8)
    CAN_TIMEOUT_200B        = (0x200B, np.uint8)
    STATUS2                 = (0x200C, np.uint32)
    STATUS3                 = (0x200D, np.int16)
    STATUS4                 = (0x200E, np.uint32)
    STATUS5                 = (0x200F, np.float32)
    STATUS6                 = (0x2010, np.uint8)
    CUR_FILT_GAIN_2011      = (0x2011, np.float32)
    CUR_KP_2012             = (0x2012, np.float32)
    CUR_KI_2013             = (0x2013, np.float32)
    SPD_KP_2014             = (0x2014, np.float32)
    SPD_KI_2015             = (0x2015, np.float32)
    LOC_KP_2016             = (0x2016, np.float32)
    SPD_FILT_GAIN_2017      = (0x2017, np.float32)
    LIMIT_SPD_2018          = (0x2018, np.float32)
    LIMIT_CUR_2019          = (0x2019, np.float32)
    LIMIT_A                 = (0x201A, np.float32)
    FAULT1_201B             = (0x201B, np.float32)
    FAULT2_201C             = (0x201C, np.float32)
    FAULT3_201D             = (0x201D, np.float32)
    FAULT4_201E             = (0x201E, np.float32)
    FAULT5_201F             = (0x201F, np.float32)
    FAULT6_2020             = (0x2020, np.float32)
    FAULT7_2021             = (0x2021, np.float32)
    BAUD                    = (0x2022, np.uint8)
    ZERO_STA_2023           = (0x2023, np.uint8)
    POSITION_OFFSET_2024    = (0x2024, np.uint8)
    PROTOCOL_1              = (0x2025, np.uint8)
    DAMPER_2026             = (0x2026, np.uint8)
    ADD_OFFSET_2027         = (0x2027, np.float32)

    # ==========================================
    # 0x30XX Parameters (Diagnostic Read-Only)
    # ==========================================
    TIME_USE_0              = (0x3000, np.uint16)
    TIME_USE_1              = (0x3001, np.uint16)
    TIME_USE_2              = (0x3002, np.uint16)
    TIME_USE_3              = (0x3003, np.uint16)
    ENCODER_RAW             = (0x3004, np.int16)
    MCU_TEMP                = (0x3005, np.int16)
    MOTOR_TEMP              = (0x3006, np.int16)
    VBUS_MV                 = (0x3007, np.uint16)
    ADC1_OFFSET             = (0x3008, np.int32)
    ADC2_OFFSET             = (0x3009, np.int32)
    ADC1_RAW                = (0x300A, np.uint16)
    ADC2_RAW                = (0x300B, np.uint16)
    VBUS_300C               = (0x300C, np.float32)
    CMD_ID                  = (0x300D, np.float32)
    CMD_IQ                  = (0x300E, np.float32)
    CMD_LOC_REF             = (0x300F, np.float32)
    CMD_SPD_REF             = (0x3010, np.float32)
    CMD_TORQUE              = (0x3011, np.float32)
    CMD_POS                 = (0x3012, np.float32)
    CMD_VEL                 = (0x3013, np.float32)
    ROTATION                = (0x3014, np.int16)
    MOD_POS                 = (0x3015, np.float32)
    MEASURED_POSITION_3016  = (0x3016, np.float32)
    MEASURED_VELOCITY_3017  = (0x3017, np.float32)
    ELEC_POS                = (0x3018, np.float32)
    IA                      = (0x3019, np.float32)
    IB                      = (0x301A, np.float32)
    IC                      = (0x301B, np.float32)
    TIMEOUT                 = (0x301C, np.uint32)
    PHASE_ORDER             = (0x301D, np.uint8)
    IQF_301E                = (0x301E, np.float32)
    BOARD_TEMP              = (0x301F, np.int16)
    IQ                      = (0x3020, np.float32)
    ID                      = (0x3021, np.float32)
    FAULT_STA               = (0x3022, np.uint32)
    WARN_STA                = (0x3023, np.uint32)
    DRV_FAULT               = (0x3024, np.uint16)
    DRV_TEMP                = (0x3025, np.int16)
    UQ                      = (0x3026, np.float32)
    AS_ANGLE                = (0x3027, np.float32)
    CS_ANGLE                = (0x3028, np.float32)
    CHASU_ANGLE             = (0x3029, np.float32)
    V_BUS_302A              = (0x302A, np.float32)
    ELEC_OFFSET             = (0x302B, np.float32)
    MEASURED_TORQUE         = (0x302C, np.float32)
    RATED_I                 = (0x302D, np.float32)
    MECH_POS_INIT           = (0x302E, np.float32)
    INSTEP                  = (0x302F, np.float32)
    STATUS                  = (0x3030, np.uint8)
    CMD_LOC_REF_3031        = (0x3031, np.float32)
    VEL_MAX_3032            = (0x3032, np.float32)
    FAULT1_3033             = (0x3033, np.float32)
    FAULT2_3034             = (0x3034, np.float32)
    FAULT3_3035             = (0x3035, np.float32)
    FAULT4_3036             = (0x3036, np.float32)
    FAULT5_3037             = (0x3037, np.float32)
    FAULT6_3038             = (0x3038, np.uint32)
    FAULT7_3039             = (0x3039, np.uint32)
    FAULT8_303A             = (0x303A, np.uint32)
    MC_OVER_TEMP            = (0x303B, np.int16)
    KT_NM_AMP               = (0x303C, np.float32)
    TQCALI_TYPE             = (0x303D, np.uint8)
    THETA_MECH1             = (0x303E, np.float32)
    ADC_OFFSET_1            = (0x303F, np.uint32)
    ADC_OFFSET_2            = (0x3040, np.uint32)
    CAN_STATUS              = (0x3041, np.uint8)
    POSITION_3042           = (0x3042, np.float32)
    CHASU_ANGLE_INIT        = (0x3043, np.float32)
    CHASU_ANGLE_OUT         = (0x3044, np.float32)
    MOTOR_MECH_INIT         = (0x3045, np.float32)
    MECH_ANGLE_INIT2        = (0x3046, np.float32)
    MECH_ANGLE_ROTAT        = (0x3047, np.int16)
    CODER_REG               = (0x3048, np.uint16)
    POS_CNT1                = (0x3049, np.uint16)

    # ==========================================
    # 0x70XX Parameters (Control R/W)
    # ==========================================
    MODE                    = (0x7005, np.uint8)
    IQ_TARGET               = (0x7006, np.float32)
    VELOCITY_TARGET         = (0x700A, np.float32)
    TORQUE_LIMIT            = (0x700B, np.float32)
    CURRENT_KP              = (0x7010, np.float32)
    CURRENT_KI              = (0x7011, np.float32)
    CURRENT_FILTER_GAIN     = (0x7014, np.float32)
    POSITION_TARGET         = (0x7016, np.float32)
    VELOCITY_LIMIT          = (0x7017, np.float32)
    CURRENT_LIMIT           = (0x7018, np.float32)
    MECHANICAL_POSITION     = (0x7019, np.float32)
    IQ_FILTERED             = (0x701A, np.float32)
    MECHANICAL_VELOCITY     = (0x701B, np.float32)
    VBUS                    = (0x701C, np.float32)
    # ROTATION                = (0x701D, np.float32)
    POSITION_KP             = (0x701E, np.float32)
    VELOCITY_KP             = (0x701F, np.float32)
    VELOCITY_KI             = (0x7020, np.float32)
    VELOCITY_FILTER_GAIN    = (0x7021, np.float32)
    VEL_ACCELERATION_TARGET = (0x7022, np.float32)
    PP_VELOCITY_MAX         = (0x7024, np.float32)
    PP_ACCELERATION_TARGET  = (0x7025, np.float32)
    EPSCAN_TIME             = (0x7026, np.uint16)
    CAN_TIMEOUT             = (0x7028, np.uint32)
    ZERO_STATE              = (0x7029, np.uint8)
    DAMPER                  = (0x702A, np.uint8)
    ADD_OFFSET              = (0x702B, np.float32)