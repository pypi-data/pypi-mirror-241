import os
import numpy as np
import networkx as nx

class ProbabilisticSymptomConditionGraph:
    def __init__(self, condition_names, symptom_names, graph, similarity_matrix=None, similarity_cutoff=0.65):
        self.symptom_names = symptom_names
        self.symptom_to_index = {symptom:i for i,symptom in enumerate(self.symptom_names)}
        self.condition_names = condition_names
        self.condition_to_index = {condition:i for i,condition in enumerate(self.condition_names)}
        self.similarity_cutoff = similarity_cutoff
        self.graph = graph
        
        # Normalize matrix
        self.similarity_matrix = similarity_matrix
        
    def get_all_symptoms(self):
        return self.symptom_names

    def get_all_conditions(self):
        return self.condition_names

    def get_condition_probs(self, symptoms):
        probabilities = np.array([self.graph.nodes[condition_name]["prevalence"] for condition_name in self.condition_names]) # Probabilities
        
        # Get symptom prevelance
        symptom_weights = np.zeros(len(self.symptom_names)) # How much of each symptom there is present
        if type(self.similarity_matrix) is np.ndarray:
            for symptom in symptoms:
                symptom_row = self.similarity_matrix[self.symptom_to_index[symptom]]
                symptom_row = (symptom_row - symptom_row.min()) / (symptom_row.max() - symptom_row.min())
                symptom_row[symptom_row <= self.similarity_cutoff] = 0
                symptom_weights += symptom_row
        else:
            for symptom in symptoms:
                symptom_weights[self.symptom_to_index[symptom]] = 1.0
                
        # Check each edge
        for condition_name in self.condition_names:
            best_weight = 0.0001
            for symp in self.symptom_names:
                symp_weight = symptom_weights[self.symptom_to_index[symp]]
                edge_data = self.graph.get_edge_data(condition_name, symp)
                if symp_weight != 0:
                    if edge_data != None and symp_weight == 1.0:
                        probabilities[self.condition_to_index[condition_name]] *= symp_weight * edge_data["prevalence"] / 100
                        best_weight = 1.0
                    elif edge_data != None:
                        best_weight = max(best_weight, 0.1 * symp_weight * edge_data["prevalence"] / 100)
    
                if edge_data == None and symp_weight == 1.0:
                    probabilities[self.condition_to_index[condition_name]] *= 0.01
                
            probabilities[self.condition_to_index[condition_name]] *= best_weight
        
        
        # Normalize
        chance_sum = probabilities.sum()
        probs = {}
        for i in range(len(probabilities)):
            probs[self.condition_names[i]] = probabilities[i] / chance_sum
            
        return sorted(probs.items(), key=lambda x:-x[1])
        
# medical_condition_names = list(set(medical_condition_names))
# all_symptoms = list(set(all_symptoms))
# BayesianSymptomConditionGraph(medical_condition_names, all_symptoms, G, similarity_matrix).get_condition_probs(["runny nose", "cough", "fever"])