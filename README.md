# decision-engine

Closed-loop orchestration is an advanced approach to managing and optimizing network and application resources in real-time. It integrates predictive analytics, decision-making, and automated orchestration to ensure efficient and intelligent resource management across distributed infrastructures. By continuously monitoring system performance and utilizing feedback mechanisms, closed-loop orchestration translates high-level performance goals into automated actions, thereby enhancing system reliability, scalability, and overall efficiency. This approach enables proactive adjustments to resource allocation, ensuring that the system can adapt dynamically to changing conditions and demands.

Am important component of the closed-loop orchestration is the Decision ENgine (DE). This repo contains pseudocode for a DE implementation.

The DE comprises several key components, each playing a crucial role in its functionality. Notably, we have integrated the predictive analytics described earlier in the closed/loop orchestration framework as part of the DE, enabling it to communicate with the data aggregator of the observability stack, which in our case is Thanos. 
These components include the thanos_client, which handles communication with the metrics layer; the rules_engine, responsible for implementing rule-based processing; the ml_model, which provides machine learning capabilities; and the nbi_client, which executes orchestration actions.
The DE employs a series of methods to ensure efficient operation. These methods include collect_metrics, which coordinates with the Thanos Store API for data retrieval during the Metrics Collection Phase; process_metrics, which executes the Analysis Phase by parallelizing rule-based and ML processing; make_decisions, which implements decision logic based on analysis results; and execute_actions, which completes the Action Phase by communicating with the NearbyOne Orchestrator (Multi-Site Orchestrator in VERGE overall architecture) and handling action confirmation and logging.
