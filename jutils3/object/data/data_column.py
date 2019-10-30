class DataColumn():
    def __init__(self, name, data_type, required = True, unique = False, default = None):
        self.name = name
        self.data_type = data_type
        self.required = required
        self.unique = unique
        self.default = default
    
    def __repr__(self):
        return "DataColumn(%s, %s, %s, %s, %s)" % (self.name, self.data_type, self.required, self.unique, self.default)