import numpy as np

class ProceduralPolicy:
    def __init__(self, env, randomized=False, verbose=False):
        self.env = env
        self.randomized = randomized
        self.verbose = verbose
        self.avg_remission_probs = self._calculate_average_remission_probs()
        self.treatment_weights = self._calculate_treatment_weights()
        self.treatments_applied = set()  # Keep track of treatments already applied
        if not randomized:  # Initialize the sequence only if it's not randomized
            self.treatment_sequence = self._generate_treatment_sequence()
        else:
            self.treatment_sequence = []

    def _calculate_average_remission_probs(self):
        avg_remission_probs = {}
        for t in range(self.env.n_treatments):
            total_prob = 0
            for d, disease in enumerate(self.env.diseases.values()):
                # Multiply the remission probability by the stationary distribution of the disease
                total_prob += disease['remission_probs'].get(t, 0) * self.env.stationary_distribution[d] 
            # Only add to the dictionary if the remission probability is not zero
            if total_prob > 0:
                avg_remission_probs[t] = total_prob / len(self.env.diseases)
        return avg_remission_probs

    def _calculate_treatment_weights(self):
        weights = {}
        for treatment, remission_prob in self.avg_remission_probs.items():
            cost = self.env.treatments[f"Treatment_{treatment}"]['base_cost']
            weights[treatment] = remission_prob / cost
        return weights

    def _generate_treatment_sequence(self):
        # Generate the sequence based on sorted treatment weights
        sorted_treatments = sorted(self.treatment_weights.items(), key=lambda item: item[1], reverse=True)
        return [t[0] for t in sorted_treatments]

    def _weighted_random_choice(self, available_treatments):
        # Choose a treatment randomly, weighted by the treatment weights
        weights = [self.treatment_weights[t] for t in available_treatments]
        normalized_weights = np.array(weights) / np.sum(weights)
        return np.random.choice(available_treatments, p=normalized_weights)
    
    def get_treatment(self, current_disease, current_step):
        # Get the list of available treatments, excluding those already applied
        # Ensure that we only include treatments that have non-zero weights
        available_treatments = [t for t in self.treatment_weights.keys() if t not in self.treatments_applied]

        # If all treatments have been tried, return None
        if not available_treatments:
            if self.verbose:
                print("No more available treatments to choose from.")
            return None

        if self.randomized:
            chosen_treatment = self._weighted_random_choice(available_treatments)
        else:
            # For sequential policy, select the next treatment in the sorted sequence
            if not self.treatment_sequence:
                self.treatment_sequence = self._generate_treatment_sequence()
            # Pop the first treatment off the list
            chosen_treatment = self.treatment_sequence.pop(0) if self.treatment_sequence else None

        # Mark the chosen treatment as applied if it's not None
        if chosen_treatment is not None:
            self.treatments_applied.add(chosen_treatment)

        return chosen_treatment
    
    def reset(self):
        self.treatments_applied.clear()
        if not self.randomized:
            self.treatment_sequence = self._generate_treatment_sequence()
    
class QuasiOptimalPolicy:
    def __init__(self, env):
        self.env = env  # The environment instance
    
    def select_action(self, current_disease):
        # Check if the current disease is in remission
        if current_disease == "Remission":
            return None  # No action required
        
        # Retrieve the disease's data from the environment
        disease_info = self.env.diseases[current_disease]
        
        # Find the treatment with the highest remission probability for the current disease
        best_treatment = max(disease_info['remission_probs'], key=disease_info['remission_probs'].get)
        
        return best_treatment

    def step(self, observation):
        current_disease = self.env.current_disease  # Directly accessing the current disease state (which is "cheating")
        
        # Select the action (treatment) with the highest remission probability
        action = self.select_action(current_disease)
        
        return action