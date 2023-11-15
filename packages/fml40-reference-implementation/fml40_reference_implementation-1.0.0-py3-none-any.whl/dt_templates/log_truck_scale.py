from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import log_truck_scale


class LogTruckScaleTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        log_truck_scale["thingId"] = oauth2_id
        log_truck_scale["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(log_truck_scale)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(log_truck_scale["attributes"].get("name", None))
        super(LogTruckScaleTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    scale = LogTruckScaleTemplate(oauth2_id="", oauth2_secret="")
    scale.run_forever()
