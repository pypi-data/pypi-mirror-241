from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import log_loading_unit


class LogLoadingUnitTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        log_loading_unit["thingId"] = oauth2_id
        log_loading_unit["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(log_loading_unit)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(log_loading_unit["attributes"].get("name", None))
        super(LogLoadingUnitTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    llu = LogLoadingUnitTemplate(oauth2_id="", oauth2_secret="")
    llu.run_forever()
