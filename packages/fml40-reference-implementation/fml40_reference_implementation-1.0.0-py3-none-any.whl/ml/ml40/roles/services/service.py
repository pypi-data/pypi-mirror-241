from ml.role import Role


class Service(Role):
    def __init__(self, namespace="ml40", name="", identifier="", parent=None):
        super(Service, self).__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
