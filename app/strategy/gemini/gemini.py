from configs import generation_config, genai
from safety_settings import safety_settings

string: str = "I want to buy shares of hdfc bank of 100 shares. It should buy at 458 level, and stop loss of 420, and max profit of 1000. The trade should taken at 12:00 and exit at 3:10"

system_instruction = "Generate ONLY JSON and it shouldn't contain other than json"
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", generation_config=generation_config,safety_settings=safety_settings) # type: ignore
convo = model.start_chat(history=[
  {
    "role": "user",
    "parts": ["I want to buy 200 shares of Tata Motors today at 10:30 AM. My entry price is $150 per share, and I plan to sell them when the price hits $180 per share. I'm willing to risk $15 per share, with a maximum loss capped at $30 per share. I aim to close the position by 3:00 PM.\nPlease generate JSON data for the provided strategy using the following keys:\n\"scrip\": \"Tata Motors\",\n\"action\": \"buy\",\n\"entry\": 150,\n\"exit\": 180,\n\"entry_time\": \"10:30 AM\",\n\"exit_time\": \"3:00 PM\",\n\"quantity\": 200,\n\"risk\": 15,\n\"max_loss\": 30,\n\"max_profit\": 30,\n\"risk_reward\": 2"]
  },
  {
    "role": "model",
    "parts": ["```json\n{\n\"scrip\": \"Tata Motors\",\n\"action\": \"buy\",\n\"entry\": 150,\n\"exit\": 180,\n\"entry_time\": \"10:30 AM\",\n\"exit_time\": \"3:00 PM\",\n\"quantity\": 200,\n\"risk\": 15,\n\"max_loss\": 30,\n\"max_profit\": 30,\n\"risk_reward\": 2\n}\n```"]
  },
])
instruction = "\nGenerate JSON for the provided strategy using the following keys:\n"\
             "scrip, action, entry, exit, entry_time, exit_time, quantity, risk, max_loss, max_profit, risk_reward"\
             " If parameter values are not available, assign empty strings."
convo.send_message(instruction+"**Generate JSON only**\n" +string)
print(convo.last.text) # type: ignore