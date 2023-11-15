from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import mill_gate


class MillGateTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        mill_gate["thingId"] = oauth2_id
        mill_gate["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(mill_gate)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(mill_gate["attributes"].get("name", None))
        super(MillGateTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    gate = MillGateTemplate(oauth2_id="", oauth2_secret="")
    gate.run_forever()

