class RulesEngine:
    def __init__(self):
        self.rules = {}
        self.thresholds = {}
        
    def evaluate(self, metrics_data):
        """
        Evaluate metrics against defined rules
        """
        results = {}
        
        for rule_name, rule in self.rules.items():
            result = rule['condition'](metrics_data)
            results[rule_name] = {
                'passed': result,
                'threshold': self.thresholds.get(rule_name),
                'metrics': metrics_data
            }
            
        return results
    
    def add_rule(self, rule_name, condition, action):
        """
        Add a new rule to the engine
        """
        self.rules[rule_name] = {
            'condition': condition,
            'action': action
        }
        self.thresholds[rule_name] = None
    
    def remove_rule(self, rule_name):
        """
        Remove a rule from the engine
        """
        if rule_name in self.rules:
            del self.rules[rule_name]
            del self.thresholds[rule_name]
    
    def update_threshold(self, rule_name, threshold):
        """
        Update the threshold for a specific rule
        """
        if rule_name in self.rules:
            self.thresholds[rule_name] = threshold
