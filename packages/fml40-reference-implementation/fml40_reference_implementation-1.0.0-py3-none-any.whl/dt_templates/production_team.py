from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import production_team


class ProductionTeamTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        production_team["thingId"] = oauth2_id
        production_team["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(production_team)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(production_team["attributes"].get("name", None))
        super(ProductionTeamTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    pt = ProductionTeamTemplate(oauth2_id="", oauth2_secret="")
    pt.run_forever()