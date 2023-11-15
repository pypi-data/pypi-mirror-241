from ml.ml40.features.functionalities.functionality import Functionality

from ml.fml40.features.properties.values.timber_harvesting_procedure import TimberHarvestingProcedure
from ml.fml40.features.properties.values.timber_harvesting_capacity import TimberHarvestingCapacity
from ml.fml40.features.properties.values.timber_assortment import TimberAssortment
from ml.fml40.features.properties.values.harvesting_machine_equipement_types import HarvestingMachineEquipmentTypes
from ml.fml40.features.properties.values.time_period import TimePeriod


class CreatesProductionteam(Functionality):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )

    def createProductionteam(self, orderDetails: dict, periodOfTime: dict,
                             contractor: dict, resource: dict, productionTeamOwner: dict,
                             productionTeamLeader: dict) -> dict:
        pass
