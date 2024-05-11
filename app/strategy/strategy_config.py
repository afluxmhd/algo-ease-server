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
                 "scrip (string), action ('BUY' or 'SELL'), entry (float), exit (float), entry_time (string), exit_time (string), quantity (int), risk (float percentage), max_loss (float), max_profit (float), risk_reward (float)\n"\
                 "If parameter values are not available, assign empty strings for strings and -1 for float or int. The risk parameter should be a percentage float value. The time format should be ISO 8601 but avoid timezone (eg: 2023-11-07T15:30:00). If the prompt doesn’t contain date, then use today’s date, and adjust accordingly."
                                                              
