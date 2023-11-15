from ml.ml40.features.functionalities.functionality import Functionality


class Event(Functionality):
    """Generic implementation of an Event."""
    topic: str
    description: str
    frequency: int

    def __init__(self, namespace="ml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.topic = None
        self.description = None
        self.frequency = None
