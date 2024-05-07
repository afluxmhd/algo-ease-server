class DataClean:
    def remove_noise(self,string:str):
        text_without_start = string[len("```json\n"):]
        text_without_end = text_without_start[:-len("````\n")]
        result = text_without_end
        return result