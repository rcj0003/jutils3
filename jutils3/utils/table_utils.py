from jutils3.object.data.data_table import DataTable
from jutils3.object.data.data_column import DataColumn

def infer_table_from_entry_list(data_set, column_names):
    """Infers the columns for a table based on a list of column names and a entry list data set."""
    if len(data_set) == 0:
        raise Exception("Cannot infer columns from empty entry list!")

    inferred_columns = {}
    entry_length = len(data_set[0])

    for entry in data_set:
        if len(entry) != entry_length:
            raise Exception("Cannot infer columns from entry list, inconsistent entries!")

    for entry in data_set:
        for index in range(entry_length):
            inferred_columns[column_names[index]] = DataColumn(column_names[index], type(entry[index]))

    for entry in data_set:
        for index in range(entry_length):
            if inferred_columns[column_names[index]].data_type != type(entry[index]):
                raise Exception("Cannot infer columns from entry list, inconsistent entries!")
    
    if len(inferred_columns) != len(column_names):
        raise Exception("Cannot infer column names, data types and column names are inconsistent!")

    table = DataTable(*inferred_columns.values())

    for entry in data_set:
        data_entry = {}
        for index in range(entry_length):
            data_entry[column_names[index]] = entry[index]
        table.insert(**data_entry)
    
    return table.perform_updates()

def infer_table_from_dictionary(data_set, key_column_name = 'key'):
    if len(data_set) == 0:
        raise Exception("Cannot infer columns from empty dictionary!")
    
    inferred_columns = {}

    for key, data in data_set.items():
        if key_column_name not in inferred_columns:
            inferred_columns[key_column_name] = DataColumn(key_column_name, type(key), unique = True)

        for column_name, value in data.items():
            if column_name not in inferred_columns:
                inferred_columns[column_name] = DataColumn(column_name, type(value))
    
    table = DataTable(*inferred_columns.values())

    for key, data in data_set.items():
        data_entry = {
            key_column_name: key,
        }

        for column_name, value in data.items():
            data_entry[column_name] = value

        table.insert(**data_entry)

    return table.perform_updates()

def infer_table_from_dictionary_list(data_set):
    if len(data_set) == 0:
        raise Exception("Cannot infer columns from empty dictionary!")
    
    inferred_columns = {}
    
    for entry in data_set:
        for column_name, value in entry.items():
            if column_name not in inferred_columns:
                inferred_columns[column_name] = DataColumn(column_name, type(value))
    
    table = DataTable(*inferred_columns.values())

    for entry in data_set:
        table.insert(**entry)

    return table.perform_updates()