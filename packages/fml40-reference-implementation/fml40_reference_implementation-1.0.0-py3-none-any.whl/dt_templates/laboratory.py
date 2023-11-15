from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import laboratory


class LaboratoryTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        laboratory["thingId"] = oauth2_id
        laboratory["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(laboratory)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(laboratory["attributes"].get("name", None))
        super(LaboratoryTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    labor = LaboratoryTemplate(oauth2_id="", oauth2_secret="")
    labor.run_forever()


