from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import forest_owner


class ForestOwnerTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        forest_owner["thingId"] = oauth2_id
        forest_owner["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(forest_owner)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(forest_owner["attributes"].get("name", None))
        super(ForestOwnerTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    fo = ForestOwnerTemplate(oauth2_id="", oauth2_secret="")
    fo.run_forever()





