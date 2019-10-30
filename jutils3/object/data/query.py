class ColumnOperation():
	def __init__(self, column_name, condition):
		self.column_name = column_name
		self.condition = condition

class Query():
	def __init__(self, table):
		self.table = table
		self.conditions = []
		self.columns = table.get_column_names()
		self.output_converter = lambda results: results
		self.orderer = None
		self.descending = False
		self.result_limit = -1
	
	def select(self, *columns):
		self.columns = columns
		return self

	def where(self, *conditions):
		self.conditions = conditions
		return self

	def outputter(self, output_converter):
		self.output_converter = output_converter
		return self
	
	def order_by(self, orderer, descending = False):
		self.orderer = orderer
		self.descending = descending
		return self
	
	def limit(self, result_limit):
		self.result_limit = result_limit
		return self

	def execute(self):
		return self.output_converter([])
	
	def clone(self):
		clone_query = self.__class__(self.table)
		
		clone_query.conditions = self.conditions
		clone_query.columns = self.columns
		clone_query.output_converter = self.output_converter
		clone_query.orderer = self.orderer
		clone_query.descending = self.descending
		clone_query.result_limit = self.result_limit

		return clone_query

class MultiQuery(Query):
	def execute(self):
		results = []
		conditions_met = False

		entries = self.table.entries

		if self.orderer != None:
			entries = list(entries)
			entries.sort(key = lambda element: self.orderer.condition(element[self.orderer.column_name]), reverse = self.descending)

		for entry in entries:
			if self.result_limit > 0 and len(results) >= self.result_limit:
				break

			conditions_met = True

			for condition in self.conditions:
				if not condition.condition(entry[condition.column_name]):
					conditions_met = False
					break

			if conditions_met:
				result = {}

				for column in self.columns:
					result[column] = entry[column]
				
				results.append(result)

		return self.output_converter(results)

class SingleQuery(Query):
	def execute(self):
		results = []
		conditions_met = False

		entries = self.table.entries

		if self.orderer != None:
			entries = list(entries)
			entries.sort(key = lambda element: self.orderer.condition(element[self.orderer.column_name]), reverse = self.descending)

		for entry in entries:
			conditions_met = True

			for condition in self.conditions:
				if not condition.condition(entry[condition.column_name]):
					conditions_met = False
					break
					
			if conditions_met:
				if len(results) > 0:
					raise Exception("A result was already found for the query!")

				result = {}

				for column in self.columns:
					result[column] = entry[column]
				
				results.append(result)
		
		return self.output_converter(result)