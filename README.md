# decision-engine

Closed-loop orchestration is an advanced approach to managing and optimizing network and application resources in real-time. It integrates predictive analytics, decision-making, and automated orchestration to ensure efficient and intelligent resource management across distributed infrastructures. By continuously monitoring system performance and utilizing feedback mechanisms, closed-loop orchestration translates high-level performance goals into automated actions, thereby enhancing system reliability, scalability, and overall efficiency. This approach enables proactive adjustments to resource allocation, ensuring that the system can adapt dynamically to changing conditions and demands.

Am important component of the closed-loop orchestration is the Decision ENgine (DE). This repo contains pseudocode for a DE implementation within the framework of a closed/loop orchestration.

The DE comprises several key components, each playing a crucial role in its functionality. Notably, we have integrated the predictive analytics described earlier in the closed/loop orchestration framework as part of the DE, enabling it to communicate with the data aggregator of the observability stack, which in our case is Thanos. 

The DE consists of the following components:
•	thanos_client that handles communication with the metrics layer
•	rules_engine that implements rule-based processing
•	ml_model that provides machine learning capabilities
•	nbi_client that executes orchestration actions

The DE employs the following methods:
•	collect_metrics: this method implements the Metrics Collection Phase from the sequence diagram, coordinates with Thanos Store API for data retrieval and handles time-range queries and metric specifications
•	process_metrics: the method executes the Analysis Phase, parallelizes rule-based and ML processing and combines results for comprehensive analysis
•	make_decisios: this method implements decision logic based on analysis results, maps conditions to specific orchestration actions and follows the conditional flow shown in the sequence diagram
•	execute_actions: the method completes the Action Phase, communicates with NearbyOne Orchestrator (the Multi-Site Orchestrator in VERGE overall architecture) and handles action confirmation and logging

