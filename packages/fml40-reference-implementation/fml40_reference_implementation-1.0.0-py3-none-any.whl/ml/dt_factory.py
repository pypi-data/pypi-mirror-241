""" This module implements a factory for managing and creating Digital Twins according to Forest Modeling Language 4.0."""

from ml.app_logger import APP_LOGGER
from ml.tools import remove_namespace, check_var_conflict
from ml.ditto_feature import DittoFeature
import sys
import inspect
from ml.parameters import Parameters
from ml.entry import Entry
from ml.thing import Thing
from ml.ml40.roles.services.service import Service
from ml.ml40.roles.services.openweather_service import OpenWeatherService
from ml.ml40.roles.hmis.app import App
from ml.ml40.roles.hmis.dashboard import Dashboard
from ml.ml40.roles.hmis.machine_ui import MachineUI
from ml.ml40.roles.hmis.hmd import HMD
from ml.ml40.roles.hmis.hmi import HMI
from ml.ml40.roles.dts.handheld_devices.handheld_device import HandheldDevice
from ml.ml40.roles.dts.machines.machine import Machine
from ml.ml40.roles.dts.organisations.organisation import Organisation
from ml.ml40.roles.dts.organisations.forwarding_agency import ForwardingAgency
from ml.ml40.roles.dts.organisations.funding_agency import FundingAgency
from ml.ml40.roles.dts.organisations.production_team import ProductionTeam
from ml.ml40.roles.dts.organisations.supplier import Supplier
from ml.ml40.roles.dts.parts.chain import Chain
from ml.ml40.roles.dts.parts.crane import Crane
from ml.ml40.roles.dts.parts.part import Part
from ml.ml40.roles.dts.parts.engine import Engine
from ml.ml40.roles.dts.parts.scale import Scale
from ml.ml40.roles.dts.parts.tank import Tank
from ml.ml40.roles.dts.parts.winch import Winch
from ml.ml40.roles.dts.parts.wheel import Wheel
from ml.ml40.roles.dts.persons.machine_operator import MachineOperator
from ml.ml40.roles.dts.persons.person import Person
from ml.ml40.roles.dts.persons.precinct_leader import PrecinctLeader
from ml.ml40.roles.dts.sensors.sensor import Sensor
from ml.ml40.roles.dts.sensors.air_sensor import AirSensor
from ml.ml40.roles.dts.sensors.accelerometer import Accelerometer
from ml.ml40.roles.dts.sensors.counter_sensor import CounterSensor
from ml.ml40.roles.dts.sensors.gyroscope import Gyroscope
from ml.ml40.roles.dts.sensors.high_speed_camera import HighSpeedCamera
from ml.ml40.roles.dts.sensors.imu import IMU
from ml.ml40.roles.dts.sensors.laser_range_finder import LaserRangeFinder
from ml.ml40.roles.dts.sensors.lidar import LiDAR
from ml.ml40.roles.dts.sensors.pressure_sensor import PressureSensor
from ml.ml40.roles.dts.sensors.sensor import Sensor
from ml.ml40.roles.dts.sensors.soil_sensor import SoilSensor
from ml.ml40.roles.dts.sensors.sound_sensor import SoundSensor
from ml.ml40.roles.dts.sensors.stereo_camera import StereoCamera
from ml.ml40.roles.dts.sensors.temperature_sensor import TemperatureSensor
from ml.ml40.roles.dts.sensors.vehicle_counter_sensor import VehicleCounterSensor
from ml.ml40.roles.dts.sites.site import Site
from ml.ml40.roles.dts.sites.laboratory import Laboratory
from ml.ml40.roles.dts.ways.way import Way

from ml.fml40.roles.dts.handheld_devices.brushcutter import Brushcutter
from ml.fml40.roles.dts.handheld_devices.chainsaw import Chainsaw
from ml.fml40.roles.dts.machines.forest_machine import ForestMachine
from ml.fml40.roles.dts.machines.forwarder import Forwarder
from ml.fml40.roles.dts.machines.harvester import Harvester
from ml.fml40.roles.dts.machines.log_truck import LogTruck
from ml.fml40.roles.dts.machines.mini_tractor import MiniTractor
from ml.fml40.roles.dts.machines.skidder import Skidder
from ml.fml40.roles.dts.machines.wheel_loader import WheelLoader
from ml.fml40.roles.dts.parts.band import Band
from ml.fml40.roles.dts.parts.clam_bunk import ClamBunk
from ml.fml40.roles.dts.parts.front_bogie_lift import FrontBogieLift
from ml.fml40.roles.dts.parts.grabber import Grabber
from ml.fml40.roles.dts.parts.harvesting_head import HarvestingHead
from ml.fml40.roles.dts.parts.log_loading_area import LogLoadingArea
from ml.fml40.roles.dts.parts.log_truck_scale import LogTruckScale
from ml.fml40.roles.dts.parts.log_storage_box import LogStorageBox
from ml.fml40.roles.dts.parts.rear_bogie_lift import RearBogieLift
from ml.fml40.roles.dts.parts.rung_basket import RungBasket
from ml.fml40.roles.dts.parts.saw import Saw
from ml.fml40.roles.dts.parts.mill_gate import MillGate
from ml.fml40.roles.dts.parts.skidding_winch import SkiddingWinch
from ml.fml40.roles.dts.parts.stacking_shield import StackingShield
from ml.fml40.roles.dts.parts.traction_winch import TractionWinch
from ml.fml40.roles.dts.persons.chain_saw_operator import ChainsawOperator
from ml.fml40.roles.dts.persons.forest_owner import ForestOwner
from ml.fml40.roles.dts.persons.forest_worker import ForestWorker
from ml.fml40.roles.dts.persons.mini_tractor_operator import MiniTractorOperator
from ml.fml40.roles.dts.persons.skidder_operator import SkidderOperator
from ml.fml40.roles.dts.sensors.vitality_sensor import VitalitySensor
from ml.fml40.roles.dts.sensors.barkbeetle_sensor import BarkbeetleSensor
from ml.fml40.roles.dts.sites.forest_enterprise import ForestEnterprise
from ml.fml40.roles.dts.sites.hauler import Hauler
from ml.fml40.roles.dts.sites.mill.mill import Mill
from ml.fml40.roles.dts.sites.mill.papermill import Papermill
from ml.fml40.roles.dts.sites.mill.sawmill import Sawmill
from ml.fml40.roles.dts.sites.wood_yard import WoodYard
from ml.fml40.roles.dts.ways.forest_road import ForestRoad
from ml.fml40.roles.dts.woods.log_loading_unit import LogLoadingUnit
from ml.fml40.roles.dts.woods.loose_stack import LooseStack
from ml.fml40.roles.dts.woods.wood import Wood
from ml.fml40.roles.dts.woods.stem_segment import StemSegment
from ml.fml40.roles.dts.woods.wood_pile import WoodPile
from ml.fml40.roles.dts.forest.forest import Forest
from ml.fml40.roles.dts.forest.forest_segment import ForestSegment
from ml.fml40.roles.dts.forest.tree import Tree

from ml.mml40.roles.dts.parts.cantilever import Cantilever
from ml.mml40.roles.dts.sensors.strain_gauge import StrainGauge

from ml.wml40.roles.dts.sensors.waterlevelflowsensor import WaterLevelFlowSensor
from ml.wml40.roles.dts.sites.damwall import DamWall
from ml.wml40.roles.dts.sites.waterqualitymeasuringpoint import WaterQualityMeasuringPoint
from ml.wml40.roles.dts.sites.waterretainingstructure import WaterRetainingStructure
from ml.wml40.roles.dts.water.inflow import Inflow
from ml.wml40.roles.dts.water.outflow import Outflow
from ml.wml40.roles.dts.water.water import Water
from ml.wml40.roles.dts.water.waterreservoir import WaterReservoir

from ml.ml40.features.properties.associations.association import Association
from ml.ml40.features.properties.associations.composite import Composite
from ml.ml40.features.properties.property import Property
from ml.ml40.features.properties.associations.shared import Shared
from ml.ml40.features.properties.values.acceleration import Acceleration
from ml.ml40.features.properties.values.address import Address
from ml.ml40.features.properties.values.air_volume import AirVolume
from ml.ml40.features.properties.values.bank_account import BankAccount
from ml.ml40.features.properties.values.brand import Brand
from ml.ml40.features.properties.values.capacity import Capacity
from ml.ml40.features.properties.values.contacts import Contacts
from ml.ml40.features.properties.values.contract_number import ContractNumber
from ml.ml40.features.properties.values.cost import Cost
from ml.ml40.features.properties.values.count import Count
from ml.ml40.features.properties.values.current_load import CurrentLoad
from ml.ml40.features.properties.values.current_weight import CurrentWeight
from ml.ml40.features.properties.values.delivery_address import DeliveryAddress
from ml.ml40.features.properties.values.description import Description
from ml.ml40.features.properties.values.diameter import Diameter
from ml.ml40.features.properties.values.dimensions import Dimensions
from ml.ml40.features.properties.values.distance import Distance
from ml.ml40.features.properties.values.empty_load import EmptyLoad
from ml.ml40.features.properties.values.empty_weight import EmptyWeight
from ml.ml40.features.properties.values.expansion_length import ExpansionLength
from ml.ml40.features.properties.values.financial_value import FinancialValue
from ml.ml40.features.properties.values.force import Force
from ml.ml40.features.properties.values.fuel import Fuel
from ml.ml40.features.properties.values.fuel_comsumption import FuelConsumption
from ml.ml40.features.properties.values.fuel_type import FuelType
from ml.ml40.features.properties.values.generic_property import GenericProperty
from ml.ml40.features.properties.values.idling_operating_hours import IdlingOperatingHours
from ml.ml40.features.properties.values.imu_quaternion import IMUQuaternion
from ml.ml40.features.properties.values.land_velocity import LandVelocity
from ml.ml40.features.properties.values.last_service_check import LastServiceCheck
from ml.ml40.features.properties.values.lift import Lift
from ml.ml40.features.properties.values.linestring import LineString
from ml.ml40.features.properties.values.linestring_wkt import LineStringWKT
from ml.ml40.features.properties.values.liquid_filling_level import LiquidFillingLevel
from ml.ml40.features.properties.values.load import Load
from ml.ml40.features.properties.values.load_index import LoadIndex
from ml.ml40.features.properties.values.loading_volume import LoadingVolume
from ml.ml40.features.properties.values.lot import Lot
from ml.ml40.features.properties.values.location import Location
from ml.ml40.features.properties.values.machine_operating_status import MachineOperatingStatus
from ml.ml40.features.properties.values.machine_operating_status_type import MachineOperatingStatusType
from ml.ml40.features.properties.values.maintenance_due import MaintenanceDue
from ml.ml40.features.properties.values.maintenance_remaining_hours import MaintenanceRemainingHours
from ml.ml40.features.properties.values.manufacturing_year import ManufacturingYear
from ml.ml40.features.properties.values.mean_moisture import MeanMoisture
from ml.ml40.features.properties.values.measure import Measure
from ml.ml40.features.properties.values.model import Model
from ml.ml40.features.properties.values.moisture import Moisture
from ml.ml40.features.properties.values.motor_vehicle_license_plate_number import MotorVehicleLicensePlateNumber
from ml.ml40.features.properties.values.number import Number
from ml.ml40.features.properties.values.opening_hours import OpeningHours
from ml.ml40.features.properties.values.operating_hours import OperatingHours
from ml.ml40.features.properties.values.orientation_rpy import OrientationRPY
from ml.ml40.features.properties.values.percentage import Percentage
from ml.ml40.features.properties.values.personal_name import PersonalName
from ml.ml40.features.properties.values.pressure import Pressure
from ml.ml40.features.properties.values.price_list import PriceList
from ml.ml40.features.properties.values.purchase_cost import PurchaseCost
from ml.ml40.features.properties.values.reference_number import ReferenceNumber
from ml.ml40.features.properties.values.road_velocity import RoadVelocity
from ml.ml40.features.properties.values.rotational_speed import RotationalSpeed
from ml.ml40.features.properties.values.route import Route
from ml.ml40.features.properties.values.serial_number import SerialNumber
from ml.ml40.features.properties.values.srid import SRID
from ml.ml40.features.properties.values.status import Status
from ml.ml40.features.properties.values.steering_angle import SteeringAngle
from ml.ml40.features.properties.values.surface import Surface
from ml.ml40.features.properties.values.surface_wkt import SurfaceWKT
from ml.ml40.features.properties.values.switching_stage import SwitchingStage
from ml.ml40.features.properties.values.tax_number import TaxNumber
from ml.ml40.features.properties.values.temperature import Temperature
from ml.ml40.features.properties.values.time import Time
from ml.ml40.features.properties.values.time_slot import TimeSlot
from ml.ml40.features.properties.values.tilt import Tilt
from ml.ml40.features.properties.values.torque import Torque
from ml.ml40.features.properties.values.type import Type
from ml.ml40.features.properties.values.unit import Unit
from ml.ml40.features.properties.values.velocity import Velocity
from ml.ml40.features.properties.values.volume import Volume
from ml.ml40.features.properties.values.weatherdata import WeatherData
from ml.ml40.features.properties.values.weight import Weight
from ml.ml40.features.properties.values.documents.contacts.contact import Contact
from ml.ml40.features.properties.values.documents.contacts.organizational_contact import OrganizationalContact
from ml.ml40.features.properties.values.documents.contacts.personal_contact import PersonalContact
from ml.ml40.features.properties.values.documents.contracts.contract import Contract
from ml.ml40.features.properties.values.documents.jobs.generic_job import GenericJob
from ml.ml40.features.properties.values.documents.jobs.job import Job
from ml.ml40.features.properties.values.documents.jobs.job_list import JobList
from ml.ml40.features.properties.values.documents.jobs.job_status import JobStatus
from ml.ml40.features.properties.values.documents.notes.note import Note
from ml.ml40.features.properties.values.documents.reports.report import Report
from ml.ml40.features.properties.values.documents.reports.production_data import ProductionData


from ml.fml40.features.properties.values.abstract_inventory import AbstractInventory
from ml.fml40.features.properties.values.allow_wood_delivery_time_slot import AllowWoodDeliveryTimeSlot
from ml.fml40.features.properties.values.assortment import Assortment
from ml.fml40.features.properties.values.basal_area import BasalArea
from ml.fml40.features.properties.values.climbing_ability import ClimbingAbility
from ml.fml40.features.properties.values.cost_index_low_loader import CostIndexLowLoader
from ml.fml40.features.properties.values.customer_type import CustomerType
from ml.fml40.features.properties.values.dbh import DBH
from ml.fml40.features.properties.values.fell_indicator import FellIndicator
from ml.fml40.features.properties.values.felling_period import FellingPeriod
from ml.fml40.features.properties.values.ground_clearance import GroundClearance
from ml.fml40.features.properties.values.harvesting_parameter import HarvestingParameters
from ml.fml40.features.properties.values.harvested_volume import HarvestedVolume
from ml.fml40.features.properties.values.interfering_branches import InterferingBranches
from ml.fml40.features.properties.values.inventory_data import InventoryData
from ml.fml40.features.properties.values.is_felled import IsFelled
from ml.fml40.features.properties.values.log_forecast_volume import LogForecastVolume
from ml.fml40.features.properties.values.log_loading_length import LogLoadingLength
from ml.fml40.features.properties.values.maintenance_data import MaintenanceData
from ml.fml40.features.properties.values.mean_height import MeanHeight
from ml.fml40.features.properties.values.overhang import Overhang
from ml.fml40.features.properties.values.piling_period import PilingPeriod
from ml.fml40.features.properties.values.piling_status import PilingStatus
from ml.fml40.features.properties.values.product_length import ProductLength
from ml.fml40.features.properties.values.round_wood_product import RoundWoodProduct
from ml.fml40.features.properties.values.sawing_processing_step import SawingProcessingStep
from ml.fml40.features.properties.values.sawing_processing_time import SawingProcessingTime
from ml.fml40.features.properties.values.sawing_setup_time import SawingSetupTime
from ml.fml40.features.properties.values.mill_delivery_parking_area_status import MillDeliveryParkingAreaStatus
from ml.fml40.features.properties.values.mill_entry_parking_area_status import MillEntryParkingAreaStatus
from ml.fml40.features.properties.values.stem_segment_list import StemSegmentList
from ml.fml40.features.properties.values.stem_segment_properties import StemSegmentProperties
from ml.fml40.features.properties.values.stock_volume import StockVolume
from ml.fml40.features.properties.values.timber_assortment import TimberAssortment
from ml.fml40.features.properties.values.timber_harvesting_capacity import TimberHarvestingCapacity
from ml.fml40.features.properties.values.timber_harvesting_cost import TimberHarvestingCost
from ml.fml40.features.properties.values.timber_harvesting_procedure import TimberHarvestingProcedure
from ml.fml40.features.properties.values.timber_purchaser import TimberPurchaser
from ml.fml40.features.properties.values.timber_volume import TimberVolume
from ml.fml40.features.properties.values.time_period import TimePeriod
from ml.fml40.features.properties.values.thickness_class import ThicknessClass
from ml.fml40.features.properties.values.tree_data import TreeData
from ml.fml40.features.properties.values.species_group import SpeciesGroup
from ml.fml40.features.properties.values.tree_type import TreeType
from ml.fml40.features.properties.values.vegetationindex import VegetationIndex
from ml.fml40.features.properties.values.vitality_status import VitalityStatus
from ml.fml40.features.properties.values.wood_pile_list import WoodPileList
from ml.fml40.features.properties.values.wood_pile_measurement_properties import WoodPileMeasurementProperties
from ml.fml40.features.properties.values.wood_quality import WoodQuality
from ml.fml40.features.properties.values.wood_volume_solid_under_bark import WoodVolumeSolidUnderBark
from ml.fml40.features.properties.values.documents.contracts.log_procurement_contract import LogProcurementContract
from ml.fml40.features.properties.values.documents.jobs.felling_job import FellingJob
from ml.fml40.features.properties.values.documents.jobs.fellung_support_job import FellingSupportJob
from ml.fml40.features.properties.values.documents.jobs.forwarding_job import ForwardingJob
from ml.fml40.features.properties.values.documents.jobs.log_transportation_job import LogTransportationJob
from ml.fml40.features.properties.values.documents.notes.log_delivery_note import LogDeliveryNote
from ml.fml40.features.properties.values.documents.reports.afforestation_suggestion import AfforestationSuggestion
from ml.fml40.features.properties.values.documents.reports.felling_tool import FellingTool
from ml.fml40.features.properties.values.documents.reports.log_measurement import LogMeasurement
from ml.fml40.features.properties.values.documents.reports.log_transportation_report import LogTransportationReport
from ml.fml40.features.properties.values.documents.reports.map_data import MapData
from ml.fml40.features.properties.values.documents.reports.moisture_prediction_report import MoisturePredictionReport
from ml.fml40.features.properties.values.documents.reports.passability_report import PassabilityReport
from ml.fml40.features.properties.values.documents.reports.soil_moisture_measurement import SoilMoistureMeasurement
from ml.fml40.features.properties.values.documents.reports.wood_certificate import WoodCertificate

from ml.mml40.features.properties.values.Displacement import Displacement
from ml.mml40.features.properties.values.GeometryProperties import GeometryProperties
from ml.mml40.features.properties.values.LoadAlarm import LoadAlarm
from ml.mml40.features.properties.values.MaterialProperties import MaterialProperties
from ml.mml40.features.properties.values.Stretch import Stretch

from ml.wml40.features.properties.values.waterflow import WaterFlow
from ml.wml40.features.properties.values.waterlevel import WaterLevel
from ml.wml40.features.properties.values.waterquality import WaterQuality


from ml.ml40.features.functionalities.accepts_jobs import AcceptsJobs
from ml.ml40.features.functionalities.accepts_reports import AcceptsReports
from ml.ml40.features.functionalities.clears_jobs import ClearsJobs
from ml.ml40.features.functionalities.controls_production import ControlsProduction
from ml.ml40.features.functionalities.functionality import Functionality
from ml.ml40.features.functionalities.manages_jobs import ManagesJobs
from ml.ml40.features.functionalities.plans_routes import PlansRoutes
from ml.ml40.features.functionalities.predicts_consumption import PredictsConsumption
from ml.ml40.features.functionalities.predicts_maintenance import PredictsMaintenance
from ml.ml40.features.functionalities.predicts_purchase import PredictsPurchase
from ml.ml40.features.functionalities.provides_emissions_data import ProvidesEmissionsData
from ml.ml40.features.functionalities.provides_machine_data import ProvidesMachineData
from ml.ml40.features.functionalities.provides_map_data import ProvidesMapData
from ml.ml40.features.functionalities.provides_operational_data import ProvidesOperationalData
from ml.ml40.features.functionalities.predicts_purchase import PredictsPurchase
from ml.ml40.features.functionalities.provides_settlement import ProvidesSettlement
from ml.ml40.features.functionalities.provides_weather_data import ProvidesWeatherData
from ml.ml40.features.functionalities.renders import Renders

from ml.fml40.features.functionalities.accepts_felling_jobs import AcceptsFellingJobs
from ml.fml40.features.functionalities.accepts_felling_support_jobs import AcceptsFellingSupportJobs
from ml.fml40.features.functionalities.accepts_forwarding_jobs import AcceptsForwardingJobs
from ml.fml40.features.functionalities.accepts_log_loading_unit import AcceptsLogLoadingUnit
from ml.fml40.features.functionalities.accepts_log_loading_unit_in_wood_yard import AcceptsLogLoadingUnitInWoodYard
from ml.fml40.features.functionalities.accepts_log_measurements import AcceptsLogMeasurements
from ml.fml40.features.functionalities.accepts_log_transportaition_jobs import AcceptsLogTransportationJobs
from ml.fml40.features.functionalities.accepts_log_truck_weight_measurement import AcceptsLogTruckWeightMeasurement
from ml.fml40.features.functionalities.accepts_moisture_measurement import AcceptsMoistureMeasurement
from ml.fml40.features.functionalities.accepts_move_commands import AcceptsMoveCommands
from ml.fml40.features.functionalities.accepts_passability_report import AcceptsPassabilityReport
from ml.fml40.features.functionalities.accepts_proximity_alert import AcceptsProximityAlert
from ml.fml40.features.functionalities.accepts_shield_commands import AcceptsShieldCommands
from ml.fml40.features.functionalities.accepts_single_tree_felling_jobs import AcceptsSingleTreeFellingJobs
from ml.fml40.features.functionalities.accepts_winch_command import AcceptsWinchCommands
from ml.fml40.features.functionalities.calculates_machine_operation_cost import CalculatesMachineOperationCost
from ml.fml40.features.functionalities.classifies_tree_species import ClassifiesTreeSpecies
from ml.fml40.features.functionalities.controls_forest_production import ControlsForestProduction
from ml.fml40.features.functionalities.controls_sawmill_production import ControlsSawmillProduction
from ml.fml40.features.functionalities.converts_shapefile import ConvertsShapefile
from ml.fml40.features.functionalities.creates_productionteam import CreatesProductionteam
from ml.fml40.features.functionalities.cuts import Cuts
from ml.fml40.features.functionalities.determines_passability import DeterminesPassability
from ml.fml40.features.functionalities.displays_health_alarms import DisplaysHealthAlarms
from ml.fml40.features.functionalities.evaluates_stand_attributes import EvaluatesStandAttributes
from ml.fml40.features.functionalities.fells import Fells
from ml.fml40.features.functionalities.forest_planning_evaluation import ForestPlanningEvaluation
from ml.fml40.features.functionalities.forwards import Forwards
from ml.fml40.features.functionalities.generates_afforestation_suggestions import GeneratesAfforestationSuggestions
from ml.fml40.features.functionalities.generates_felling_suggestions import GeneratesFellingSuggestions
from ml.fml40.features.functionalities.generates_log_delivery_note import GeneratesLogDeliveryNote
from ml.fml40.features.functionalities.generates_log_loading_note import GeneratesLogLoadingNote
from ml.fml40.features.functionalities.grabs import Grabs
from ml.fml40.features.functionalities.harvests import Harvests
from ml.fml40.features.functionalities.load_log_loading_unit import LoadLogLoadingUnit
from ml.fml40.features.functionalities.generates_log_loading_unit import GeneratesLogLoadingUnit
from ml.fml40.features.functionalities.measure_wood import MeasuresWood
from ml.fml40.features.functionalities.monitor_health_status import MonitorsHealthStatus
from ml.fml40.features.functionalities.removes_log_loading_unit import RemovesLogLoadingUnit
from ml.fml40.features.functionalities.plans_harvesting_job_list import PlansHarvestingJobList
from ml.fml40.features.functionalities.predicts_forest_development import PredictsForestDevelopment
from ml.fml40.features.functionalities.predicts_maintenance import PredictsMaintenance
from ml.fml40.features.functionalities.provides_emission_data import ProvidesEmissionData
from ml.fml40.features.functionalities.provides_moisture_prediction import ProvidesMoisturePrediction
from ml.fml40.features.functionalities.provides_passability_information import ProvidesPassabilityInformation
from ml.fml40.features.functionalities.provides_production_data import ProvidesProductionData
from ml.fml40.features.functionalities.provides_stem_segment_data import ProvidesStemSegmentData
from ml.fml40.features.functionalities.provides_soil_data import ProvidesSoilData
from ml.fml40.features.functionalities.unload_log_loading_unit import UnloadsLogLoadingUnit

from ml.fml40.features.functionalities.provides_tree_data import ProvidesTreeData
from ml.fml40.features.functionalities.provides_weather_data import ProvidesWeatherData
from ml.fml40.features.functionalities.simulates_tree_growth import SimulatesTreeGrowth
from ml.fml40.features.functionalities.supports_felling import SupportsFelling
from ml.fml40.features.functionalities.transports_logs import TransportsLogs

from ml.mml40.features.functionalities.CantileverConfigure import CantileverConfigure
from ml.mml40.features.functionalities.EstimatesLoading import EstimatesLoading
from ml.mml40.features.functionalities.ProvidesDisplacementData import ProvidesDisplacementData
from ml.mml40.features.functionalities.ProvidesForceData import ProvidesForceData
from ml.mml40.features.functionalities.ProvidesStretchData import ProvidesStretchData

from ml.wml40.features.functionalities.provides_water_data import ProvidesWaterData
from ml.wml40.features.functionalities.provides_water_quality_data import ProvidesWaterQualityData

DT_FACTORY = {}

clsmembers = inspect.getmembers(sys.modules[__name__], inspect.isclass)
for member in clsmembers:
    DT_FACTORY[member[0]] = member[1]


def build_sub_features(feature_ins, feature):
    """
    Instantiates and inserts ml40/fml40 sub features object into feature instance

    :param feature_ins: ml40/fml40 feature instance, which has a sub feature to be built
    :type feature_ins: ml.Feature
    :param feature: ml40/fml40 feature containing subFeatures
    :type feature: dict

    """
    sub_features = feature.get("subFeatures", [])
    for sub_f in sub_features:
        sub_f_name = sub_f.get("class")
        if sub_f_name is None:
            sub_f_name = sub_f.get("name")
        if sub_f_name is None:
            sub_f_name = sub_f.get("identifier")
        _class_name = sub_f.get("class", "")
        sub_f_obj = DT_FACTORY.get(remove_namespace(_class_name), None)
        if sub_f_obj is None:
            APP_LOGGER.critical("Subfeature: %s is missing" % _class_name)
        else:
            sub_f_instance = sub_f_obj()
            for key in sub_f.keys():
                if key == "targets":
                    build_sub_thing(sub_f_instance, sub_f)
                elif key == "subFeatures":
                    build_sub_features(sub_f_instance, sub_f)
                else:
                    setattr(sub_f_instance, key, sub_f[key])
            sub_f_instance.parent = feature_ins
            feature_ins.subFeatures[sub_f_name] = sub_f_instance


def build_sub_thing(feature_ins, feature):
    """
    Instantiates and inserts sub thing object into a feature instance

    :param feature_ins: ml40/fml40 feature instance
    :type feature_ins: ml.Feature
    :param feature: ml40/fml40 feature, which contains a sub thing
    :type feature: dict

    """
    json_sub_things = feature.get("targets", [])
    for json_sub_thing in json_sub_things:
        sub_thing_ref = build({"attributes": json_sub_thing})
        sub_thing_name = json_sub_thing.get("name", None)
        feature_ins.targets[sub_thing_name] = sub_thing_ref
        sub_thing_ref.parent = feature_ins


def build(model):
    """
    Builds an instance of ml.Entry

    :param model: A serialized modeling for DT, conform to ForestML 4.0
    :type model: dict

    """
    identifier = model.get("thingId", None)
    attributes = model.get("attributes", None)
    name = attributes.get("name", None)
    ditto_features = model.get("features", None)
    entry_ref = Entry(identifier, name)

    if not isinstance(model, dict):
        # TODO JSON Schema
        APP_LOGGER.critical("Model contains an invalid JSON")
        return

    if attributes.get("identifier"):
        entry_ref.identifier = attributes.get("identifier")

    roles = attributes.get("roles", [])
    for role in roles:
        role_instance = build_role(role)
        role_instance.parent = entry_ref
        entry_ref.roles[role.get("class")] = role_instance

    json_features = attributes.get("features", [])
    for feature in json_features:
        feature_ins = build_feature(feature=feature)
        feature_ins.parent = entry_ref
        entry_ref.features[feature.get("class")] = feature_ins

    if ditto_features is not None:
        __build_ditto_features(entry_ref, ditto_features)

    return entry_ref


def __build_ditto_features(thing, ditto_features):
    """
    Instantiates Eclipse Ditto conform feature class
    """
    for key in ditto_features.keys():
        for _key in ditto_features[key]["properties"]:
            ditto_f = DittoFeature(id=key, key=_key, value=ditto_features[key]["properties"][_key])
            thing.ditto_features[ditto_f.id] = ditto_f


def build_role(role):
    """
    Instantiates a ml40/fml40 role class

    :param role: ml40/fml40 role
    :type role: dict

    """
    role_class_name = role.get("class", "")
    role_obj = DT_FACTORY.get(remove_namespace(role_class_name), None)
    if role_obj is None:
        APP_LOGGER.critical("Roles: %s undefined in ForestML 4.0" % role_class_name)
        role_instance = None
    else:
        role_instance = role_obj()
    return role_instance


def build_feature(feature):
    """
    Instantiates a ml40/fml40 feature class

    :param feature: ml40/fml40 feature
    :type feature: dict

    """
    feature_class_name = feature.get("class", "")
    feature_obj = DT_FACTORY.get(remove_namespace(feature_class_name), None)

    if feature_obj is None:
        APP_LOGGER.critical("Feature: %s undefined in ForestML 4.0" % feature_class_name)
        feature_instance = None
    else:
        feature_instance = feature_obj()
        for key in feature.keys():
            if key == "class":
                continue
            if key == "targets":
                build_sub_thing(feature_instance, feature)
            elif key == "subFeatures":
                build_sub_features(feature_instance, feature)
            else:
                setattr(feature_instance, check_var_conflict(key), feature[key])
    return feature_instance


