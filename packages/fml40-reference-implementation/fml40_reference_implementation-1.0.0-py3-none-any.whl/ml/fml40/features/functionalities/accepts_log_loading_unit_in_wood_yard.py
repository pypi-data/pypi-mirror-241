from ml.fml40.features.functionalities.accepts_log_loading_unit import AcceptsLogLoadingUnit


class AcceptsLogLoadingUnitInWoodYard(AcceptsLogLoadingUnit):
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

    def accept(self, receiptNumber, logLoadingUnit) -> dict:
        """Accepts the given log_loading_unit. Returns true if the unit has
        been accepted, otherwise returns false.

        :param receiptNumber: receipt number
        :param logLoadingUnit: log_loading_unit to be accepted
        :rtype: dict

        """
        pass
