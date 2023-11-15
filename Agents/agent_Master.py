from collections import Counter


class MasterTradingAgent:
    def __init__(self, sma_agent, rsi_agent, obv_agent, macd_agent):
        self.sma_agent = sma_agent
        self.rsi_agent = rsi_agent
        self.obv_agent = obv_agent
        self.macd_agent = macd_agent

    def train_models(self):
        self.sma_agent.train_model()
        self.obv_agent.train_model()
        self.rsi_agent.train_model()
        self.macd_agent.train_model()

    def make_decision(self):
        # Get decisions from each agent
        sma_decision = self.sma_agent.predict(self.sma_agent.env.reset())
        obv_decision = self.obv_agent.predict(self.obv_agent.env.reset())
        rsi_decision = self.rsi_agent.predict(self.rsi_agent.env.reset())
        macd_decision = self.macd_agent.predict(self.macd_agent.env.reset())

        # Decision-making logic
        decisions = [*sma_decision, *obv_decision, *rsi_decision, *macd_decision]
        print("Decisions: ", decisions)

        final_decision = self.decision_logic(decisions)

        return final_decision

    def decision_logic(self, decisions):
        vote_count = Counter(decisions)
        if vote_count[1] > vote_count[2]:  # More buy votes
            return 1  # Buy
        elif vote_count[2] > vote_count[1]:  # More sell votes
            return 2  # Sell
        return 0  # Hold
