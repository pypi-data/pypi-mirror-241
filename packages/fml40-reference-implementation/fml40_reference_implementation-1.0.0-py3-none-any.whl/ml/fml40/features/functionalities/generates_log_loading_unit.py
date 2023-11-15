from ml.ml40.features.functionalities.functionality import Functionality
from typing import List

class GeneratesLogLoadingUnit(Functionality):
    def __init__(self, namespace="fml40", name="", identifier="", parent=None):
        super().__init__(namespace=namespace, name=name, identifier=identifier, parent=parent)

    def generate(self, woodPileIdentifiers: List[str], contractNumber: str, referenceNumber: str) -> dict:
        pass