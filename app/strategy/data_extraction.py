class DataClean:
    def remove_noise(self,string:str):
        # text_without_start = string[len("```json\n"):]
        # text_without_end = text_without_start[:-len("```\n")]
        start_index = string.find('{')
        end_index = string.rfind('}') + 1
        json_string = string[start_index:end_index]
        return json_string