from ml.ml40.features.properties.values.value import Value


class Number(Value):
    def __init__(self, namespace="ml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__value = None
        self.__json_out = dict()

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value

    def to_json(self):
        self.__json_out = super().to_json()
        if self.value is not None:
            self.__json_out["value"] = self.value
        return self.__json_out
