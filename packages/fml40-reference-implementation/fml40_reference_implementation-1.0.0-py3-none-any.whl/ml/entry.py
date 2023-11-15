class Entry(object):
    """
    Class to define an entry object that refers to ForestML4.0 modeling and its conform data.
    Here, the model will be serialized into JSON stored as the attribute self.__dt_json
    This class should not be directly called. To build an entry, you need to use ml.build()

    :param identifier: identifier of the DT
    :type identifier: string
    :param name: name of the DT
    :type name: string
    """
    def __init__(self, identifier, name):
        self.__name = name
        self.__identifier = identifier
        self.__features = {}
        self.__roles = {}
        self.__ditto_features = {}
        self.__dt_json = {
            "thingId": "",
            "policyId": "",
            "attributes": {
            }
        }
        self.refresh_dt_json()

    @property
    def features(self):
        """
        Returns the dictionary for features.
        Keys are name of ml40/fml40 features and their value are instantiated objects

        :rtype: dict
        """
        return self.__features

    @features.setter
    def features(self, value):
        """
        Sets the dictionary for features

        :param value: feature instance
        :type value: ml.Feature
        """
        self.__features = value

    @property
    def ditto_features(self):
        """
        Returns the optional dictionary for Eclipse Ditto features.
        This will only be used, if the serialized modeling of DT should be pushed to S3I Repository and
        the feature key on the top level of Eclipse Ditto JSON modeling should be used

        :rtype: dict
        """
        return self.__ditto_features

    @ditto_features.setter
    def ditto_features(self, value):
        """
        Sets the dictionary for ditto feature

        """
        self.__ditto_features = value

    @property
    def roles(self):
        """
        Returns the roles of DT as a dictionary. Keys are the name of ml40/fml40 roles.
        Their values are instantiated objects

        :rtype: dict
        """
        return self.__roles

    @property
    def name(self):
        """
        Returns the name of DT

        :rtype: str
        """
        return self.__name

    @name.setter
    def name(self, value):
        """
        Sets the name of DT

        :param value: new name of DT
        :type value: string
        """
        self.__name = value

    @property
    def identifier(self):
        """
        Returns the identifier of DT
        """
        return self.__identifier

    @identifier.setter
    def identifier(self, value):
        self.__identifier = value

    @property
    def dt_json(self):
        """
        Returns the complete serialized JSON of the DT

        rtype: dict
        """
        return self.__dt_json

    def refresh_dt_json(self):
        """
        Refreshes and returns a thing's current state conform to ForestML 4.0 modeling
        The thing's state is serialized as JSON

        :returns: the complete serialized JSON of the DT modeling
        :rtype: dict
        """

        self.__dt_json = {
            "thingId": self.__identifier,
            "policyId": self.__identifier,
            "attributes": {
                "class": "ml40::Thing",
                "name": self.__name,
            },
        }
        if self.identifier:
            self.__dt_json["attributes"]["identifier"] = self.identifier
        if self.roles:
            self.__dt_json["attributes"]["roles"] = []
        if self.features:
            self.__dt_json["attributes"]["features"] = []
        if self.ditto_features:
            self.__dt_json["features"] = {}
        for key in self.__roles.keys():
            self.__dt_json["attributes"]["roles"].append(self.__roles[key].to_json())
        for key in self.__features.keys():
            self.__dt_json["attributes"]["features"].append(self.__features[key].to_json())
        for key in self.__ditto_features.keys():
            self.__dt_json["features"][key] = self.__ditto_features[key].to_json()
        return self.__dt_json


    def refresh_sub_thing_json(self):
        """
        Refreshes and returns a subordinate thing's current state which is serialized as JSON

        :returns: Representation of this object as a subordinate thing
        :rtype: dict
        """

        json_out = {
            "class": "ml40::Thing",
            "name": self.name,
            "roles": [],
            "features": [],
        }
        if self.__identifier:
            json_out["identifier"] = self.__identifier
        for key in self.__roles.keys():
            json_out["roles"].append(self.__roles[key].to_json())
        for key in self.__features.keys():
            json_out["features"].append(self.__features[key].to_json())
        return json_out

