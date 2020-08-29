# AUTOGENERATED, DO NOT EDIT

from .structs import (
    SelectedRTPStreamConfiguration,
    StreamingStatus,
    SupportedAudioStreamConfiguration,
    SupportedRTPConfiguration,
    SupportedVideoStreamConfiguration,
)

characteristics = {
    "000000A6-0000-1000-8000-0026BB765291": {
        "name": "ACCESSORY_FLAGS",
        "description": "Accessory Flags",
        "perms": ["pr", "ev"],
        "format": "uint32",
    },
    "000000B0-0000-1000-8000-0026BB765291": {
        "name": "ACTIVE",
        "description": "Active",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "00000001-0000-1000-8000-0026BB765291": {
        "name": "ADMINISTRATOR_ONLY_ACCESS",
        "description": "Administrator Only Access",
        "perms": ["pr", "pw", "ev"],
        "format": "bool",
    },
    "00000064-0000-1000-8000-0026BB765291": {
        "name": "AIR_PARTICULATE_DENSITY",
        "description": "Air Particulate Density",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 1000,
        "min_value": 0,
        "step_value": 1,
    },
    "00000065-0000-1000-8000-0026BB765291": {
        "name": "AIR_PARTICULATE_SIZE",
        "description": "Air Particulate Size",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000095-0000-1000-8000-0026BB765291": {
        "name": "AIR_QUALITY",
        "description": "Air Quality",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000005-0000-1000-8000-0026BB765291": {
        "name": "AUDIO_FEEDBACK",
        "description": "Audio Feedback",
        "perms": ["pr", "pw", "ev"],
        "format": "bool",
    },
    "00000068-0000-1000-8000-0026BB765291": {
        "name": "BATTERY_LEVEL",
        "description": "Battery Level",
        "perms": ["pr", "ev"],
        "format": "uint8",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "00000008-0000-1000-8000-0026BB765291": {
        "name": "BRIGHTNESS",
        "description": "Brightness",
        "perms": ["pr", "pw", "ev"],
        "format": "int32",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "00000092-0000-1000-8000-0026BB765291": {
        "name": "CARBON_DIOXIDE_DETECTED",
        "description": "Carbon Dioxide Detected",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000093-0000-1000-8000-0026BB765291": {
        "name": "CARBON_DIOXIDE_LEVEL",
        "description": "Carbon Dioxide Level",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 100000,
        "min_value": 0,
    },
    "00000094-0000-1000-8000-0026BB765291": {
        "name": "CARBON_DIOXIDE_PEAK_LEVEL",
        "description": "Carbon Dioxide Peak Level",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 100000,
        "min_value": 0,
    },
    "00000069-0000-1000-8000-0026BB765291": {
        "name": "CARBON_MONOXIDE_DETECTED",
        "description": "Carbon Monoxide Detected",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000090-0000-1000-8000-0026BB765291": {
        "name": "CARBON_MONOXIDE_LEVEL",
        "description": "Carbon Monoxide Level",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 100,
        "min_value": 0,
    },
    "00000091-0000-1000-8000-0026BB765291": {
        "name": "CARBON_MONOXIDE_PEAK_LEVEL",
        "description": "Carbon Monoxide Peak Level",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 100,
        "min_value": 0,
    },
    "0000008F-0000-1000-8000-0026BB765291": {
        "name": "CHARGING_STATE",
        "description": "Charging State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "000000CE-0000-1000-8000-0026BB765291": {
        "name": "COLOR_TEMPERATURE",
        "description": "Color Temperature",
        "perms": ["pr", "pw", "ev"],
        "format": "uint32",
        "max_value": 500,
        "min_value": 140,
        "step_value": 1,
    },
    "0000006A-0000-1000-8000-0026BB765291": {
        "name": "CONTACT_SENSOR_STATE",
        "description": "Contact Sensor State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "0000000D-0000-1000-8000-0026BB765291": {
        "name": "COOLING_THRESHOLD_TEMPERATURE",
        "description": "Cooling Threshold Temperature",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "celsius",
        "max_value": 35,
        "min_value": 10,
        "step_value": 0.1,
    },
    "000000A9-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_AIR_PURIFIER_STATE",
        "description": "Current Air Purifier State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "0000006B-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_AMBIENT_LIGHT_LEVEL",
        "description": "Current Ambient Light Level",
        "perms": ["pr", "ev"],
        "format": "float",
        "unit": "lux",
        "max_value": 100000,
        "min_value": 0.0001,
    },
    "0000000E-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_DOOR_STATE",
        "description": "Current Door State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "000000AF-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_FAN_STATE",
        "description": "Current Fan State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "000000B1-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_HEATER_COOLER_STATE",
        "description": "Current Heater Cooler State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "0000000F-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_HEATING_COOLING_STATE",
        "description": "Current Heating Cooling State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "0000006C-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_HORIZONTAL_TILT_ANGLE",
        "description": "Current Horizontal Tilt Angle",
        "perms": ["pr", "ev"],
        "format": "int32",
        "unit": "arcdegrees",
        "max_value": 90,
        "min_value": -90,
        "step_value": 1,
    },
    "000000B3-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_HUMIDIFIER_DEHUMIDIFIER_STATE",
        "description": "Current Humidifier Dehumidifier State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "0000006D-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_POSITION",
        "description": "Current Position",
        "perms": ["pr", "ev"],
        "format": "uint8",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "00000010-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_RELATIVE_HUMIDITY",
        "description": "Current Relative Humidity",
        "perms": ["pr", "ev"],
        "format": "float",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "000000AA-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_SLAT_STATE",
        "description": "Current Slat State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000011-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_TEMPERATURE",
        "description": "Current Temperature",
        "perms": ["pr", "ev"],
        "format": "float",
        "unit": "celsius",
        "max_value": 100,
        "min_value": 0,
        "step_value": 0.1,
    },
    "000000C1-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_TILT_ANGLE",
        "description": "Current Tilt Angle",
        "perms": ["pr", "ev"],
        "format": "int32",
        "unit": "arcdegrees",
        "max_value": 90,
        "min_value": -90,
        "step_value": 1,
    },
    "0000006E-0000-1000-8000-0026BB765291": {
        "name": "CURRENT_VERTICAL_TILT_ANGLE",
        "description": "Current Vertical Tilt Angle",
        "perms": ["pr", "ev"],
        "format": "int32",
        "unit": "arcdegrees",
        "max_value": 90,
        "min_value": -90,
        "step_value": 1,
    },
    "0000011D-0000-1000-8000-0026BB765291": {
        "name": "DIGITAL_ZOOM",
        "description": "Digital Zoom",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
    },
    "000000AC-0000-1000-8000-0026BB765291": {
        "name": "FILTER_CHANGE_INDICATION",
        "description": "Filter Change Indication",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "000000AB-0000-1000-8000-0026BB765291": {
        "name": "FILTER_LIFE_LEVEL",
        "description": "Filter Life Level",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 100,
        "min_value": 0,
    },
    "00000052-0000-1000-8000-0026BB765291": {
        "name": "FIRMWARE_REVISION",
        "description": "Firmware Revision",
        "perms": ["pr"],
        "format": "string",
    },
    "00000053-0000-1000-8000-0026BB765291": {
        "name": "HARDWARE_REVISION",
        "description": "Hardware Revision",
        "perms": ["pr"],
        "format": "string",
    },
    "00000012-0000-1000-8000-0026BB765291": {
        "name": "HEATING_THRESHOLD_TEMPERATURE",
        "description": "Heating Threshold Temperature",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "celsius",
        "max_value": 25,
        "min_value": 0,
        "step_value": 0.1,
    },
    "0000006F-0000-1000-8000-0026BB765291": {
        "name": "HOLD_POSITION",
        "description": "Hold Position",
        "perms": ["pw"],
        "format": "bool",
    },
    "00000013-0000-1000-8000-0026BB765291": {
        "name": "HUE",
        "description": "Hue",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "arcdegrees",
        "max_value": 360,
        "min_value": 0,
        "step_value": 1,
    },
    "00000014-0000-1000-8000-0026BB765291": {
        "name": "IDENTIFY",
        "description": "Identify",
        "perms": ["pw"],
        "format": "bool",
    },
    "0000011F-0000-1000-8000-0026BB765291": {
        "name": "IMAGE_MIRRORING",
        "description": "Image Mirroring",
        "perms": ["pr", "pw", "ev"],
        "format": "bool",
    },
    "0000011E-0000-1000-8000-0026BB765291": {
        "name": "IMAGE_ROTATION",
        "description": "Image Rotation",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "arcdegrees",
        "max_value": 270,
        "min_value": 0,
        "step_value": 90,
    },
    "000000D2-0000-1000-8000-0026BB765291": {
        "name": "IN_USE",
        "description": "In Use",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "000000D6-0000-1000-8000-0026BB765291": {
        "name": "IS_CONFIGURED",
        "description": "Is Configured",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "00000070-0000-1000-8000-0026BB765291": {
        "name": "LEAK_DETECTED",
        "description": "Leak Detected",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000019-0000-1000-8000-0026BB765291": {
        "name": "LOCK_CONTROL_POINT",
        "description": "Lock Control Point",
        "perms": ["pw"],
        "format": "tlv8",
    },
    "0000001D-0000-1000-8000-0026BB765291": {
        "name": "LOCK_CURRENT_STATE",
        "description": "Lock Current State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "0000001C-0000-1000-8000-0026BB765291": {
        "name": "LOCK_LAST_KNOWN_ACTION",
        "description": "Lock Last Known Action",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "0000001A-0000-1000-8000-0026BB765291": {
        "name": "LOCK_MANAGEMENT_AUTO_SECURITY_TIMEOUT",
        "description": "Lock Management Auto Security Timeout",
        "perms": ["pr", "pw", "ev"],
        "format": "uint32",
        "unit": "seconds",
    },
    "000000A7-0000-1000-8000-0026BB765291": {
        "name": "LOCK_PHYSICAL_CONTROLS",
        "description": "Lock Physical Controls",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "0000001E-0000-1000-8000-0026BB765291": {
        "name": "LOCK_TARGET_STATE",
        "description": "Lock Target State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "0000001F-0000-1000-8000-0026BB765291": {
        "name": "LOGS",
        "description": "Logs",
        "perms": ["pr", "ev"],
        "format": "tlv8",
    },
    "00000020-0000-1000-8000-0026BB765291": {
        "name": "MANUFACTURER",
        "description": "Manufacturer",
        "perms": ["pr"],
        "format": "string",
    },
    "00000021-0000-1000-8000-0026BB765291": {
        "name": "MODEL",
        "description": "Model",
        "perms": ["pr"],
        "format": "string",
    },
    "00000022-0000-1000-8000-0026BB765291": {
        "name": "MOTION_DETECTED",
        "description": "Motion Detected",
        "perms": ["pr", "ev"],
        "format": "bool",
    },
    "0000011A-0000-1000-8000-0026BB765291": {
        "name": "MUTE",
        "description": "Mute",
        "perms": ["pr", "pw", "ev"],
        "format": "bool",
    },
    "00000023-0000-1000-8000-0026BB765291": {
        "name": "NAME",
        "description": "Name",
        "perms": ["pr"],
        "format": "string",
    },
    "0000011B-0000-1000-8000-0026BB765291": {
        "name": "NIGHT_VISION",
        "description": "Night Vision",
        "perms": ["pr", "pw", "ev"],
        "format": "bool",
    },
    "000000C4-0000-1000-8000-0026BB765291": {
        "name": "NITROGEN_DIOXIDE_DENSITY",
        "description": "Nitrogen Dioxide Density",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 1000,
        "min_value": 0,
        "step_value": 1,
    },
    "00000024-0000-1000-8000-0026BB765291": {
        "name": "OBSTRUCTION_DETECTED",
        "description": "Obstruction Detected",
        "perms": ["pr", "ev"],
        "format": "bool",
    },
    "00000071-0000-1000-8000-0026BB765291": {
        "name": "OCCUPANCY_DETECTED",
        "description": "Occupancy Detected",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000025-0000-1000-8000-0026BB765291": {
        "name": "ON",
        "description": "On",
        "perms": ["pr", "pw", "ev"],
        "format": "bool",
    },
    "0000011C-0000-1000-8000-0026BB765291": {
        "name": "OPTICAL_ZOOM",
        "description": "Optical Zoom",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
    },
    "00000026-0000-1000-8000-0026BB765291": {
        "name": "OUTLET_IN_USE",
        "description": "Outlet In Use",
        "perms": ["pr", "ev"],
        "format": "bool",
    },
    "000000C3-0000-1000-8000-0026BB765291": {
        "name": "OZONE_DENSITY",
        "description": "Ozone Density",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 1000,
        "min_value": 0,
        "step_value": 1,
    },
    "0000004C-0000-1000-8000-0026BB765291": {
        "name": "PAIR_SETUP",
        "description": "Pair Setup",
        "perms": ["pr", "pw"],
        "format": "tlv8",
    },
    "0000004E-0000-1000-8000-0026BB765291": {
        "name": "PAIR_VERIFY",
        "description": "Pair Verify",
        "perms": ["pr", "pw"],
        "format": "tlv8",
    },
    "0000004F-0000-1000-8000-0026BB765291": {
        "name": "PAIRING_FEATURES",
        "description": "Pairing Features",
        "perms": ["pr"],
        "format": "uint8",
    },
    "00000050-0000-1000-8000-0026BB765291": {
        "name": "PAIRING_PAIRINGS",
        "description": "Pairing Pairings",
        "perms": ["pr", "pw"],
        "format": "tlv8",
    },
    "000000C7-0000-1000-8000-0026BB765291": {
        "name": "PM10_DENSITY",
        "description": "PM10 Density",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 1000,
        "min_value": 0,
        "step_value": 1,
    },
    "000000C6-0000-1000-8000-0026BB765291": {
        "name": "PM2_5_DENSITY",
        "description": "PM2.5 Density",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 1000,
        "min_value": 0,
        "step_value": 1,
    },
    "00000072-0000-1000-8000-0026BB765291": {
        "name": "POSITION_STATE",
        "description": "Position State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "000000D1-0000-1000-8000-0026BB765291": {
        "name": "PROGRAM_MODE",
        "description": "Program Mode",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000073-0000-1000-8000-0026BB765291": {
        "name": "PROGRAMMABLE_SWITCH_EVENT",
        "description": "Programmable Switch Event",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "000000C9-0000-1000-8000-0026BB765291": {
        "name": "RELATIVE_HUMIDITY_DEHUMIDIFIER_THRESHOLD",
        "description": "Relative Humidity Dehumidifier Threshold",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "000000CA-0000-1000-8000-0026BB765291": {
        "name": "RELATIVE_HUMIDITY_HUMIDIFIER_THRESHOLD",
        "description": "Relative Humidity Humidifier Threshold",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "000000D4-0000-1000-8000-0026BB765291": {
        "name": "REMAINING_DURATION",
        "description": "Remaining Duration",
        "perms": ["pr", "ev"],
        "format": "uint32",
        "max_value": 3600,
        "min_value": 0,
        "step_value": 1,
    },
    "000000AD-0000-1000-8000-0026BB765291": {
        "name": "RESET_FILTER_INDICATION",
        "description": "Reset Filter Indication",
        "perms": ["pw"],
        "format": "uint8",
        "max_value": 1,
        "min_value": 1,
        "step_value": 1,
    },
    "00000028-0000-1000-8000-0026BB765291": {
        "name": "ROTATION_DIRECTION",
        "description": "Rotation Direction",
        "perms": ["pr", "pw", "ev"],
        "format": "int32",
    },
    "00000029-0000-1000-8000-0026BB765291": {
        "name": "ROTATION_SPEED",
        "description": "Rotation Speed",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "0000002F-0000-1000-8000-0026BB765291": {
        "name": "SATURATION",
        "description": "Saturation",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "0000008E-0000-1000-8000-0026BB765291": {
        "name": "SECURITY_SYSTEM_ALARM_TYPE",
        "description": "Security System Alarm Type",
        "perms": ["pr", "ev"],
        "format": "uint8",
        "max_value": 1,
        "min_value": 0,
        "step_value": 1,
    },
    "00000066-0000-1000-8000-0026BB765291": {
        "name": "SECURITY_SYSTEM_CURRENT_STATE",
        "description": "Security System Current State",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000067-0000-1000-8000-0026BB765291": {
        "name": "SECURITY_SYSTEM_TARGET_STATE",
        "description": "Security System Target State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "00000117-0000-1000-8000-0026BB765291": {
        "name": "SELECTED_RTP_STREAM_CONFIGURATION",
        "description": "Selected RTP Stream Configuration",
        "perms": ["pr", "pw"],
        "format": "tlv8",
        "struct": SelectedRTPStreamConfiguration,
    },
    "00000030-0000-1000-8000-0026BB765291": {
        "name": "SERIAL_NUMBER",
        "description": "Serial Number",
        "perms": ["pr"],
        "format": "string",
    },
    "000000CB-0000-1000-8000-0026BB765291": {
        "name": "SERVICE_LABEL_INDEX",
        "description": "Service Label Index",
        "perms": ["pr"],
        "format": "uint8",
        "max_value": 255,
        "min_value": 1,
        "step_value": 1,
    },
    "000000CD-0000-1000-8000-0026BB765291": {
        "name": "SERVICE_LABEL_NAMESPACE",
        "description": "Service Label Namespace",
        "perms": ["pr"],
        "format": "uint8",
    },
    "000000D3-0000-1000-8000-0026BB765291": {
        "name": "SET_DURATION",
        "description": "Set Duration",
        "perms": ["pr", "pw", "ev"],
        "format": "uint32",
        "max_value": 3600,
        "min_value": 0,
        "step_value": 1,
    },
    "00000118-0000-1000-8000-0026BB765291": {
        "name": "SETUP_ENDPOINTS",
        "description": "Setup Endpoints",
        "perms": ["pr", "pw"],
        "format": "tlv8",
    },
    "000000C0-0000-1000-8000-0026BB765291": {
        "name": "SLAT_TYPE",
        "description": "Slat Type",
        "perms": ["pr"],
        "format": "uint8",
    },
    "00000076-0000-1000-8000-0026BB765291": {
        "name": "SMOKE_DETECTED",
        "description": "Smoke Detected",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000075-0000-1000-8000-0026BB765291": {
        "name": "STATUS_ACTIVE",
        "description": "Status Active",
        "perms": ["pr", "ev"],
        "format": "bool",
    },
    "00000077-0000-1000-8000-0026BB765291": {
        "name": "STATUS_FAULT",
        "description": "Status Fault",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000078-0000-1000-8000-0026BB765291": {
        "name": "STATUS_JAMMED",
        "description": "Status Jammed",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000079-0000-1000-8000-0026BB765291": {
        "name": "STATUS_LOW_BATTERY",
        "description": "Status Low Battery",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "0000007A-0000-1000-8000-0026BB765291": {
        "name": "STATUS_TAMPERED",
        "description": "Status Tampered",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000120-0000-1000-8000-0026BB765291": {
        "name": "STREAMING_STATUS",
        "description": "Streaming Status",
        "perms": ["pr", "ev"],
        "format": "tlv8",
        "struct": StreamingStatus,
    },
    "000000C5-0000-1000-8000-0026BB765291": {
        "name": "SULPHUR_DIOXIDE_DENSITY",
        "description": "Sulphur Dioxide Density",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 1000,
        "min_value": 0,
        "step_value": 1,
    },
    "00000115-0000-1000-8000-0026BB765291": {
        "name": "SUPPORTED_AUDIO_STREAM_CONFIGURATION",
        "description": "Supported Audio Stream Configuration",
        "perms": ["pr"],
        "format": "tlv8",
        "struct": SupportedAudioStreamConfiguration,
    },
    "00000116-0000-1000-8000-0026BB765291": {
        "name": "SUPPORTED_RTP_CONFIGURATION",
        "description": "Supported RTP Configuration",
        "perms": ["pr"],
        "format": "tlv8",
        "struct": SupportedRTPConfiguration,
        "array": True,
    },
    "00000114-0000-1000-8000-0026BB765291": {
        "name": "SUPPORTED_VIDEO_STREAM_CONFIGURATION",
        "description": "Supported Video Stream Configuration",
        "perms": ["pr"],
        "format": "tlv8",
        "struct": SupportedVideoStreamConfiguration,
    },
    "000000B6-0000-1000-8000-0026BB765291": {
        "name": "SWING_MODE",
        "description": "Swing Mode",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "000000A8-0000-1000-8000-0026BB765291": {
        "name": "TARGET_AIR_PURIFIER_STATE",
        "description": "Target Air Purifier State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "000000AE-0000-1000-8000-0026BB765291": {
        "name": "TARGET_AIR_QUALITY",
        "description": "Target Air Quality",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "00000032-0000-1000-8000-0026BB765291": {
        "name": "TARGET_DOOR_STATE",
        "description": "Target Door State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "000000BF-0000-1000-8000-0026BB765291": {
        "name": "TARGET_FAN_STATE",
        "description": "Target Fan State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "000000B2-0000-1000-8000-0026BB765291": {
        "name": "TARGET_HEATER_COOLER_STATE",
        "description": "Target Heater Cooler State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "00000033-0000-1000-8000-0026BB765291": {
        "name": "TARGET_HEATING_COOLING_STATE",
        "description": "Target Heating Cooling State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "0000007B-0000-1000-8000-0026BB765291": {
        "name": "TARGET_HORIZONTAL_TILT_ANGLE",
        "description": "Target Horizontal Tilt Angle",
        "perms": ["pr", "pw", "ev"],
        "format": "int32",
        "unit": "arcdegrees",
        "max_value": 90,
        "min_value": -90,
        "step_value": 1,
    },
    "000000B4-0000-1000-8000-0026BB765291": {
        "name": "TARGET_HUMIDIFIER_DEHUMIDIFIER_STATE",
        "description": "Target Humidifier Dehumidifier State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "0000007C-0000-1000-8000-0026BB765291": {
        "name": "TARGET_POSITION",
        "description": "Target Position",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "00000034-0000-1000-8000-0026BB765291": {
        "name": "TARGET_RELATIVE_HUMIDITY",
        "description": "Target Relative Humidity",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "000000BE-0000-1000-8000-0026BB765291": {
        "name": "TARGET_SLAT_STATE",
        "description": "Target Slat State",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "00000035-0000-1000-8000-0026BB765291": {
        "name": "TARGET_TEMPERATURE",
        "description": "Target Temperature",
        "perms": ["pr", "pw", "ev"],
        "format": "float",
        "unit": "celsius",
        "max_value": 38,
        "min_value": 10,
        "step_value": 0.1,
    },
    "000000C2-0000-1000-8000-0026BB765291": {
        "name": "TARGET_TILT_ANGLE",
        "description": "Target Tilt Angle",
        "perms": ["pr", "pw", "ev"],
        "format": "int32",
        "unit": "arcdegrees",
        "max_value": 90,
        "min_value": -90,
        "step_value": 1,
    },
    "0000007D-0000-1000-8000-0026BB765291": {
        "name": "TARGET_VERTICAL_TILT_ANGLE",
        "description": "Target Vertical Tilt Angle",
        "perms": ["pr", "pw", "ev"],
        "format": "int32",
        "unit": "arcdegrees",
        "max_value": 90,
        "min_value": -90,
        "step_value": 1,
    },
    "00000036-0000-1000-8000-0026BB765291": {
        "name": "TEMPERATURE_DISPLAY_UNITS",
        "description": "Temperature Display Units",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
    },
    "000000D5-0000-1000-8000-0026BB765291": {
        "name": "VALVE_TYPE",
        "description": "Valve Type",
        "perms": ["pr", "ev"],
        "format": "uint8",
    },
    "00000037-0000-1000-8000-0026BB765291": {
        "name": "VERSION",
        "description": "Version",
        "perms": ["pr", "ev"],
        "format": "string",
    },
    "000000C8-0000-1000-8000-0026BB765291": {
        "name": "VOC_DENSITY",
        "description": "VOC Density",
        "perms": ["pr", "ev"],
        "format": "float",
        "max_value": 1000,
        "min_value": 0,
        "step_value": 1,
    },
    "00000119-0000-1000-8000-0026BB765291": {
        "name": "VOLUME",
        "description": "Volume",
        "perms": ["pr", "pw", "ev"],
        "format": "uint8",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
        "step_value": 1,
    },
    "000000B5-0000-1000-8000-0026BB765291": {
        "name": "WATER_LEVEL",
        "description": "Water Level",
        "perms": ["pr", "ev"],
        "format": "float",
        "unit": "percentage",
        "max_value": 100,
        "min_value": 0,
    },
}
