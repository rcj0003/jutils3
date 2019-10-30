from jutils3.utils import utils

class Stream():
   """Offers functionality similar to Java's Stream class."""
   def __init__(self, *results):
      self.results = []
      for x in results:
         if hasattr(x, "__iter__"):
            self.results += list(x)
         else:
            self.results.append(x)

   def __iter__(self):
      for x in self.results:
         yield x

   def __getitem__(self, key):
      return self.results[key]

   def __bool__(self):
      return len(self.results) > 0

   def __len__(self):
      return len(self.results)

   def __add__(self, other):
      if hasattr(other, "__iter__"):
         self.results = self.results + list(other)
      else:
         self.results.append(other)
      return self

   def __iadd__(self, other):
      if hasattr(other, "__iter__"):
         self.results = self.results + list(other)
      else:
         self.results.append(other)
      return self

   def __repr__(self):
      return "Stream[%s]" % self.results
        
   def map_data(self, function, data = None):
      """Maps the provides data using the provided function and stores it as the results.\n'function' - The function to be used to map the results.\n'data' - The data to be mapped. If no argument is provided, the already stored results will be used."""
      if data == None:
         data = self.results
      self.results = list(map(function, list(data)))
      return self

   def selective_map(self, filter_function, map_function):
      """Maps only the stored data that passes the filter function provided.\n'filter_function' - The function to filter the results.\n'map_function' - The function to be used for mapping."""
      plist = utils.create_embedded_list(range(0, len(self)), self)
      Stream(plist).filter_results(lambda x: filter_function(x[1])).for_each(lambda x: Stream.__setElementAt(self.results, x[0], map_function(x[1])))
      return self
   
   def add_map_to_results(self, function, data):
      """Maps the provides data using the provided function and adds it the current results.\n'function' - The function to be used to map the results.\n'data' - The data to be mapped."""
      self.results += list(map(function, list(data)))
      return self
    
   def filter_results(self, function):
      """Filters stored results using the function provided, and thus alters the final result.\n'function' - The function used to filter the stored results."""
      self.results = list(filter(function, self.results))
      return self

   def for_each(self, function):
      """Executes the given function and passes each stored result as a parameter."""
      for element in self:
         function(element)
      return self

   def get_results(self):
      """Returns the results of all maps and filters."""
      return list(self.results)

   def clear(self):
      """Clears stored results."""
      self.results.clear()
      return self

   @staticmethod
   def __setElementAt(plist, index, newElement):
      # Internal function so we can do an assignment operator in a lambda, normally not allowed.
      plist[index] = newElement