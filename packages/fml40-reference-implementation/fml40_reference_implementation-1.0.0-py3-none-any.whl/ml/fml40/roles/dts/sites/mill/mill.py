from ml.ml40.roles.dts.sites.site import Site


class Mill(Site):
    def __init__(self, namespace="fml40", name="", identifier=""):
        super().__init__(namespace=namespace, name=name, identifier=identifier)
