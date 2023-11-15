from ml.ml40.features.properties.values.address import Address


class DeliveryAddress(Address):
    def __init__(self, namespace="ml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
