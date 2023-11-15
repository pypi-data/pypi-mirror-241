from ml import Thing, build, S3IConnector, setup_logger
import asyncio
from dt_templates.json_models import forwarding_agency


class ForwardingAgencyTemplate(Thing):
    def __init__(self, oauth2_id, oauth2_secret):
        forwarding_agency["thingId"] = oauth2_id
        forwarding_agency["policyId"] = oauth2_id
        loop = asyncio.get_event_loop()
        entry = build(forwarding_agency)
        connector = S3IConnector(
            oauth2_id=oauth2_id,
            oauth2_secret=oauth2_secret,
            is_repository=True,
            is_broker_rest=False,
            is_broker=True,
            dt_entry_ins=entry,
            loop=loop
        )
        setup_logger(forwarding_agency["attributes"].get("name", None))
        super(ForwardingAgencyTemplate, self).__init__(
            loop=loop,
            entry=entry,
            connector=connector
        )


if __name__ == "__main__":
    fa = ForwardingAgencyTemplate(oauth2_id="", oauth2_secret="")
    fa.run_forever()

