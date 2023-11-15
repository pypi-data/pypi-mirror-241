from ml.ml40.features.properties.values.number import Number


class ReferenceNumber(Number):
    def __init__(self, namespace="ml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
