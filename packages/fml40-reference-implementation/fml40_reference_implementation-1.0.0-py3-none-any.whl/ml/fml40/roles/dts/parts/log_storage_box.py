from ml.ml40.roles.dts.parts.part import Part


class LogStorageBox(Part):
    def __init__(self, namespace="ml40", name="", identifier="", parent=None):
        super(LogStorageBox, self).__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
