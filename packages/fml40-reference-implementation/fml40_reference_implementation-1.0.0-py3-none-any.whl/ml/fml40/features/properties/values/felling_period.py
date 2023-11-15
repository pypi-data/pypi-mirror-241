from ml.ml40.features.properties.values.value import Value


class FellingPeriod(Value):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__method = None
        self.__date = None
        self.__json_out = dict()

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, value):
        self.__method = value

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, value):
        self.__date = value

    def to_json(self):
        self.__json_out = super().to_json()
        if self.__method is not None:
            self.__json_out["method"] = self.__method
        if self.__date is not None:
            self.__json_out["date"] = self.__date
        return self.__json_out
