class MLModel:
    def __init__(self):
        self.model = None
        self.thresholds = {
            'anomaly_score': 0.8,
            'prediction_confidence': 0.7
        }
    
    def train(self, training_data):
        """
        Train the ML model using historical metrics data
        """
        from sklearn.ensemble import IsolationForest
        self.model = IsolationForest(contamination=0.1)
        self.model.fit(training_data)
    
    def predict(self, metrics_data):
        """
        Predict anomalies and future trends in metrics
        """
        if not self.model:
            raise ValueError("Model not trained")
            
        predictions = self.model.predict(metrics_data)
        anomaly_scores = self.model.decision_function(metrics_data)
        
        return {
            'anomaly_score': anomaly_scores.mean(),
            'prediction': predictions,
            'confidence': self._calculate_confidence(anomaly_scores)
        }
    
    def _calculate_confidence(self, anomaly_scores):
        """
        Calculate prediction confidence based on anomaly scores
        """
        return abs(anomaly_scores.mean()) / self.thresholds['prediction_confidence']
    
    def load_model(self, model_path):
        """
        Load a trained model from file
        """
        import pickle
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
    
    def save_model(self, model_path):
        """
        Save the trained model to file
        """
        import pickle
        with open(model_path, 'wb') as f:
            pickle.dump(self.model, f)
