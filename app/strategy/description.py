

class ModelDescription:
    
    def get_model_description(self,json_data):
        market_condition = self._get_market_condition(json_data.get("action", ""))
        action_description = self._get_action_description(json_data.get("action", ""))
    

        risk = json_data.get("risk", 0)
        risk_reward = json_data.get("risk_reward", 0)
        favorable_description=self._is_favorable_risk_reward(risk_reward)
        max_profit = json_data.get("max_profit", 0)
    
    
        profit_level = self._profit_level_description(max_profit,json_data)
    
        dynamic_text = f"This model is designed for {market_condition} market conditions, providing a {action_description} action with the potential for a {profit_level} profit. It carries a risk level of about {risk}%, with the possibility of some losses. {favorable_description}, making it suitable for traders looking to capitalize on {'upward' if json_data['action'] == 'BUY' else 'downward'} market trends while managing risk effectively."
    
        return dynamic_text
    
    def _profit_level_description(self,profit, json_data):
        # Extract profit data from the JSON data
        max_profit = json_data.get("max_profit", 0)
        max_loss = json_data.get("max_loss", 0)

        # Calculate quartiles based on the profit data
        profit_quartile_1 = max_loss + (max_profit - max_loss) * 0.25  # 25th percentile
        profit_quartile_3 = max_loss + (max_profit - max_loss) * 0.75  # 75th percentile

        # Determine profit level based on quartiles
        if profit < profit_quartile_1:
            return "low"
        elif profit < profit_quartile_3:
            return "moderate"
        else:
            return "good"

    def _is_favorable_risk_reward(self,risk_reward_ratio, favorable_threshold=1.0):
  
        if risk_reward_ratio >= favorable_threshold:
            return "The risk-reward ratio is favorable."
        else:
            return "The risk-reward ratio is not favorable."



    def _get_market_condition(self, action):
        return "bullish" if action == "BUY" else "bearish"

    def _get_action_description(self,action):
        return "recommendation to BUY" if action == "BUY" else "suggestion to SELL"
