from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import wood_yard


class WoodYardTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        wood_yard["thingId"] = oauth2_id
        wood_yard["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(wood_yard)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(wood_yard["attributes"].get("name", None))
        super(WoodYardTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    wy = WoodYardTemplate(oauth2_id="", oauth2_secret="")
    wy.run_forever()




