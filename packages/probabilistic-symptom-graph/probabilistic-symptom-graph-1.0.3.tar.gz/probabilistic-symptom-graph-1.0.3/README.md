# Probabilistic Symptom Graph

```bash
pip install probabilistic-symptom-graph
```

```py
from src.ProbabilisticSymptomGraph import ProbabilisticSymptomConditionGraph

import networkx as nx
import numpy as np

medical_condition_gexf = "./data/medical-condition-symptom-graph.gexf"
graph = nx.read_gexf(medical_condition_gexf)
sim_matrix = np.load('./data/md-symptom-sim-mat.npy')

symptom_names = []
for node_id, tpe in graph.nodes(data="type"):
    if tpe == "Symptom":
        symptom_names.append(node_id)
symptom_names = sorted(symptom_names)

condition_names = []
for node_id, tpe in graph.nodes(data="type"):
    if tpe == "MedicalCondition":
        condition_names.append(node_id)
condition_names = sorted(condition_names)

probabilistic_graph = ProbabilisticSymptomConditionGraph(condition_names, symptom_names, graph, sim_matrix)
print(" | ".join(probabilistic_graph.get_all_symptoms()[:10]))
probabilistic_graph.get_condition_probs(["acne"])[:5]
```

## Graph Image
Red nodes represent medical conditions and green nodes represent symptoms.
![image](https://github.com/bart1259/ProbabilisticSymptomGraph/assets/21147581/1f693ddf-20d8-4320-9265-a84a3403a5eb)
This graph data was gathered by mining Wikipedia "Medical Condition (New)" infoboxes and extracting medical condition <=> Symptom pairs. Post processing was done using ChatGPT.

## Data Mining
See `./data/WikipediaSymptomExtractor.ipynb`