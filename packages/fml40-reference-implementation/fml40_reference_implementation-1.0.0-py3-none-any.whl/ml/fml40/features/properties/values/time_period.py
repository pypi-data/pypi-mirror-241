from ml.ml40.features.properties.values.value import Value


class TimePeriod(Value):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__start = None
        self.__end = None
        self.__json_out = dict()

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, newStart):
        self.__start = newStart

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, newEnd):
        self.__end = newEnd

    def to_json(self):
        self.__json_out = super().to_json()
        if self.__start is not None:
            self.__json_out["start"] = self.__start
        if self.__end is not None:
            self.__json_out["end"] = self.__end
        return self.__json_out

