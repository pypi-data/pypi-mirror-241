import os
from dataclasses import is_dataclass, fields


def check_env_vars(env_vars, logger):
    """Checks if the required environment variables are set."""
    for var in env_vars:
        if os.getenv(var) is None:
            message = f"The environment variable {var} is not set. It is required for the database connection."
            logger.error(message)
            raise EnvironmentError(message)


def map_row_to_dataclass(dataclass_type: type, row: tuple, headers: list[str]):
    """
    Maps a database row to a given dataclass type based on headers.

    :param dataclass_type: The type of the dataclass to map to.
    :param row: A tuple representing a row from the database.
    :param headers: A list of strings representing the column names.
    :return: An instance of the specified dataclass with values from the row.
    """
    if not is_dataclass(dataclass_type):
        raise ValueError(f"{dataclass_type.__name__} is not a dataclass")

    dataclass_fields = {f.name: f.type for f in fields(dataclass_type)}
    mapped_data = {}
    for header, value in zip(headers, row):
        if header in dataclass_fields:
            mapped_data[header] = value

    return dataclass_type(**mapped_data)


def get_dataclass_list_from_query(query_result: tuple, class_type: type) -> list[any]:
    data = query_result[0]
    headers = query_result[1]

    data_list = []

    for row in data:
        loan = map_row_to_dataclass(class_type, row, headers)
        data_list.append(loan)

    return data_list
