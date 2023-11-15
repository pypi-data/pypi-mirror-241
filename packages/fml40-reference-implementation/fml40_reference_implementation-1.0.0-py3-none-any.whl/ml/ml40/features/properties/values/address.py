from ml.ml40.features.properties.values.value import Value


class Address(Value):
    def __init__(self, namespace="ml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )

        self.city = None
        self.country = None
        self.street = None
        self.street_number = None
        self.zip = None
        self.__json_out = dict()

    def to_json(self):
        self.__json_out = super().to_json()
        if self.city is not None:
            self.__json_out["city"] = self.city
        if self.country is not None:
            self.__json_out["country"] = self.country
        if self.street is not None:
            self.__json_out["street"] = self.street
        if self.street_number is not None:
            self.__json_out["streetNumber"] = self.street_number
        if self.zip is not None:
            self.__json_out["zip"] = self.zip

        return self.__json_out
