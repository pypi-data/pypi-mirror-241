from ml.ml40.features.properties.values.value import Value


class HarvestingMachineEquipmentTypes(Value):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__machines = None
        self.__equipment = None
        self.__json_out = dict()

    @property
    def machines(self):
        return self.__machines

    @machines.setter
    def machines(self, newMachines):
        self.__machines = newMachines

    @property
    def equipment(self):
        return self.__equipment

    @equipment.setter
    def equipment(self, newEquipment):
        self.__equipment = newEquipment

    def to_json(self):
        self.__json_out = super().to_json()
        if self.__machines is not None:
            self.__json_out["machines"] = self.__machines
        if self.__equipment is not None:
            self.__json_out["equipment"] = self.__equipment
        return self.__json_out

