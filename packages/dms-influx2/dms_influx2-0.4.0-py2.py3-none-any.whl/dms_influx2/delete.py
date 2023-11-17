import itertools
import logging
from datetime import datetime, timedelta
from typing import Union

from dateutil.parser import parse
from influxdb_client import DeleteApi

from dms_influx2.utils import timestamp_to_influx_string

logger = logging.getLogger(__name__)


class Delete(DeleteApi):
    def __init__(self, client):
        self.org = client.org
        self.time_offset = client.time_offset
        self.query_str = client.query_str
        super().__init__(client)

    def delete_data(self,
                    bucket,
                    measurements=None,
                    device_ids=None,
                    descriptions=None,
                    org: str = None,
                    time_range: str = None,
                    time_from: Union[str, datetime] = None,
                    time_to: Union[str, datetime] = None) -> dict:

        # TODO: add time_range
        if time_range is not None:
            pass

        if org is None:
            org = self.org

        if time_from is None:
            start = "1900-01-01T00:00:00Z"
        else:
            start = timestamp_to_influx_string(time_from, self.time_offset)

        if time_to is None:
            # Add some safety timedelta
            stop_time = datetime.now() + timedelta(days=1)
            stop = timestamp_to_influx_string(stop_time, self.time_offset)
        else:
            stop = timestamp_to_influx_string(time_to, self.time_offset)

        predicates = []

        if measurements is not None:
            _predicates = []
            for measurement in measurements:
                _predicates.append(f'_measurement="{measurement}"')
            predicates.append(_predicates)

        if device_ids is not None:
            _predicates = []
            for device_id in device_ids:
                _predicates.append(f'device_id="{device_id}"')
            predicates.append(_predicates)

        if descriptions is not None:
            _predicates = []
            for description in descriptions:
                _predicates.append(f'description="{description}"')
            predicates.append(_predicates)

        # Filter empty lists and find all combinations for predicates, execute all queries
        predicates = list(filter(None, predicates))
        predicates = [predicate for predicate in itertools.product(*predicates)]
        predicates = [" and ".join(i for i in predicate) for predicate in predicates]
        predicates = list(dict.fromkeys(predicates))
        for predicate in predicates:
            self.delete(start=parse(start), stop=parse(stop), predicate=predicate, bucket=bucket, org=org)
            logger.debug(f"Delete data {parse(start)}->{parse(stop)} from bucket: {bucket}, predicate: {predicate}")
        return {"start": start, "stop": stop, "predicates": predicates}
