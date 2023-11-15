from ml.ml40.features.properties.values.value import Value


class StemSegmentList(Value):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__targets = dict()

    @property
    def targets(self):
        return self.__targets

    @targets.setter
    def targets(self, value):
        self.__targets = value

    def to_json(self):
        self.__json_out = super().to_json()
        if self.targets:
            self.__json_out["targets"] = []
            for key in self.targets.keys():
                self.__json_out["targets"].append(self.targets[key].refresh_sub_thing_json())
        return self.__json_out