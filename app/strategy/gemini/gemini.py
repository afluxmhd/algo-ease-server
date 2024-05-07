# import json
import re
from app.strategy.gemini.config import generation_config, genai
from app.strategy.gemini.safety_settings import safety_settings

class Gemini:

  def send_prompt(self,prompt:str,history:list,instruction:str):
    model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config,safety_settings=safety_settings) # type: ignore
    convo = model.start_chat(history = history)
    convo.send_message(instruction+"**Generate JSON only**\n" +prompt)
    return convo.last.text # type: ignore
    








































  

   


