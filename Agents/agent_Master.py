from collections import Counter


class MasterTradingAgent:
    def __init__(self, sma_agent, rsi_agent, obv_agent, macd_agent):
        self.agents = [sma_agent, rsi_agent, obv_agent, macd_agent]

    def train_models(self):
        for agent in self.agents:
            agent.train_model()

    def make_decision(self):
        decisions = [agent.predict(agent.env.reset()) for agent in self.agents]
        print(f"Decisions: {decisions}")
        return self.apply_decision_rules(decisions)

    def apply_decision_rules(self, decisions):
        vote_count = Counter(decisions)
        consensus = len(self.agents) // 2 + 1

        if vote_count[1] >= consensus:
            return 1  # Buy
        elif vote_count[2] >= consensus:
            return 2  # Sell

        if vote_count[0] > max(vote_count[1], vote_count[2]):
            return 0  # Hold

        return 0  # Hold as a default action

    def evaluate_all_agents(self, historical_signals):
        accuracy_dict = {}
        for agent, actual_signals in zip(self.agents, historical_signals):
            accuracy = agent.evaluate(actual_signals)
            accuracy_dict[agent.__class__.__name__] = accuracy
        return accuracy_dict