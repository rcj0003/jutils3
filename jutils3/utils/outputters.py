from object.object_stream import Stream

class StandardOutputters():
    @staticmethod
    def single_object_outputter(result):
        return None if len(result) == 0 else result[0]

    @staticmethod
    def stream_outputter(result):
        return Stream(result)

class OutputterFactory():
    @staticmethod
    def create_single_column_list_outputter(column_name):
        def output_list(results):
            return Stream(results).map_data(lambda result: result[column_name]).get_results()
        return output_list

    @staticmethod
    def create_mapped_result_outputter(mapper):
        def output_list(results):
            return Stream(results).map_data(mapper).get_results()
        return output_list