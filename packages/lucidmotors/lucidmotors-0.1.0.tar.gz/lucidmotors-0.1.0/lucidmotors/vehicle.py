"""Lucid vehicle configuration, state and controls."""

from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class AlarmMode(str, Enum):
    ON = "ALARM_ON"
    OFF = "ALARM_OFF"
    SILENT = "ALARM_SILENT"

    def __str__(self) -> str:
        match self:
            case AlarmMode.ON:
                return "On"
            case AlarmMode.OFF:
                return "Off"
            case AlarmMode.SILENT:
                return "Silent"


class AlarmStatus(str, Enum):
    ARMED = "ALARM_ARMED"
    DISABLED = "ALARM_DISABLED"
    # NOTE: I assume there are other values, but I don't know what they are.

    def __str__(self) -> str:
        match self:
            case AlarmStatus.ARMED:
                return "Armed"
            case AlarmStatus.DISABLED:
                return "Disarmed"


class AlarmState(BaseModel):
    mode: AlarmMode = Field(alias="alarmMode")
    status: AlarmStatus = Field(alias="alarmStatus")


class BatteryPreconStatus(str, Enum):
    UNAVAILABLE = "BATTERY_PRECON_UNAVAILABLE"
    OFF = "BATTERY_PRECON_OFF"
    ON = "BATTERY_PRECON_ON"
    # NOTE: I assume there are other values, but I don't know what they are.


class WarningState(str, Enum):
    OFF = "WARNING_OFF"
    ON = "WARNING_ON"
    # TODO: Other values?


class BatteryState(BaseModel):
    health: WarningState = Field(alias="batteryHealth")
    preconditioning_status: BatteryPreconStatus = Field(alias="batteryPreconStatus")
    # NOTE: Need to figure out what this value means by checking while
    # preconditioning is actually turned on in the car.
    preconditioning_time_remaining: Optional[int] = Field(
        alias="batteryPreconTimeRemaining", le=255
    )
    capacity_kwhr: float = Field(alias="capacityKwHr")
    charge_percent: float = Field(alias="chargePercent")
    kwhr: float = Field(alias="kwHr")
    critical_charge_level: WarningState = Field(alias="criticalChargeLevel")
    low_charge_level: WarningState = Field(alias="criticalChargeLevel")
    remaining_range: int = Field(alias="range")
    unavailable_charge_percent: float = Field(alias="unavailableChargePercent")

    @field_validator("preconditioning_time_remaining")
    def preconditioning_time_max_to_empty(cls, v: object) -> object:
        if v == 255:
            return None
        return v


class LockState(str, Enum):
    LOCKED = "LOCKED"
    UNLOCKED = "UNLOCKED"
    # TODO: Other values?


class DoorState(str, Enum):
    CLOSED = "CLOSED"
    AJAR = "AJAR"
    OPEN = "OPEN"
    # TODO: Other values?


class WalkawayState(str, Enum):
    ACTIVE = "WALKAWAY_ACTIVE"
    # TODO: Other values?


class AccessTypeStatus(str, Enum):
    ACTIVE_ACCESS_REQQUEST = "ACTIVE_ACCESS_REQUEST"
    PASSIVE_ACCESS_REQUEST = "PASSIVE_ACCESS_REQUEST"
    # TODO: Other values?


class BodyState(BaseModel):
    # Not sure what this means. Is this the unlocking counterpart to
    # walkawayLockSts maybe?
    access_type_status: AccessTypeStatus = Field(alias="accessTypeSts")
    walkaway_lock_enabled: WalkawayState = Field(alias="walkawayLockSts")
    charge_port: DoorState = Field(alias="chargePortState")
    door_locks: LockState = Field(alias="doorLocks")
    front_cargo: DoorState = Field(alias="frontCargo")
    rear_cargo: DoorState = Field(alias="rearCargo")
    front_left_door: DoorState = Field(alias="frontLeftDoor")
    front_right_door: DoorState = Field(alias="frontRightDoor")
    rear_left_door: DoorState = Field(alias="rearLeftDoor")
    rear_right_door: DoorState = Field(alias="rearRightDoor")


class CabinState(BaseModel):
    exterior_temp_c: float = Field(alias="exteriorTemp")
    interior_temp_c: float = Field(alias="interiorTemp")


class ChargeState(str, Enum):
    NOT_CONNECTED = "NOT_CONNECTED"
    CHARGING = "CHARGING"
    CABLE_CONNECTED = "CONNECTED"
    CHARGE_SUCCESSFUL = "CHARGING_END_OK"
    # TODO: Figure out possible values for this


class EnergyType(str, Enum):
    UNKNOWN = "UNKNOWN_ENERGY_TYPE"
    AC = "AC"
    DC = "DC"
    # TODO: Figure out possible values for this


class ChargeScheduledStatus(str, Enum):
    UNKNOWN = "UNKNOWN_CHARGE_SCHEDULED_STATUS"
    # TODO: Other values?


class ChargingState(BaseModel):
    cable_lock: LockState = Field(alias="cableLock")
    # what unit is this?
    charge_limit: int = Field(alias="chargeLimit")
    charge_limit_percent: float = Field(alias="chargeLimitPercent")
    charge_rate_kwh_precise: float = Field(alias="chargeRateKwhPrecise")
    charge_rate_miles_min_precise: float = Field(alias="chargeRateMilesMinPrecise")
    charge_rate_mph_precise: float = Field(alias="chargeRateMphPrecise")
    charge_scheduled_status: ChargeScheduledStatus = Field(
        alias="chargeScheduledStatus"
    )
    # what unit is this?
    charge_scheduled_time: int = Field(alias="chargeScheduledTime")
    charge_session_kwh: float = Field(alias="chargeSessionKwh")
    charge_session_mi: float = Field(alias="chargeSessionMi")
    charge_state: ChargeState = Field(alias="chargeState")
    energy_type: EnergyType = Field(alias="energyType")
    # TODO: Figure out possible values for this
    # Also, why is there a 'chargeScheduledStatus' and a
    # 'scheduledChargeStatus', what's the difference??
    # scheduled_charge_status: ScheduledChargeStatus
    # TODO: Figure out possible values for this
    # scheduled_charge_unavailable_status: ScheduledChargeUnavailableStatus
    session_minutes_remaining: Optional[int] = Field(
        alias="sessionMinutesRemaining", le=65535
    )

    @field_validator("session_minutes_remaining")
    def session_minutes_remaining_max_to_empty(cls, v: object) -> object:
        if v == 65535:
            return None
        return v


class LightState(str, Enum):
    # NOTE: Switching to DRL in the car is an unknown state.
    UNKNOWN = "UNKNOWN_LIGHTS_STATE"
    OFF = "LIGHTS_OFF"
    ON = "LIGHTS_ON"
    # TODO: Figure out possible values for this


class ChassisState(BaseModel):
    front_left_tire_pressure_bar: float = Field(
        alias="frontLeftTirePressBar", le=6.375000094994903
    )
    front_right_tire_pressure_bar: float = Field(
        alias="frontRightTirePressBar", le=6.375000094994903
    )
    rear_left_tire_pressure_bar: float = Field(
        alias="rearLeftTirePressBar", le=6.375000094994903
    )
    rear_right_tire_pressure_bar: float = Field(
        alias="rearRightTirePressBar", le=6.375000094994903
    )
    headlights: LightState = Field(alias="headlightState")
    indicators: LightState = Field(alias="indicatorState")
    odometer_km: float = Field(alias="odometer")
    software_version: str = Field(alias="softwareVersion")
    # Tire pressure high/low warnings I'm guessing?
    hard_warn_left_front: WarningState = Field(alias="hardWarnLeftFront")
    hard_warn_right_front: WarningState = Field(alias="hardWarnRightFront")
    hard_warn_left_rear: WarningState = Field(alias="hardWarnLeftRear")
    hard_warn_right_rear: WarningState = Field(alias="hardWarnRightRear")
    soft_warn_left_front: WarningState = Field(alias="softWarnLeftFront")
    soft_warn_right_front: WarningState = Field(alias="softWarnRightFront")
    soft_warn_left_rear: WarningState = Field(alias="softWarnLeftRear")
    soft_warn_right_rear: WarningState = Field(alias="softWarnRightRear")

    @field_validator("front_left_tire_pressure_bar")
    def front_left_tp_max_to_empty(cls, v: object) -> object:
        if v == 6.375000094994903:
            return None
        return v

    @field_validator("front_right_tire_pressure_bar")
    def front_right_tp_max_to_empty(cls, v: object) -> object:
        if v == 6.375000094994903:
            return None
        return v

    @field_validator("rear_left_tire_pressure_bar")
    def rear_left_tp_max_to_empty(cls, v: object) -> object:
        if v == 6.375000094994903:
            return None
        return v

    @field_validator("rear_right_tire_pressure_bar")
    def rear_right_tp_max_to_empty(cls, v: object) -> object:
        if v == 6.375000094994903:
            return None
        return v


class DriveMode(str, Enum):
    COMFORT = "DRIVEMODE_COMFORT"
    SWIFT = "DRIVEMODE_SWIFT"
    SPRINT = "DRIVEMODE_SPRINT"
    # Just guessing here
    SAPPHIRE = "DRIVEMODE_SAPPHIRE"
    TRACK = "DRIVEMODE_TRACK"


class GearPosition(str, Enum):
    PARK = "GEAR_PARK"
    NEUTRAL = "GEAR_NEUTRAL"
    DRIVE = "GEAR_DRIVE"
    REVERSE = "GEAR_REVERSE"


class Location(BaseModel):
    latitude: float
    longitude: float


class GPS(BaseModel):
    # TODO: What unit is this? My elevation is around 218 ft and it reads 2760.
    elevation: int
    heading_precise: float = Field(alias="headingPrecise")
    position_time: datetime = Field(alias="positiontime")
    location: Location


class HvacPower(str, Enum):
    OFF = "HVAC_OFF"
    ON = "HVAC_ON"
    PRECONDITION = "HVAC_PRECONDITION"
    # TODO: Other values?


class HvacPreconditionStatus(str, Enum):
    STILL_ACTIVE = "STILL_ACTIVE"
    USER_INPUT = "USER_INPUT"
    # TODO: Other values?


class DefrostState(str, Enum):
    OFF = "DEFROST_OFF"
    ON = "DEFROST_ON"
    # TODO: Other values?


class HvacState(BaseModel):
    defrost: DefrostState
    power: HvacPower = Field(alias="powerMode")
    precondition_status: HvacPreconditionStatus = Field(alias="preconditionStatus")


class PowerState(str, Enum):
    SLEEP = "SLEEP"
    MONITOR = "MONITOR"
    WINK = "WINK"
    DRIVE = "DRIVE"
    ACCESSORY = "ACCESSORY"
    SLEEP_CHARGE = "SLEEP_CHARGE"
    CLOUD_2 = "CLOUD_2"
    # During DC fast charging
    LIVE_CHARGE = "LIVE_CHARGE"
    # Awake and live updating, used for software updates
    LIVE_UPDATE = "LIVE_UPDATE"
    # TODO: Figure out possible values for this


class PrivacyMode(str, Enum):
    CONNECTIVITY_ENABLED = "CONNECTIVITY_ENABLED"
    # TODO: Figure out possible values for this


class UpdateAvailableState(str, Enum):
    UNKNOWN = "UNKNOWN_UPDATE_AVAILABLE"
    UPDATE_AVAILABLE = "UPDATE_AVAILABLE"
    # TODO: Figure out possible values for this


class UpdateState(str, Enum):
    UPDATE_FAILED_DRIVE_ALLOWED = "UPDATE_FAILED_DRIVE_ALLOWED"
    UNKNOWN = "UNKNOWN_UPDATE_STATE"
    IN_PROGRESS = "IN_PROGRESS"
    # TODO: Figure out possible values for this


class RollbackState(str, Enum):
    UNKNOWN = "UNKNOWN_ROLLBACK_STATE"
    # TODO: Figure out possible values for this


class SoftwareUpdateState(BaseModel):
    install_duration_minutes: int = Field(alias="installDurationMinutes")
    percent_complete: int = Field(alias="percentComplete")
    rollback_percent_complete: int = Field(alias="rollbackPercentComplete")
    rollback_state: RollbackState = Field(alias="rollbackState")
    # what is this? it's 0 for me. maybe epoch, maybe seconds/minutes in the
    # future?
    scheduled_start_time_sec: int = Field(alias="scheduledStartTimeSec")
    update_available: UpdateAvailableState = Field(alias="updateAvailable")
    state: UpdateState = Field(alias="updateState")
    version_available: str = Field(alias="versionAvailable")
    version_available_raw: int = Field(alias="versionAvailableRaw")


class InternetStatus(str, Enum):
    INTERNET_ACCESS = "INTERNET_ACCESS"
    NO_INTERNET_ACCESS = "NO_INTERNET_ACCESS"


class LteType(str, Enum):
    UNKNOWN = "UNKNOWN_INTERNET_TYPE"
    FOUR_G_LTE = "FOUR_G_LTE"
    # TODO: Figure out possible values for this


class TcuInternetState(BaseModel):
    lte_rssi: int = Field(alias="lteRssi")
    lte_status: InternetStatus = Field(alias="lteStatus")
    lte_type: LteType = Field(alias="lteType")
    wifi_rssi: int = Field(alias="wifiRssi")
    wifi_status: InternetStatus = Field(alias="wifiStatus")


class TcuState(str, Enum):
    DROWSY = "TCU_DROWSY"
    FULL = "TCU_FULL"
    SLEEP = "TCU_SLEEP"
    FACTORY = "TCU_FACTORY"
    UNKNOWN = "UNKNOWN_TCU_STATE"
    # TODO: Figure out possible values for this


class CloudConnectionState(str, Enum):
    CONNECTED = "CLOUD_CONNECTED"
    DISCONNECTED = "CLOUD_DISCONNECTED"
    # TODO: Figure out possible values for this


class KeylessDrivingState(str, Enum):
    OFF = "KEYLESS_OFF"
    # TODO: Figure out possible values for this


class VehicleState(BaseModel):
    alarm: AlarmState = Field(alias="alarmState")
    battery: BatteryState = Field(alias="batteryState")
    body: BodyState = Field(alias="bodyState")
    cabin: CabinState = Field(alias="cabinState")
    charging: ChargingState = Field(alias="chargingState")
    chassis: ChassisState = Field(alias="chassisState")
    cloud_connection: CloudConnectionState = Field(alias="cloudConnectionState")
    drive_mode: DriveMode = Field(alias="driveMode")
    gear_position: GearPosition = Field(alias="gearPosition")
    gps: GPS = Field(alias="gps")
    hvac: HvacState = Field(alias="hvacStatus")
    keyless_driving: KeylessDrivingState = Field(alias="keylessDrivingState")
    last_updated: datetime = Field(alias="lastUpdatedMs")
    # TODO:
    # mobile_app_request: MobileAppRequestState
    power: PowerState = Field(alias="powerState")
    privacy_mode: PrivacyMode = Field(alias="privacyMode")
    software_update: SoftwareUpdateState = Field(alias="softwareUpdate")
    tcu_internet: TcuInternetState = Field(alias="tcuInternetStatus")
    tcu: TcuState = Field(alias="tcuState")


class PaintColor(str, Enum):
    FATHOM_BLUE = 'FATHOM_BLUE'
    ZENITH_RED = 'ZENITH_RED'
    STELLAR_WHITE = 'STELLAR_WHITE'
    INFINITE_BLACK = 'INFINITE_BLACK'
    EUREKA_GOLD = 'EUREKA_GOLD'
    COSMOS_SILVER = 'COSMOS_SILVER'
    QUANTUM_GREY = 'QUANTUM_GREY'
    # Guessing with these
    SAPPHIRE_BLUE = 'SAPPHIRE_BLUE'


class FrunkStrutType(str, Enum):
    POWER_STRUT = 'POWER_STRUT'
    GAS_STRUT = 'GAS_STRUT'


class Interior(str, Enum):
    SANTA_MONICA = 'SANTA_MONICA'
    TAHOE = 'TAHOE'
    MOJAVE = 'MOJAVE'
    # Guessing with these
    SANTA_CRUZ = 'SANTA_CRUZ'
    # TODO: mojave purluxe? mojave purluxe leather alternative? sapphire mojave?


class Look(str, Enum):
    PLATINUM = 'PLATINUM'
    STEALTH = 'STEALTH'


class Model(str, Enum):
    AIR = "AIR"
    GRAVITY = "GRAVITY"

    def __str__(self) -> str:
        match self:
            case Model.AIR:
                return "Air"
            case Model.GRAVITY:
                return "Gravity"


class ModelVariant(str, Enum):
    DREAM_EDITION = 'DREAM_EDITION'
    TOURING = 'TOURING'
    PURE = 'PURE'
    GRAND_TOURING = 'GRAND_TOURING'
    # Guessing at the rest
    SAPPHIRE = 'SAPPHIRE'

    def __str__(self) -> str:
        match self:
            case ModelVariant.DREAM_EDITION:
                return "Dream Edition"
            case ModelVariant.TOURING:
                return "Touring"
            case ModelVariant.PURE:
                return "Pure"
            case ModelVariant.GRAND_TOURING:
                return "Grand Touring"
            case ModelVariant.SAPPHIRE:
                return "Sapphire"


class Edition(str, Enum):
    PERFORMANCE_EDITION = 'EDITION_PERFORMANCE'
    RANGE_EDITION = 'EDITION_RANGE'
    STANDARD_EDITION = 'EDITION_STANDARD'


class Wheels(str, Enum):
    DREAM = 'DREAM'
    RANGE = 'RANGE'
    PERFORMANCE = 'PERFORMANCE'
    BLADE = 'BLADE'


class Battery(str, Enum):
    # Absolutely no idea what these mean, but I know they're accurate!
    BATTERY_TYPE_01 = 'BATTERY_TYPE_01'  # Pure battery?
    BATTERY_TYPE_02 = 'BATTERY_TYPE_02'  # GT Battery?
    BATTERY_TYPE_03 = 'BATTERY_TYPE_03'
    BATTERY_TYPE_04 = 'BATTERY_TYPE_04'
    BATTERY_TYPE_05 = 'BATTERY_TYPE_05'  # Dream battery


class VehicleConfig(BaseModel):
    country_code: str = Field(alias="countryCode")
    exterior_color_code: str = Field(alias="exteriorColorCode")
    frunk_strut: FrunkStrutType = Field(alias="frunkStrut")
    interior: Interior = Field(alias="interior")
    interior_color_code: str = Field(alias="interiorColorCode")
    look: Look = Field(alias="look")
    model: Model
    variant: ModelVariant = Field(alias="modelVariant")
    edition: Edition = Field(alias="edition")
    battery: Battery = Field(alias="battery")
    nickname: str
    # TODO: Enum-ize?
    paint_color: PaintColor = Field(alias="paintColor")
    region_code: str = Field(alias="regionCode")
    vin: str
    wheels: Wheels = Field(alias="wheels")


class AccessLevel(str, Enum):
    PRIMARY_OWNER = "PRIMARY_OWNER"
    # TODO: Figure out possible values for this


class Vehicle(BaseModel):
    access_level: AccessLevel = Field(alias="accessLevel")
    vehicle_id: str = Field(alias="vehicleId")
    config: VehicleConfig = Field(alias="vehicleConfig")
    state: VehicleState = Field(alias="vehicleState")
