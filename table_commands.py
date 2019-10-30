import jutils3.terminal.decorators as decorators
import jutils3.utils.table_utils as tu
import jutils3.utils.query_utils as qu
from jutils3.utils.config_utils import load_config
from jutils3.object.data.query import ColumnOperation, Query, MultiQuery
from jutils3.object.data.data_table import DataTable
from jutils3.utils import utils

@decorators.description("Infers and loads the table based on dictionary data.")
@decorators.minimum_args(1)
def dicloadinf(terminal, arguments, data = None):
    try:
        if data == None:
            if len(arguments) > 1:
                data = load_config(arguments[1])
            else:
                terminal.output("You must provide a file to construct the table from or pass table data!")
                return
        if type(data) is not dict:
            terminal.output("Valid data must be provided to load table!")

        table = tu.infer_table_from_dictionary(**data)
        terminal.variables[f"table_{arguments[0]}"] = table
    except:
        terminal.output("Table cannot be inferred from data, operation failed.")
    
    return table

@decorators.description("Infers and loads the table based on a list of dictionaries.")
@decorators.minimum_args(1)
def dlsloadinf(terminal, arguments, data = None):
    try:
        if data == None:
            if len(arguments) > 1:
                data = load_config(arguments[1])
            else:
                terminal.output("You must provide a file to construct the table from or pass table data!")
                return
        if type(data) is not list:
            terminal.output("Valid data must be provided to load table!")

        table = tu.infer_table_from_dictionary_list(data)
        terminal.variables[f"table_{arguments[0]}"] = table
    except:
        terminal.output("Table cannot be inferred from data, operation failed.")
    
    return table

@decorators.description("Infers and loads the table based on CSV data. The first argument is the table name, second is the file, and the second is the delimiter.")
@decorators.minimum_args(3)
def csvloadinf(terminal, arguments, data = None):
    try:
        column_names = []
        data = []

        with open(arguments[1], 'r') as file:
            column_names = file.readline().strip().split(arguments[2])

            for line in file.readlines():
                data.append(line.strip().split(arguments[2]))
        
        table = tu.infer_table_from_entry_list(data, column_names)
        terminal.variables[f"table_{arguments[0]}"] = table
    except:
        terminal.output("Table cannot be inferred from data, operation failed.")
    
    return table

@decorators.description("Specifies a table to perform operations on. Passes on a query to the next command.")
@decorators.minimum_args(1)
def fromtbl(terminal, arguments, data = None):
    table = terminal.variables.get(f"table_{arguments[0]}", None)

    if table == None:
        terminal.output("No table found with name {arguments[0]}.")
        return
    
    if type(table) is not DataTable:
        terminal.output("The variable is not of type 'DataTable'!")
        return
    
    return MultiQuery(table)

@decorators.description("Peeks at data from the passed query. A query must be passed for the command to succeed.")
@decorators.requires_data(Query)
def peek(terminal, arguments, data = None):
    qu.format_results(data.columns, data.execute())
    return data

@decorators.description("Selects columns from the passed query. A query must be passed for the command to succeed.")
@decorators.requires_data(Query)
def select(terminal, arguments, data = None):
    return data.select(*arguments)

@decorators.description("Searches for data based on the provided arguments.", "The first argument is the column and the second is the term.", "A query must be passed for the command to succeed.")
@decorators.requires_data(Query)
def search(terminal, arguments, data = None):
    return data.where(ColumnOperation(arguments[0], lambda element: arguments[1].lower() in element.lower()))

@decorators.description("Limits data of query results.", "A query must be passed for the command to succeed.")
@decorators.requires_data(Query)
def limit(terminal, arguments, data = None):
    return data.limit(utils.try_parse(arguments[0], -1))

@decorators.description("Executes results of query and passes it on to the next command. A query must be passed for the command to succeed.")
@decorators.requires_data(Query)
def results(terminal, arguments, data = None):
    results = data.execute()
    qu.format_results(data.columns, results)
    return results