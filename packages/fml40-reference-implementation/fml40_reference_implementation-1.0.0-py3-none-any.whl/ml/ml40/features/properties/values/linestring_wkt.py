from ml.ml40.features.properties.values.linestring import LineString


class LineStringWKT(LineString):
    def __init__(self, namespace="ml40", name="", identifier="", parent=None):
        super().__init__(
            namespace=namespace, name=name, identifier=identifier, parent=parent
        )
        self.__wkt = None
        self.__json_out = dict()

    
    @property
    def wkt(self):
        return self.__wkt

    @wkt.setter
    def wkt(self, value):
        self.__wkt = value 
    
    def to_json(self):
        self.__json_out = super().to_json()
        if self.__wkt is not None:
            self.__json_out["wkt"] = self.__wkt
        return self.__json_out
        
