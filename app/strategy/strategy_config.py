history = [
      {
        "role": "user",
        "parts": ["I want to buy 200 shares of Tata Motors today at 10:30 AM. My entry price is $150 per share, and I plan to sell them when the price hits $180 per share. I'm willing to risk $15 per share, with a maximum loss capped at $30 per share. I aim to close the position by 3:00 PM.\nPlease generate JSON data for the provided strategy using the following keys:\n\"scrip\": \"Tata Motors\",\n\"action\": \"buy\",\n\"entry\": 150,\n\"exit\": 180,\n\"entry_time\": \"10:30 AM\",\n\"exit_time\": \"3:00 PM\",\n\"quantity\": 200,\n\"risk\": 15,\n\"max_loss\": 30,\n\"max_profit\": 30,\n\"risk_reward\": 2"]
      },
      {
        "role": "model",
        "parts": ["```json\n{\n\"scrip\": \"Tata Motors\",\n\"action\": \"buy\",\n\"entry\": 150,\n\"exit\": 180,\n\"entry_time\": \"10:30 AM\",\n\"exit_time\": \"3:00 PM\",\n\"quantity\": 200,\n\"risk\": 15,\n\"max_loss\": 30,\n\"max_profit\": 30,\n\"risk_reward\": 2\n}\n```"]
      },
    ]
    
instruction = "\nGenerate JSON for the provided strategy using the following keys:\n"\
                 "scrip, action, entry, exit, entry_time, exit_time, quantity, risk, max_loss, max_profit, risk_reward"\
                 " If parameter values are not available, assign empty strings.,the risk parameter should be percentage float value, the action either BUY or SELL, the time format should be millisecondsSinceEpoch"
