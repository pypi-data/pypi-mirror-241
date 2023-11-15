from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import truck, forest_machine


class TruckTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        forest_machine_features =forest_machine["attributes"]["features"]
        json_model = truck
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
        super(TruckTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    t = TruckTemplate(oauth2_id="", oauth2_secret="")
    t.run_forever()

