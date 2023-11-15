from ml.ml40.features.properties.values.volume import Volume


class TimberVolume(Volume):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
