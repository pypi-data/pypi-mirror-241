from typing import Union

from .connectors.database import MySqlConnector, PostgresConnector
from .connectors.file import ParquetConnector


def _get_connector(
    connector_type: str
) -> Union[PostgresConnector, MySqlConnector, ParquetConnector]:
    supported_connectors = {
        "postgresql": PostgresConnector,
        "mysql": MySqlConnector,
        "parquet": ParquetConnector,
    }
    if connector_type not in supported_connectors:
        raise ValueError(f"The connector {connector_type} is not supported.")
    return supported_connectors[connector_type]


def transfer(
    *,
    source_query: str,
    source_object: str,
    source_connection: dict,
    batch_size: int,
    target_object: str,
    destination_connection: dict,
):
    source_connector = _get_connector(source_connection["type"])(
        connection_parameters=source_connection.get("parameters"),
    )
    destination_connector = _get_connector(destination_connection["type"])(
        connection_parameters=destination_connection.get("parameters"),
    )
    batch_iterator = source_connector.extract(
        source_query=source_query,
        source_object=source_object,
        batch_size=batch_size,
    )
    destination_connector.load(
        batch_iterator=batch_iterator,
        target_object=target_object,
    )
