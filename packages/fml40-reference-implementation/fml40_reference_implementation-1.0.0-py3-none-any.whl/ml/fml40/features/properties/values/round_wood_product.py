from ml.ml40.features.properties.values.value import Value


class RoundWoodProduct(Value):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__product_name = None
        self.__json_out = dict()

    @property
    def productName(self):
        return self.__product_name

    @productName.setter
    def productName(self, value):
        self.__product_name = value

    def to_json(self):
        self.__json_out = super().to_json()
        if self.__product_name is not None:
            self.__json_out["productName"] = self.__product_name
        return self.__json_out
