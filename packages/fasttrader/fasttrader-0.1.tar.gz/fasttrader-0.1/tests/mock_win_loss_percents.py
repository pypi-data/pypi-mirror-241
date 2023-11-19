import numpy as np


def mock_win_loss_percents(array_length=100):
    """
    Mock the win loss percents numpy array.

    Args:
        array_length (int): The length of the numpy array to mock.

    Returns:
        np.array: A numpy array of win loss percents.
    """

    mock = np.random.random(array_length)
    for i in range(len(mock)):
        if mock[i] > 0.1:
            mock[i] = 0
        elif mock[i] < -0.1:
            mock[i] = 0


    return mock


print(mock_win_loss_percents())

