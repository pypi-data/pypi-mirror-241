import gym
import numpy as np
import scipy.linalg as la
from scipy.sparse.csgraph import connected_components

def get_communicating_classes(matrix):
    """ Finds the communicating classes in the Markov chain. """
    # Use scipy's connected_components to find the strongly connected components
    n_components, labels = connected_components(csgraph=matrix, directed=True, return_labels=True)
    
    # Create a list of lists to hold states for each communicating class
    classes = [[] for _ in range(n_components)]
    for index, label in enumerate(labels):
        classes[label].append(index)
    
    return classes

def get_stationary_distribution_for_class(matrix, communicating_class):
    """ Finds the stationary distribution for a communicating class. """
    # Extract the submatrix corresponding to the communicating class
    submatrix = matrix[communicating_class, :][:, communicating_class]
    
    # Number of states in the class
    n = len(submatrix)
    
    # Create an augmented matrix to account for the normalization condition
    # We stack an additional row for the constraint that probabilities sum to 1
    A = np.vstack((submatrix - np.eye(n), np.ones(n)))
    b = np.zeros(n + 1)
    b[-1] = 1  # The sum of the probabilities should be 1

    # Solve the system of linear equations
    pi, residuals, rank, s = la.lstsq(A.T, b)  # Transpose A to solve the left eigenvector problem

    # Return the stationary distribution for the class, with zero-padding for the other states
    full_pi = np.zeros(len(matrix))
    for i, state in enumerate(communicating_class):
        full_pi[state] = pi[i]

    return full_pi

def combine_distributions(distributions, weights):
    """ Combine distributions weighted by the size of each class. """
    combined_distribution = np.zeros_like(distributions[0])
    for dist, weight in zip(distributions, weights):
        combined_distribution += dist * weight
    return combined_distribution / combined_distribution.sum()

def analyze_markov_chain(matrix):
    """ Analyze the Markov chain to find the stationary distribution. """
    # Find the communicating classes
    classes = get_communicating_classes(matrix)
    
    # Handle the reducible case
    if len(classes) > 1:
        # Calculate the stationary distribution for each class
        distributions = [get_stationary_distribution_for_class(matrix, c) for c in classes]
        # Assuming a uniform initial distribution, the weight is the relative size of the class
        weights = [len(c) / len(matrix) for c in classes]
        # Combine the distributions
        return combine_distributions(distributions, weights)
    # Handle the irreducible case
    else:
        return get_stationary_distribution_for_class(matrix, classes[0])

def calculate_stationary_distribution(matrix, communicating_classes):
    """
    Calculates the stationary distribution for the entire Markov chain
    given the communicating classes and assuming a uniform initial distribution over states.
    """
    n = matrix.shape[0]  # Total number of states in the Markov chain
    uniform_initial_distribution = np.ones(n) / n  # Uniform distribution over states

    # Initialize the stationary distribution for the entire chain
    full_stationary_distribution = np.zeros(n)

    # Calculate the stationary distribution for each communicating class
    for states in communicating_classes:
        # Formulate the system πP = π
        submatrix = matrix[states][:, states]
        num_states_in_class = len(submatrix)
        A = np.vstack((submatrix.T - np.eye(num_states_in_class), np.ones(num_states_in_class)))
        b = np.zeros(num_states_in_class + 1)
        b[-1] = 1  # The sum of probabilities should be 1

        # Solve the system
        pi, _, _, _ = la.lstsq(A, b)

        # Assign the stationary distribution to the full distribution
        # weighted by the initial probability of the states in the class
        for i, state in enumerate(states):
            full_stationary_distribution[state] = pi[i] * (num_states_in_class / n)

    # Normalize the stationary distribution to ensure it sums to 1
    full_stationary_distribution /= full_stationary_distribution.sum()

    return full_stationary_distribution

class DiseaseTreatmentEnv(gym.Env):
    """Environment to model disease treatment using RL."""

    def __init__(self, 
                 n_diseases=3, 
                 n_treatments=5, 
                 n_symptoms=7, 
                 treatment_cost_range=(1, 5),
                 disease_cost_range=(1, 10), 
                 symptom_modulation_range=(-0.5, 0.25),
                 remission_reward=64,
                 seed=1,
                 max_visits=8,
                 use_gymnasium=False,
                 use_symptom_rewards=True,
                 use_disease_rewards=False,
                 treatment_affect_observation=False):
        super(DiseaseTreatmentEnv, self).__init__()

        # Create a non-defaut numpy rng
        rng = np.random.RandomState(seed)

        # Configurable parameters
        self.treatment_cost_range = treatment_cost_range
        self.disease_cost_range = disease_cost_range
        self.symptom_modulation_range = symptom_modulation_range
        self.remission_reward = remission_reward
        self.max_visits=max_visits
        self.use_symptom_rewards = use_symptom_rewards
        self.use_disease_rewards = use_disease_rewards
        self.treatment_affect_observation = treatment_affect_observation

        # Step tracking
        self.visit_number = 0

        # Action and observation spaces
        if use_gymnasium:
            import gymnasium
            self.action_space = gymnasium.spaces.Discrete(n_treatments)
            self.observation_space = gymnasium.spaces.Box(low=0, high=1,
                 shape=(n_symptoms + n_treatments,), dtype=np.float32)
        else:
            self.action_space = gym.spaces.Discrete(n_treatments)
            self.observation_space = gym.spaces.Box(low=0, high=1,
                 shape=(n_symptoms + n_treatments,), dtype=np.float32)

        self.n_diseases = n_diseases
        self.n_treatments = n_treatments
        self.n_symptoms = n_symptoms

        self.connection_probability = 1 / n_diseases
        
        self.generate_diseases(rng)
        self.disease_list = list(self.diseases.keys())
        self.treatments = self.generate_treatments(rng)

        self.current_disease = None
        self.current_symptoms = np.zeros(n_symptoms)
        self.generate_transition_matrix(rng)
        self.compute_stationary_distribution()
        self.reset()

    def generate_transition_matrix(self, rng):
        # Initialize a matrix filled with zeros for off-diagonal elements, and ones on the diagonal
        self.transition_matrix = np.eye(self.n_diseases)
        
        for i in range(self.n_diseases):
            for j in range(self.n_diseases):
                if i != j:
                    if rng.rand() < self.connection_probability:  # Check for connection
                        # Transition probabilities between 1% to 20%
                        self.transition_matrix[i][j] = rng.uniform(0.01, 0.2)
                        self.transition_matrix[j][i] = rng.uniform(0.01, 0.2)

        # Normalize rows to sum to 1, representing probability distributions
        row_sums = self.transition_matrix.sum(axis=1) - 1  # Exclude self-transition in normalization
        self.transition_matrix[np.arange(self.n_diseases), np.arange(self.n_diseases)] = 1 - row_sums

    def compute_stationary_distribution(self):
        # Compute the stationary distribution for the Markov chain
        self.communicating_classes = get_communicating_classes(self.transition_matrix)
        self.stationary_distribution = calculate_stationary_distribution(self.transition_matrix, self.communicating_classes)

    def generate_diseases(self, rng):
        self.diseases = {}  # Initialize the dictionary
        all_treatments = set(range(self.n_treatments))  # Set of all treatments

        for i in range(self.n_diseases):
            num_symptoms_for_disease = rng.randint(1, max(2, self.n_symptoms // 2))
            symptoms_for_disease = rng.choice(self.n_symptoms, size=num_symptoms_for_disease, replace=False)

            num_effective_treatments = rng.randint(1, max(2, self.n_treatments // 2))
            effective_treatments = rng.choice(self.n_treatments, size=num_effective_treatments, replace=False)
            all_treatments -= set(effective_treatments)  # Remove used treatments from the set

            means = rng.uniform(0.3, 0.7, size=num_symptoms_for_disease)
            std_devs = rng.uniform(0.05, 0.15, size=num_symptoms_for_disease)
            symptom_distributions = list(zip(means, std_devs))

            treatment_to_remission_probs = rng.uniform(0.1, 0.7, size=num_effective_treatments)

            base_cost = rng.uniform(*self.disease_cost_range)

            self.diseases[f"Disease_{i}"] = {
                'symptoms': symptoms_for_disease,
                'treatments': effective_treatments,
                'symptom_distributions': symptom_distributions,
                'remission_probs': dict(zip(effective_treatments, treatment_to_remission_probs)),
                'base_cost': base_cost
            }

        # Sprinkle unused treatments among the diseases
        for treatment in all_treatments:
            random_disease = f"Disease_{rng.randint(0, self.n_diseases)}"
            self.diseases[random_disease]['treatments'] = np.append(self.diseases[random_disease]['treatments'], treatment)

            # Assign a random remission probability to this new treatment
            self.diseases[random_disease]['remission_probs'][treatment] = rng.uniform(0.1, 0.7)


    def _combine(self, observation, action):
        """Combine the observation and action into a single vector
        action vector is one-hot encoded"""
        action_one_hot = np.zeros(self.n_treatments, dtype=np.float32)
        action_one_hot[int(action)] = 1.0
        return np.concatenate([observation, action_one_hot])
    
    def handle_remission(self, action):
        # Update remission-related states and compute reward
        self.current_disease = "Remission"
        self.reward_components['remission'] += self.remission_reward
        self.time_to_remission = self.visit_number if self.time_to_remission is None else self.time_to_remission
        reward = self.remission_reward - self.reward_components['treatment_based']
        self.current_symptoms = np.zeros(self.n_symptoms)  # Reset symptoms
        return self._combine(self.current_symptoms, action), reward, True, {
            "treatment": action, 
            "disease_pre_treatment": self.current_disease, 
            "remission": True
        }
    
    def apply_treatment_and_transition_disease(self, action, treatment):
        treatment_modifiers = treatment["transition_modifiers"]
        modified_transitions = self.transition_matrix[self.current_disease_index] * treatment_modifiers
        modified_transitions /= modified_transitions.sum()
        new_disease_index = np.random.choice(self.n_diseases, p=modified_transitions)
        self.current_disease = f"Disease_{new_disease_index}"
        self.current_disease_index = new_disease_index

        disease_cost = 0
        symptom_cost = 0

        # Deduct the base reward for the current disease from the total reward
        if self.use_disease_rewards:
            disease_cost = self.diseases[self.current_disease]['base_cost']
            self.reward_components['state_based'] -= disease_cost

        # Fluctuate symptoms based on disease distributions and then adjust them based on treatment effects
        self.current_symptoms = self.sample_symptoms()
        if self.treatment_affect_observation:
            for symptom, change in treatment['affected_symptoms'].items():
                self.current_symptoms[symptom] += change
            self.current_symptoms = np.clip(self.current_symptoms, 0, 1)

        if self.use_symptom_rewards:
            symptom_cost = (self.current_symptoms.sum() / self.n_symptoms) * (self.remission_reward / self.max_visits)
            self.reward_components['symptom_based'] -= symptom_cost

        return new_disease_index, disease_cost, symptom_cost

    def step(self, action):
        self.visit_number += 1
        reward = 0 # Reset step reward

        # Handle treatment cost
        treatment = self.treatments[f"Treatment_{action}"]
        treatment_cost = treatment['base_cost']
        self.reward_components['treatment_based'] -= treatment_cost
        reward -= treatment_cost
    
        # Handle potential remission
        if np.random.rand() < self.diseases[self.current_disease]['remission_probs'].get(action, 0):
            return self.handle_remission(action)

        # Handle disease transition and symptom changes
        new_disease_index, disease_cost, symptom_cost = self.apply_treatment_and_tranisition_disease(action, treatment)
        reward -= (disease_cost + symptom_cost)

        # Visits cutoff check
        terminated = self.visit_number == self.max_visits

        # Combine observation and action, then return the step information
        return self._combine(self.current_symptoms, action), reward, terminated, {
            "treatment": action, 
            "disease_pre_treatment": self.current_disease, 
            "remission": False
        }

    def sample_symptoms(self):
        # Baseline symptoms for a healthy individual
        baseline_symptom_level = np.random.uniform(0, 0.05, self.n_symptoms)

        if self.current_disease == "Remission":
            return baseline_symptom_level  # Mimic healthy individual with baseline noise

        symptom_values = baseline_symptom_level.copy()  # Start with baseline symptoms
        
        symptoms_for_disease = self.diseases[self.current_disease]['symptoms']
        symptom_distributions = self.diseases[self.current_disease]['symptom_distributions']
        
        for symptom, (mean, std_dev) in zip(symptoms_for_disease, symptom_distributions):
            sampled_value = np.random.normal(mean, std_dev)
            symptom_values[symptom] += sampled_value  # Add disease symptom on top of baseline
        symptom_values = np.clip(symptom_values, 0, 1)  # Ensure values are within valid range

        return symptom_values
    
    def generate_treatments(self, rng):
        treatments = {}
        for i in range(self.n_treatments):
            # Each treatment can have a cost between the configurable range
            base_cost = rng.uniform(*self.treatment_cost_range)  
            
            affected_symptoms_count = rng.randint(1, max(2, self.n_symptoms))
            affected_symptoms = rng.choice(self.n_symptoms, size=affected_symptoms_count, replace=False)
            
            # Change in symptom severity due to treatment is generated within the configurable range
            symptom_changes = {symptom: rng.uniform(*self.symptom_modulation_range) for symptom in affected_symptoms}
            
            treatments[f"Treatment_{i}"] = {
                'base_cost': base_cost,
                'affected_symptoms': symptom_changes
            }

            # Generate treatment-specific transition modifiers for each disease transition
            transition_modifiers = rng.uniform(0.5, 1.5, size=self.n_diseases)
            treatments[f"Treatment_{i}"]["transition_modifiers"] = transition_modifiers
        return treatments

    def reset(self, *, seed=None, options=None):
        self.current_disease = np.random.choice(self.disease_list, p=self.stationary_distribution)
        self.current_disease_index = self.disease_list.index(self.current_disease)
        self.current_symptoms = self.sample_symptoms()  # Initialize symptoms based on the current disease
        self.visit_number=0

        # For tracking reward components and time to remission
        self.reward_components = {
        'remission': 0,
        'state_based': 0,
        'treatment_based': 0,
        'symptom_based': 0
        }
        self.time_to_remission = -1 # -1 indicates no remission achieved
        
        #print(f"[DEBUG] Resetting environment. Starting disease: {self.current_disease}, Initial symptoms: {self.current_symptoms}")
        return self._combine(self.current_symptoms, -1)
        

    def render(self, mode='human'):
        # Simple visualization for now
        print(f"Current Disease: {self.current_disease}")
        print(f"Current Symptoms: {self.current_symptoms}")
        print("\n")

    def get_metrics(self):
        return self.reward_components, self.time_to_remission