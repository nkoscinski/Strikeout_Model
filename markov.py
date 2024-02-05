import numpy as np
from hitters import transition_matrix  # Assuming transition_matrix is your DataFrame

# Define the initial state
initial_state = "0_0"

# Define the intermediate states (2-strike counts)
intermediate_states = ["0_2", "1_2", "2_2", "3_2"]

# Define the target state
target_state = "Strike"

# Initialize the probabilities
prob_intermediate = 0
prob_target = 0

# Normalize each row to get the transition probabilities
transition_probs = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)

# Convert the DataFrame to a numpy array
transition_matrix = transition_probs.to_numpy()

# Transpose the transition matrix before matrix multiplication
transition_matrix_transposed = transition_matrix.T

# Use an iterative method to approximate the matrix power for non-square matrices
raised_matrix = np.eye(
    transition_matrix.shape[1]
)  # Identity matrix with the correct dimensions
for _ in range(10):  # Adjust the number of iterations as needed
    raised_matrix = np.dot(raised_matrix, transition_matrix)

# Add the probabilities of reaching the intermediate states from the initial state to the total probability
for intermediate_state in intermediate_states:
    if (
        intermediate_state in transition_probs.index
        and initial_state in transition_probs.columns
    ):
        prob_intermediate += raised_matrix[
            transition_probs.columns.get_loc(initial_state),
            transition_probs.index.get_loc(intermediate_state),
        ]

# Add the probabilities of reaching the target state from each intermediate state to the total probability
for intermediate_state in intermediate_states:
    if (
        target_state in transition_probs.index
        and intermediate_state in transition_probs.columns
    ):
        prob_target += raised_matrix[
            transition_probs.columns.get_loc(intermediate_state),
            transition_probs.index.get_loc(target_state),
        ]

# Calculate the final probability
final_prob = prob_intermediate * prob_target

# Print the probability
print(
    f"Probability of reaching a 2-strike count and then a strike being called: {final_prob}"
)
