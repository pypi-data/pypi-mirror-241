import json
import os
from pathlib import Path
from typing import Any, Dict, Generator, Optional

import grpc
import pyarrow.flight
import yaml
from grpc import (
    ssl_channel_credentials,
)

from .protobufs.bauplan_pb2 import TriggerRunRequest
from .protobufs.bauplan_pb2_grpc import CommanderServiceStub

GRPC_METADATA_HEADER_API_KEY = 'x-bauplan-api-key'


def load_default_config_profile() -> dict:
    home_dir = Path.home()
    config_path = home_dir / '.bauplan/config.yml'

    if not config_path.is_file():
        return {}

    with open(config_path, 'r') as config_file:
        config_data = yaml.safe_load(config_file)

    return config_data.get('profiles', {}).get('default', {})


def dial_commander() -> grpc.Channel:
    addr: str = ''
    env: Optional[str] = os.getenv('BPLN_ENV')
    if env == 'local':
        addr = 'localhost:2758'
    elif env == 'dev':
        addr = 'commander-poc.use1.adev.bauplanlabs.com:443'
    elif env == 'qa':
        addr = 'commander-poc.use1.aqa.bauplanlabs.com:443'
    else:
        addr = 'commander-poc.use1.aprod.bauplanlabs.com:443'
    creds: grpc.ChannelCredentials = ssl_channel_credentials()
    conn: grpc.Channel = grpc.secure_channel(addr, creds)
    return conn


def query(
    query: str,
    max_rows: int = 10,
    no_cache: bool = False,
    branch: str = 'main',
    args: Optional[Dict[str, Any]] = None
) -> Optional[pyarrow.flight.FlightStreamReader]:
    conn: grpc.Channel = dial_commander()
    client: CommanderServiceStub = CommanderServiceStub(conn)

    trigger_run_request: TriggerRunRequest = TriggerRunRequest(
        module_version='0.0.1',
        args=args or {},
        query_for_flight=query,
        is_flight_query=True
    )

    if no_cache:
        trigger_run_request.args['runner-cache'] = 'off'

    if branch:
        trigger_run_request.args['read-branch'] = branch

    api_key = load_default_config_profile().get('api_key', '')
    metadata = [(GRPC_METADATA_HEADER_API_KEY, api_key)]

    job_id: TriggerRunRequest = client.TriggerRun(
        trigger_run_request, metadata=metadata)

    log_stream: grpc.Call = client.SubscribeLogs(job_id, metadata=metadata)

    flight_endpoint: Optional[str] = None
    for log in log_stream:
        if os.getenv('BPLN_DEBUG'):
            print(log)
        if log.task_lifecycle_event.flight_endpoint:
            flight_endpoint = log.task_lifecycle_event.flight_endpoint
            break

    if not flight_endpoint:
        return None

    flight_client: pyarrow.flight.FlightClient = pyarrow.flight.FlightClient(
        'grpc://' + flight_endpoint)
    options: pyarrow.flight.FlightCallOptions = pyarrow.flight.FlightCallOptions(
        headers=[(b'authorization', 'Bearer my_special_token'.encode())]
    )
    ticket: pyarrow.flight.Ticket = next(flight_client.list_flights(
        options=options,
    )).endpoints[0].ticket
    reader: pyarrow.flight.FlightStreamReader = flight_client.do_get(
        ticket,
        options=options,
    )
    return reader


def query_to_pandas(*args: Any, **kwargs: Any) -> Any:
    reader: pyarrow.flight.FlightStreamReader = query(*args, **kwargs)
    if reader is None:
        raise ValueError('No results found')
    return reader.read_pandas()


def query_to_arrow(*args: Any, **kwargs: Any) -> pyarrow.Table:
    reader: pyarrow.flight.FlightStreamReader = query(*args, **kwargs)
    if reader is None:
        raise ValueError('No results found')
    return reader.read_all()


def query_to_generator(*args: Any, **kwargs: Any) -> Generator[Dict[str, Any], None, None]:
    reader: pyarrow.flight.FlightStreamReader = query(*args, **kwargs)
    if reader is None:
        raise ValueError('No results found')
    while True:
        try:
            if reader is None:
                raise ValueError('No results found')
            chunk: Optional[pyarrow.lib.RecordBatch] = reader.read_chunk()
            if chunk is not None:
                batch: pyarrow.lib.RecordBatch = chunk.data
                schema: pyarrow.lib.Schema = batch.schema
                for i in range(batch.num_rows):
                    yield row_to_dict(batch, i, schema)
            else:
                break
        except StopIteration:
            break


def row_to_dict(batch: pyarrow.lib.RecordBatch, row_index: int, schema: pyarrow.lib.Schema) -> Dict[str, Any]:
    row: Dict[str, Any] = {}
    for j, name in enumerate(schema.names):
        column: pyarrow.lib.ChunkedArray = batch.column(j)
        row[name] = column[row_index].as_py()
    return row


def query_to_file(filename: str, *args: Any, **kwargs: Any) -> None:
    if filename.endswith('.json'):
        with open(filename, 'w') as outfile:
            outfile.write('[\n')
            first_row: bool = True
            for row in query_to_generator(*args, **kwargs):
                if not first_row:
                    outfile.write(',\n')
                    first_row = False
                outfile.write(json.dumps(row))
            outfile.write('\n]')
    else:
        raise ValueError('Only .json extension is supported for filename')
