from collections import Counter


class MasterTradingAgent:
    def __init__(self, sma_agent, rsi_agent, obv_agent, macd_agent):
        self.agents = [sma_agent, rsi_agent, obv_agent, macd_agent]

    def train_models(self):
        for agent in self.agents:
            agent.train_model()

    def make_decision(self):
            # Gather decisions from each agent
            decisions = [agent.predict(agent.env.reset()) for agent in self.agents]
            print(f"Decisions: {decisions}")
            # Apply decision rules
            return self.apply_decision_rules(decisions)
    

    def apply_decision_rules(self, decisions):
        """
        Apply a set of predefined rules to make the final decision.
        :param decisions: List of decisions from each trading agent
        :return: Final decision (0: hold, 1: buy, 2: sell)
        """
        vote_count = Counter(decisions)
        consensus = len(self.agents) // 2 + 1

        if vote_count[1] >= consensus:
            return 1  # Buy
        elif vote_count[2] >= consensus:
            return 2  # Sell

        if vote_count[0] > max(vote_count[1], vote_count[2]):
            return 0  # Hold

        return 0  # Hold as a default action