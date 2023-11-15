from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import forest_machine, harvester


class HarvesterTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        json_model = self.load_json_model()
        json_model["thingId"] = oauth2_id
        json_model["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(json_model)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(json_model["attributes"].get("name", None))
        super(HarvesterTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )

    @staticmethod
    def load_json_model():
        forest_machine_features = forest_machine["attributes"]["features"]
        json_model = harvester
        for item in forest_machine_features:
            if item.get("class") == "ml40::Composite":
                for i in range(len(json_model["attributes"]["features"])):
                    if json_model["attributes"]["features"][i].get("class") == "ml40::Composite":
                        json_model["attributes"]["features"][i]["targets"] += item["targets"]
                forest_machine_features.remove(item)
            if item.get("class") == "ml40::Shared":
                for i in range(len(json_model["attributes"]["features"])):
                    if json_model["attributes"]["features"][i].get("class") == "ml40::Shared":
                        json_model["attributes"]["features"][i]["targets"] += item["targets"]
                forest_machine_features.remvoe(item)

        json_model["attributes"]["features"] += forest_machine_features
        return json_model


if __name__ == "__main__":
    h = HarvesterTemplate(oauth2_id="", oauth2_secret="")
    h.run_forever()





