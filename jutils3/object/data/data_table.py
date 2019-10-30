class DataTable():
   def __init__(self, *columns):
      self.entries = []
      self.columns = columns
      self.updates = []

   def insert(self, **data):
      self.updates.append(lambda: self.__insert(**data))
      return self
   
   def get_column_names(self):
      return [column.name for column in self.columns]

   def __insert(self, **data):
      for column in self.columns:
         if column.required:
            if column.name not in data:
               raise Exception(f"Missing data for column '{column.name}'!")
         elif column.name not in data:
            data[column.name] = column.default
         
         if type(data[column.name]) != column.data_type:
            raise Exception(f"Type doesn't match for '{column.name}'!")
   
         if column.unique:
            for entry in self.entries:
               if entry[column.name] == data[column.name]:
                  raise Exception(f"Unique value expected for '{column.name}'!")

      self.entries.append(data)
	  
      return self
   
   def delete(self, entry):
      self.updates.append(self.entries.remove(entry))
      return self
   
   def perform_updates(self):
      for update in self.updates:
         update()
      self.updates.clear()
      return self
   
   def __repr__(self):
      return f"DataTable[{len(self.entries)}, {self.columns}]"