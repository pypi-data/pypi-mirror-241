from ml.ml40.features.properties.values.value import Value


class WoodVolumeSolidUnderBark(Value):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__value = 0

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def to_json(self):
        self.__json_out = super().to_json()
        if self.__value is not None:
            self.__json_out["value"] = self.__value
        return self.__json_out
