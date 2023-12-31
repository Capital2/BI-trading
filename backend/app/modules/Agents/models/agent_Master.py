from collections import Counter
from .agent_price_predictor import PricePredictionAgent
import uuid


class MasterTradingAgent:
    def __init__(self, sma_agent, rsi_agent, obv_agent, macd_agent, predictor):
        self.agents = [sma_agent, rsi_agent, obv_agent, macd_agent, predictor]


    def train_models(self):
        for agent in self.agents:
            agent.train_model()

    def make_decision(self):
        decisions = [self.agents[i].predict(self.agents[i].env.reset()) for i in range(0, len(self.agents) -1)]
        print(f"Decisions: {decisions}")
        return self.apply_decision_rules(decisions)

    def apply_decision_rules(self, decisions):
        vote_count = Counter(decisions)
        consensus = (len(self.agents) -1) // 2 + 1

        if vote_count[1] >= consensus:
            return 1  # Buy
        elif vote_count[2] >= consensus:
            return 2  # Sell

        if vote_count[0] > max(vote_count[1], vote_count[2]):
            return 0  # Hold

        return 0  # Hold as a default action

    def step(self, _balance, days):
        agent = self.agents[len(self.agents) - 1]
        # agent.train_model(epochs=10)
        predictions = agent.predict(days=days)
        balance = _balance

        print(f"Predictions: {predictions}")
        balances = []

        for current_day in range(days):
            action = self.make_decision()
            print(f"Action: {action}")
            current_price = predictions[current_day]
            if action == 1:
                balance -= current_price
            elif action == 2:
                balance += current_price

            balances.append(balance)

        return balances

    def evaluate_all_agents(self, historical_signals):
        accuracy_dict = {}
        for agent, actual_signals in zip(self.agents[:-1], historical_signals):
            accuracy = agent.evaluate(actual_signals)
            accuracy_dict[agent.__class__.__name__] = accuracy
        return accuracy_dict
