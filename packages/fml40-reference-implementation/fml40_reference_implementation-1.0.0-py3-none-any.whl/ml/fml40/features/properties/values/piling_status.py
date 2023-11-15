from ml.ml40.features.properties.values.value import Value


class PilingStatus(Value):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__status = None
        self.__json_out = dict()

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def to_json(self):
        self.__json_out = super().to_json()
        if self.__status is not None:
            self.__json_out["status"] = self.__status
        return self.__json_out
