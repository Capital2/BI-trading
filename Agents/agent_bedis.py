class MasterTradingAgent:
    def __init__(self, sma_agent, rsi_agent, obv_agent, macd_agent):
        self.sma_agent = sma_agent
        self.rsi_agent = rsi_agent
        self.obv_agent = obv_agent
        self.macd_agent = macd_agent

    def make_decision(self, state):
        # Get decisions from each agent
        sma_decision = self.sma_agent.predict(state)
        rsi_decision = self.rsi_agent.predict(state)
        obv_decision = self.obv_agent.predict(state)
        macd_decision = self.macd_agent.predict(state)

        # Decision-making logic
        decisions = [sma_decision, rsi_decision, obv_decision, macd_decision]
        final_decision = self.decision_logic(decisions)

        return final_decision

    def decision_logic(self, decisions):
        vote_count = Counter(decisions)
        if vote_count[1] > vote_count[2]:  # More buy votes
            return 1  # Buy
        elif vote_count[2] > vote_count[1]:  # More sell votes
            return 2  # Sell
        return 0  # Hold
