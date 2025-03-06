class NBIClient:
    def __init__(self):
        self.nbi_url = "http://nearbyone-nbi:8080"
        self.auth_token = None
    
    def execute_action(self, action, target, parameters):
        """
        Execute orchestration action through NearbyOne NBI API
        """
        if not self.auth_token:
            self.authenticate()
            
        headers = {
            'Authorization': f'Bearer {self.auth_token}',
            'Content-Type': 'application/json'
        }
        
        action_data = {
            'action': action,
            'target': target,
            'parameters': parameters
        }
        
        response = requests.post(
            f"{self.nbi_url}/api/v1/orchestration/actions",
            json=action_data,
            headers=headers
        )
        
        self.handle_error(response)
        return response.json()
    
    def authenticate(self):
        """
        Authenticate with NearbyOne NBI API
        """
        auth_url = f"{self.nbi_url}/api/v1/auth/token"
        response = requests.post(auth_url, auth=('username', 'password'))
        self.handle_error(response)
        self.auth_token = response.json()['token']
    
    def get_service_status(self, service_name):
        """
        Get current status of a service
        """
        response = requests.get(
            f"{self.nbi_url}/api/v1/services/{service_name}",
            headers={'Authorization': f'Bearer {self.auth_token}'}
        )
        self.handle_error(response)
        return response.json()
    
    def handle_error(self, response):
        """
        Handle API errors gracefully
        """
        if not response.ok:
            raise OrchestrationError(
                f"API error {response.status_code}: {response.text}"
            )
