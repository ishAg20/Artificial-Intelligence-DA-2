import numpy as np
#Ishika Agarwal 22BCE3179
# Define conditional probabilities
P_A = {'yes': 0.8, 'no': 0.2}
P_C = {'yes': 0.5, 'no': 0.5}
P_G_given_A_C = {
    ('yes', 'yes'): {'Good': 0.9, 'OK': 0.1},
    ('yes', 'no'): {'Good': 0.7, 'OK': 0.3},
    ('no', 'yes'): {'Good': 0.6, 'OK': 0.4},
    ('no', 'no'): {'Good': 0.3, 'OK': 0.7},
}
P_J_given_G = {'Good': {'yes': 0.8, 'no': 0.2}, 'OK': {'yes': 0.2, 'no': 0.8}}
P_S_given_G = {'Good': {'yes': 0.7, 'no': 0.3}, 'OK': {'yes': 0.3, 'no': 0.7}}

# Monte Carlo simulation
def monte_carlo_simulation(num_samples=10000):
    count_target = 0
    count_evidence = 0
    for _ in range(num_samples):
        # Sample A and C
        A = 'yes' if np.random.rand() < P_A['yes'] else 'no'
        C = 'yes' if np.random.rand() < P_C['yes'] else 'no'
        
        # Sample G given A and C
        G_probs = P_G_given_A_C[(A, C)]
        G = 'Good' if np.random.rand() < G_probs['Good'] else 'OK'
        
        # Sample J given G
        J_probs = P_J_given_G[G]
        J = 'yes' if np.random.rand() < J_probs['yes'] else 'no'
        
        # Evidence check
        if A == 'yes' and C == 'yes':  # Evidence: A = yes, C = yes
            count_evidence += 1
            if J == 'yes':  # Target: J = yes
                count_target += 1
    
    # Calculate conditional probability
    if count_evidence == 0:
        return 0  # Avoid division by zero
    return count_target / count_evidence

# Run simulation
estimated_probability = monte_carlo_simulation()
print(f"Estimated P(J=yes | A=yes, C=yes): {estimated_probability}")


