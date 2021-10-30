"""Utility functions."""

__author__ = "730400423"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    
    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)

    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = table[0]
    for column in first_row:
        result[column] = column_values(table, column)

    return result


def head(table: dict[str, list[str]], number_of_rows: int) -> dict[str, list[str]]:
    """Just using the first x amount of values in each column."""
    result: dict[str, list[str]] = {}
    if number_of_rows >= len(table):
        return table
    else:
        for column in table:
            list_result: list[str] = []
            i: int = 0
            while i < number_of_rows:
                list_result.append(table[column][i])
                i += 1
            result[column] = list_result
        return result


def select(table: dict[str, list[str]], columns: list[str]) -> dict[str, list[str]]:
    """Produce a new specific column based table with certain columns."""
    result: dict[str, list[str]] = {}
    for column in columns:
        result[column] = table[column]
    return result


def concat(table_one: dict[str, list[str]], table_two: dict[str, list[str]]) -> dict[str, list[str]]:
    """A new, combined, column-based table."""
    result: dict[str, list[str]] = {}
    for column_one in table_one:
        result[column_one] = table_one[column_one]
    for column_two in table_two:
        if column_two in result:
            result[column_two] = table_one[column_two] + table_two[column_two]
        else:
            result[column_two] = table_two[column_two]
    return result


def count(list_values: list[str]) -> dict[str, int]:
    """Produces a dictionary from a list that counts how many times a value appears."""
    counts: dict[str, int] = {}
    for value in list_values:
        if value in counts:
            counts[value] += 1
        else:
            counts[value] = 1
    return counts