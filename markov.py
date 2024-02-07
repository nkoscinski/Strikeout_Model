import pandas as pd


def calculate_total_probability(transition_matrix: pd.DataFrame) -> float:
    transition_matrix = transition_matrix[["Strike", "Ball", "BIP"]]

    # Normalize the transition matrix
    transition_matrix = transition_matrix.div(transition_matrix.sum(axis=1), axis=0)

    # Define the sequences
    sequences = [
        ["0_0", "0_1", "0_2"],
        ["0_0", "1_0", "1_1", "1_2"],
        ["0_0", "1_0", "2_0", "2_1", "2_2"],
        ["0_0", "1_0", "2_0", "3_0", "3_1", "3_2"],
    ]

    # Initialize the total probability
    total_probability = 0

    # Iterate over the sequences
    for sequence in sequences:
        # Initialize the sequence probability
        sequence_probability = 1
        # Iterate over the states in the sequence
        for i in range(len(sequence) - 1):
            # Multiply the sequence probability by the transition probability
            sequence_probability *= transition_matrix.loc[sequence[i], "Strike"]
        # Add the sequence probability to the total probability
        total_probability += sequence_probability

    return total_probability
