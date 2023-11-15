"""This module implements the class AcceptsLogLoadingUnit."""

from ml.ml40.features.functionalities.functionality import Functionality
from typing_extensions import TypedDict

class Result(TypedDict):
    ok: bool
    identifier: str
    receiptNumber: str

class AcceptsLogLoadingUnit(Functionality):
    """This functionality signalizes that a log loading unit can be
    accepted."""

    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        """Initializes the object.

        :param name:  Object name
        :param identifier: Identifier

        """
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )

    def accept(self, logLoadingUnit:dict) -> Result:
        """Accepts the given log_loading_unit. Returns true if the unit has
        been accepted, otherwise returns false.


        """
        pass
