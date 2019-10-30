from jutils3.object.data import data_table, data_column, query

class DataObject():
    def __init__(self):
        self.tables_table = data_table.DataTable("tables", data_column.DataColumn("table_name", str), data_column.DataColumn("table", data_table.DataTable))
        self.table_data = {
            "tables": self.tables_table
        }
    
    def add_table(self, table):
        if table.name not in self.table_data:
            self.table_data[table.name] = table
            self.tables_table.insert(table_name = table.name, table = table).perform_updates()
        return self
    
    def remove_table(self, table_name):
        table_data = self.table_data.get(table_name, None)
        del table_data

    def get_table(self, table_name):
        return query.SingleQuery(self.table_data["tables"])\
            .select('table').where(query.ColumnOperation('table_name', lambda name: table_name == name))\
                .execute().get('table', None)
        