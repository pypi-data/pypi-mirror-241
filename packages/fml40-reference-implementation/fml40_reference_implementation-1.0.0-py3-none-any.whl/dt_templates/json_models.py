chainsaw = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "name": "",
        "roles": [
            {
                "class": "fml40::Chainsaw"
            }
        ],
        "features": [
            {
                "class": "ml40::Fuel",
                "type": ""
            },
            {
                "class": "ml40::Description",
                "value": "Stihl Motorsäge"
            },
            {
                "class": "ml40::Brand",
                "name": ""
            },
            {
                "class": "ml40::SerialNumber",
                "value": ""
            },
            {
                "class": "ml40::MaintenanceRemainingHours",
                "hours": 0
            },
            {
                "class": "ml40::Model",
                "value": ""
            },
            {
                "class": "ml40::ManufacturingYear",
                "year": 0
            },
            {
                "class": "ml40::MachineOperatingStatus",
                "status": "InOperation"
            },
            {
                "class": "ml40::PurchaseCost",
                "cost": 0
            },
            {
                "class": "ml40::OperatingHours",
                "current": 0,
                "total": 0
            },
            {
                "class": "ml40::FuelConsumption",
                "currentConsumption": 0,
                "meanConsumption": 0
            },
            {
                "class": "ml40::Location",
                "longitude": 0,
                "latitude": 0
            },
            {
                "class": "ml40::IMUQuaternion",
                "x": 0,
                "y": 0,
                "z": 0,
                "w": 0
            },
            {
                "class": "ml40::Acceleration",
                "x": 0,
                "y": 0,
                "z": 0
            },
            {
                "class": "fml40::SawingSetupTime",
                "time": 0
            },
            {
                "class": "fml40::SawingProcessingTime",
                "remainingTime": 0
            },
            {
                "class": "fml40::SawingProcessingStep",
                "currentStep": ""
            },
            {
                "class": "ml40::IdlingOperatingHours",
                "total": 0
            },
            {
                "class": "ml40::Time",
                "time": 0
            },
            {
                "class": "ml40::ProvidesEmissionsData"
            },
            {
                "class": "ml40::PredictsMaintenance"
            },
            {
                "class": "fml40::AcceptsFellingJobs"
            },
            {
                "class": "fml40::Cuts"
            },
            {
                "class": "ml40::ProvidesMachineData"
            },
            {
                "class": "fml40::ProvidesStemSegmentData"
            },
            {
                "class": "ml40::JobList",
                "subFeatures": [
                    {
                        "class": "fml40::FellingJob",
                        "identifier": "Felling:4711",
                        "status": "Completed"
                    }
                ]
            },
            {
                "class": "ml40::Composite",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "name": "",
                        "roles": [
                            {
                                "class": "ml40::AirSensor"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::AirVolume",
                                "volume": 0
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "name": "",
                        "roles": [
                            {
                                "class": "ml40::Engine"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::RotationalSpeed",
                                "rpm": 0
                            },
                            {
                                "class": "ml40::Temperature",
                                "temperature": 0
                            }
                        ]
                    }
                ]
            },
            {
                "class": "ml40::Shared",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "name": "",
                        "roles": [
                            {
                                "class": "fml40::Tree"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "name": "",
                        "roles": [
                            {
                                "class": "fml40::ForestWorker"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "name": "",
                        "roles": [
                            {
                                "class": "fml40::StemSegment"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "name": "",
                        "roles": [
                            {
                                "class": "fml40::ChainsawOperator"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "name": "",
                        "roles": [
                            {
                                "class": "ml40::TemperatureSensor"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Temperature",
                                "temperature": 50
                            }
                        ]
                    },
                    {
                        "class": "ml40:.Thimg",
                        "name": "",
                        "roles": [
                            {
                                "class": "ml40::PressureSensor"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Pressure",
                                "pressure": 0
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

forest_machine = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "identifier": "",
        "name": "",
        "features": [
            {
                "class": "fml40::SuitableTreeSpecies",
                "treeSpecies": []
            },
            {
                "class": "ml40::ManufacturingYear",
                "year": 0
            },
            {
                "class": "ml40::Brand",
                "name": ""
            },
            {
                "class": "fml40::CostIndexLowLoader",
                "cost": 0
            },
            {
                "class": "ml40::MaintenanceDue",
                "value": 0
            },
            {
                "class": "ml40::Description",
                "value": ""
            },
            {
                "class": "ml40::SerialNumber",
                "value": ""
            },
            {
                "class": "ml40::OperatingHours",
                "total": 0
            },
            {
                "class": "ml40::PurchaseCost",
                "cost": 0
            },
            {
                "class": "ml40::Measure",
                "data": "",
                "type": "",
                "description": ""
            },
            {
                "class": "ml40::MachineOperatingStatus",
                "status": ""
            },
            {
                "class": "ml40::Location",
                "longitude": 0,
                "latitude": 0,
                "orientation": 0
            },
            {
                "class": "ml40::CurrentWeight",
                "weight": 0
            },
            {
                "class": "ml40::EmptyWeight",
                "weight": 0
            },
            {
                "class": "ml40::SteeringAngle",
                "angle": 0
            },
            {
                "class": "ml40::Fuel",
                "type": ""
            },
            {
                "class": "ml40::RoadVelocity",
                "currentVelocity": 0,
                "maxVelocity": 0
            },
            {
                "class": "ml40::LandVelocity",
                "currentVelocity": 0,
                "maxVelocity": 0
            },
            {
                "class": "ml40::FuelConsumption",
                "currentConsumption": 0,
                "meanConsumption": 0
            },
            {
                "class": "ml40::PriceList",
                "price": []
            },
            {
                "class": "fml40::ProvidesEmissionsData"
            },
            {
                "class": "ml40::PredictsMaintenance"
            },
            {
                "class": "fml40::CalculatesMachineOperationCost"
            },
            {
                "class": "ml40::PredictsPurchase"
            },
            {
                "class": "ml40::ProvidesSettlement"
            },
            {
                "class": "fml40::PlansHarvestingJobList"
            },
            {
                "class": "ml40::Composite",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::Wheel"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Count",
                                "currentCount": 0
                            },
                            {
                                "class": "ml40::Model",
                                "name": ""
                            },
                            {
                                "class": "ml40::EmptyLoad",
                                "load": 0
                            },
                            {
                                "class": "ml40::CurrentLoad",
                                "load": 0
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::Band"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Model",
                                "name": ""
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::FrontBogieLift"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::RearBogieLift"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::Engine"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Temperature",
                                "temperature": 0
                            },
                            {
                                "class": "ml40::Torque",
                                "maxTorque": 0,
                                "currentTorque": 0
                            },
                            {
                                "class": "ml40::AirVolume",
                                "volume": 0
                            },
                            {
                                "class": "ml40::RotationalSpeed",
                                "rpm": 0
                            },
                            {
                                "class": "ml40::SwitchingStage",
                                "currentStage": 0
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::Chain"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Model",
                                "name": ""
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::Crane"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Location",
                                "longitude": 0,
                                "latitude": 0
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::SkiddingWinch"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::TractionWinch"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::StackingShield"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Dimensions",
                                "width": 0,
                                "height": 0
                            }
                        ]
                    }
                ]
            },
            {
                "class": "ml40::Shared",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::StemSegment"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::Way"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::LoadIndex",
                                "index": 0
                            },
                            {
                                "class": "GroundClearance",
                                "groundType": "",
                                "height": 0
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::MachineOperator"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::TemperatureSensor"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Temperature",
                                "temperature": 0
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "features": {}
}

forest_owner = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "roles": [
            {
                "class": "fml40::ForestOwner"
            }
        ],
        "name": "",
        "identifier": "",
        "features": [
            {
                "class": "ml40::BankAccount",
                "iban": "",
                "bic": "",
                "accountOwner": ""
            },
            {
                "class": "ml40::PersonalContact",
                "firstName": "",
                "lastName": "",
                "address": "",
                "telefon": "",
                "mobil": "",
                "fax": "",
                "eMail": "",
                "company": ""
            },
            {
                "class": "ml40::OrganizationalContact",
                "name": "",
                "address": "",
                "telefon": "",
                "mobil": "",
                "tax": "",
                "eMail": ""
            },
            {
                "class": "fml40::WoodCertificate",
                "woodOrigin": "",
                "type": "",
                "certificatedPercentage": 0,
                "identifier": ""
            }
        ]
    }
}

forwarder = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "name": "Forwarder Template",
        "roles": [
            {
                "class": "fml40::Forwarder"
            }
        ],
        "features": [
            {
                "class": "ml40::Tilt",
                "direction": "",
                "value": ""
            },
            {
                "class": "ml40::Composite",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::RungBasket"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::ClamBunk"
                            }
                        ]
                    }
                ]
            },
            {
                "class": "ml40::Shared",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::MachineOperator"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::StemSegment"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::LooseStack"
                            }
                        ]
                    }
                ]
            },
            {
                "class": "fml40::AcceptsForwardingJobs"
            },
            {
                "class": "ml40::JobList",
                "subFeatures": []
            }
        ]
    }
}

forwarding_agency = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "name": "",
        "identifier": "",
        "roles": [
            {
                "class": "ml40::ForwardingAgency"
            }
        ],
        "features": [
            {
                "class": "ml40::OrganizationalContact",
                "name": "",
                "address": "",
                "telefon": "",
                "mobil": "",
                "fax": "",
                "eMail": ""
            },
            {
                "class": "ml40::Type",
                "value": ""
            },
            {
                "class": "ml40::BankAccount",
                "BIC": "",
                "IBAN": "",
                "AccountOwner": ""
            },
            {
                "class": "fml40::AcceptsLogTransportationJobs"
            }
        ]
    }
}

harvester = {
    "thingId": "",
    "policyId": "",
    "attributes":
        {
            "class": "ml40::Thing",
            "identifier": "",
            "name": "",
            "features": [
                {
                    "class": "ml40::Composite",
                    "targets": [
                        {
                            "class": "ml40::Thing",
                            "roles": [
                                {
                                    "class": "fml40::HarvestingHead"
                                }
                            ],
                            "features": [
                                {
                                    "class": "ml40::ProductionData",
                                    "subFeatures": [
                                        {
                                            "class": "ml40::Composite",
                                            "targets": [
                                                {
                                                    "class": "ml40::Thing",
                                                    "roles": [
                                                        {
                                                            "class": "fml40::StemSegment"
                                                        }
                                                    ]
                                                    ,
                                                    "features": [
                                                        {
                                                            "class": "fml40::StemSegmentProperties"
                                                        }
                                                        ,
                                                        {
                                                            "class": "ml40::Location"
                                                        }
                                                    ]

                                                }
                                            ]

                                        }
                                    ]

                                }
                            ]

                        }
                        ,
                        {
                            "class": "ml40::Thing",
                            "roles": [
                                {
                                    "class": "ml40::Engine"
                                }
                            ]

                        }
                        ,
                        {
                            "class": "ml40::Thing",
                            "roles": [
                                {
                                    "class": "ml40::Crane"
                                }
                            ]

                        }
                        ,
                        {
                            "class": "ml40::Thing",
                            "name": "Tank",
                            "roles": [
                                {
                                    "class": "ml40::Tank"
                                }
                            ]
                            ,
                            "features": [
                                {
                                    "class": "ml40::LiquidFillingLevel",
                                    "currentLevel": 0,
                                    "maxLevel": 0
                                }
                            ]

                        }
                    ]

                }
                ,
                {
                    "class": "ml40::Location",
                    "longitude": 0,
                    "latitude": 0
                }
                ,
                {
                    "class": "ml40::OperatingHours",
                    "total": 0
                }
                ,
                {
                    "class": "fml40::ProvidesProductionData"
                }
                ,
                {
                    "class": "fml40::MaintenanceData",
                    "lastMaintainOperatingHours": 0,
                    "intervalTime": 0
                }
                ,
                {
                    "class": "fml40::AcceptsFellingJobs"
                },
                {
                    "class": "ml40::JobList",
                    "subFeatures": [
                        {
                            "class": "fml40::FellingJob",
                            "identifier": "smart_forestry_felling_job_1",
                            "subFeatures": [
                                {
                                    "class": "fml40::Assortment",
                                    "identifier": "4711",
                                    "name": "Industrieholz kurz",
                                    "subFeatures": [
                                        {
                                            "class": "fml40::TreeType",
                                            "name": "Spruce",
                                            "conifer": True
                                        },
                                        {
                                            "class": "fml40::ThicknessClass",
                                            "name": "1a-1b"
                                        },
                                        {
                                            "class": "fml40::HarvestingParameters",
                                            "cuttingLengths": 3
                                        }
                                    ],
                                    "grade": "ls"
                                },
                                {
                                    "class": "ml40::Location",
                                    "latitude": 0,
                                    "longitude": 0
                                }
                            ],
                            "status": "Completed"
                        }
                    ]
                }
            ]
            ,
            "roles": [
                {
                    "class": "fml40::Harvester"
                }
            ]

        }
}

laboratory = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "roles": [
            {
                "class": "ml40::Laboratory"
            }
        ],
        "features": [
            {
                "class": "fml40::AcceptsMoistureMeasurement"
            }
        ]
    }
}

log_truck_scale = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "roles": [
            {
                "class": "fml40::LogTruckScale"
            }
        ],
        "features": [
            {
                "class": "fml40::AcceptsLogTruckWeightMeasurement"
            }
        ]
    }
}

mill_gate = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "name": "",
        "class": "ml40::Thing",
        "identifier": "",
        "roles": [
            {
                "class": "fml40::MillGate"
            }
        ],
        "features": [
            {
                "class": "ml40::Composite",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::VehicleCounterSensor"
                            }
                        ]
                    }
                ]
            },
            {
                "class": "fml40::AllowWoodDeliveryTimeSlot",
                "start": 0,
                "end": 0
            },
            {
                "class": "ml40::OpeningHours",
                "start": 0,
                "end": 0
            },
            {
                "class": "fml40::MillEntryParkingAreaStatus",
                "status": ""
            },
            {
                "class": "fml40::MillDeliveryParkingAreaStatus",
                "status": ""
            },
            {
                "class": "fml40::AcceptsLogLoadingUnit"
            },
            {
                "class": "ml40::Shared",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::WoodYard"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::LogTruckScale"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::Laboratory"
                            }
                        ]
                    }
                ]
            },
            {
                "class": "fml40::PredictsConsumption"
            },
            {
                "class": "fml40::ControlsSawmillProduction"
            }
        ]
    }
}

production_team = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "name": "",
        "identifier": "",
        "roles": [
            {
                "class": "ml40::ProductionTeam"
            }
        ],
        "features": [
            {
                "class": "fml40::TimberHarvestingCapacity",
                "value": 0
            },
            {
                "class": "fml40::TimberHarvestingCost",
                "value": 0
            },
            {
                "class": "fml40::ControlsForestProduction"
            },
            {
                "class": "ml40::Composite",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "ml40::PrecinctLeader"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::LogTruck"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::Forwarder"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::Skidder"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::ForestWorker"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    "features": {}
}

truck = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "name": "",
        "roles": [
            {
                "class": "fml40::LogTruck"
            }
        ],
        "features": [
            {
                "class": "fml40::ClimbingAbility",
                "value": 0
            },
            {
                "class": "ml40::CurrentLoad",
                "load": 0
            },
            {
                "class": "ml40::MotorVehicleLicensePlateNumber",
                "value": ""
            },
            {
                "class": "ml40::JobList",
                "subFeatures": [
                    {
                        "class": "fml40::LogTransportationJob"
                    }
                ]
            },
            {
                "class": "fml40::GeneratesLogLoadingUnit"
            },
            {
                "class": "fml40::RemovesLogLoadingUnit"
            },
            {
                "class": "ml40::Shared",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::ForestRoad"
                            }
                        ]
                    }
                ]
            },
            {
                "class": "fml40::GeneratesLogLoadingNote"
            },
            {
                "class": "fml40::AcceptsLogTransportationJobs"
            }
        ]
    }
}

wood_yard = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "roles": [
            {
                "class": "fml40::WoodYard"
            }
        ],
        "features": [
            {
                "class": "fml40::AcceptsLogLoadingUnitInWoodYard"
            },
            {
                "class": "ml40::Shared",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::MillGate"
                            }
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::ForestOwner"
                            }
                        ]
                    }
                ]
            },
            {
                "class": "ml40::Composite",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "name": "baysf:4711",
                        "roles": [
                            {
                                "class": "fml40::LogStorageBox"
                            }
                        ],
                        "features": [
                            {
                                "class": "ml40::Location",
                                "longitude": 0,
                                "latitude": 0
                            },
                            {
                                "class": "ml40::LoadingVolume",
                                "currentVolume": 0,
                                "maxVolume": 0,
                                "minVolume": 0
                            },
                            {
                                "class": "fml40::LogForecastVolume",
                                "value": 0
                            },
                            {
                                "class": "fml40::SpeciesGroup",
                                "name": ""  # kie, fita, la,dgl, lbh
                            },
                            {
                                "class": "fml40::RoundWoodProduct",
                                "productName": ""
                            }
                        ]
                    }
                ]
            }
        ]
    }
}

stem_segment = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "roles": [
            {
                "class": "fml40::StemSegment"
            }
        ],
        "name": "",
        "identifier": "", # Here, we can enter XPath
        "features": [
            {
                "class": "ml40::Location",
                "longitude": 0,
                "latitude": 0
            },
            {
                "class": "fml40::WoodVolumeSolidUnderBark",
                "value": 0
            },
            {
                "class": "ml40::Diameter",
                "value": 0
            },
            {
                "class": "fml40::ProductLength",
                "value": 0
            },
            {
                "class": "fml40::RoundWoodProduct",
                "productName": ""
            },
            {
                "class": "fml40::SpeciesGroup",
                "name": "" # kie, fita, la,dgl, lbh
            },
        ]
    }
}

wood_pile = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "roles": [
            {
                "class": "fml40::WoodPile"
            }
        ],
        "name": "",
        "features": [
            {
                "class": "ml40::Location",
                "longitude": "",
                "latitude": ""
            },
            {
                "class": "fml40::WoodVolumeSolidUnderBark",
                "value": 0
            },
            {
                "class": "fml40::RoundWoodProduct",
                "productName": ""
            },
            {
                "class": "fml40::PilingPeriod",
                "from": "",
                "to": ""
            },
            {
                "class": "fml40::PilingStatus",
                "status": "" # InPiling, PilingCompleted, ReadyForTransport, InTransport, TransportCompleted
            },
            {
                "class": "fml40::WoodPileMeasurementProperties",
                "method": "",
                "date": ""
            },
            {
                "class": "fml40::TimberPurchaser",
                "subFeatures": [
                    {
                        "class": "ml40::ContractNumber",
                        "value": ""
                    },
                    {
                        "class": "DeliveryAddress",
                        "country": "",
                        "city": "",
                        "street": "",
                        "streetNumber": "",
                        "zip": ""
                    },
                    {
                        "class": "ml40::OrganizationalContact",
                        "name": "",
                        "address": "",
                        "telefon": "",
                        "mobil": "",
                        "fax": "",
                        "eMail": ""
                    }
                ]
            },
            {
                "class": "fml40::StemSegmentList",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::StemSegment"
                            }
                        ],
                        "name": "100_1",
                        "identifier": "", # Here, we can enter XPath
                        "features": [
                            {
                                "class": "ml40::Location",
                                "longitude": 0,
                                "latitude": 0
                            },
                            {
                                "class": "fml40::WoodVolumeSolidUnderBark",
                                "value": 0
                            },
                            {
                                "class": "ml40::Diameter",
                                "value": 0
                            },
                            {
                                "class": "fml40::ProductLength",
                                "value": 2
                            },
                            {
                                "class": "fml40::RoundWoodProduct",
                                "productName": ""
                            },
                            {
                                "class": "fml40::SpeciesGroup",
                                "name": "" # kie, fita, la,dgl, lbh
                            },
                        ]
                    },
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::StemSegment"
                            }
                        ],
                        "name": "100_2",
                        "identifier": "", # Here, we can enter XPath
                        "features": [
                            {
                                "class": "ml40::Location",
                                "longitude": 0,
                                "latitude": 0
                            },
                            {
                                "class": "fml40::WoodVolumeSolidUnderBark",
                                "value": 0
                            },
                            {
                                "class": "ml40::Diameter",
                                "value": 0
                            },
                            {
                                "class": "fml40::ProductLength",
                                "value": 2
                            },
                            {
                                "class": "fml40::RoundWoodProduct",
                                "productName": ""
                            },
                            {
                                "class": "fml40::SpeciesGroup",
                                "name": "" # kie, fita, la,dgl, lbh
                            },
                        ]
                    }
                ]
            }

        ]
    }
}

log_loading_unit = {
    "thingId": "",
    "policyId": "",
    "attributes": {
        "class": "ml40::Thing",
        "roles": [
            {
                "class": "fml40::LogLoadingUnit"
            }
        ],
        "features": [
            {
                "class": "fml40::WoodVolumeSolidUnderBark",
                "value": 0
            },
            {
                "class": "ml40::Weight",
                "value": 0
            },
            {
                "class": "ml40::Moisture",
                "value": 0
            },
            {
                "class": "ml40::ContractNumber",
                "value": ""
            },
            {
                "class": "ml40::ReferenceNumber",
                "value": ""
            },
            {
                "class": "fml40::WoodCertificate",
                "subFeatures": [
                    {
                        "class": "ml40::Type",
                        "type": ""
                    }
                ]
            },
            {
                "class": "fml40::WoodPileList",
                "targets": []
            },
            {
                "class": "ml40::Shared",
                "targets": [
                    {
                        "class": "ml40::Thing",
                        "roles": [
                            {
                                "class": "fml40::LogTruck"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}