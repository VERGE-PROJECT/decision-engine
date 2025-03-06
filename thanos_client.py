class ThanosClient:
    def __init__(self):
        self.store_api_url = "http://thanos-store-api:10901"
    
    def query_range(self, query, start_time, end_time, step):
        """Query metrics from Thanos Store API"""
        pass  # Implementation details omitted
