import unittest
import numpy as np
import os
from Lab9 import read_values_from_file, read_oscillatory_wave_data, read_standing_wave_data, read_sound_data

# Test case for read_values_from_file() function
def test_read_values_from_file():
    filename = "test_values.txt"
    with open(filename, 'w') as file:
        file.write("1.5\n2.5\n3.5\n4.5\n5.5")
    
    expected_array = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    result = read_values_from_file(filename)
    np.testing.assert_array_equal(result, expected_array)
    os.remove(filename)

# Test case for read_oscillatory_wave_data() function
def test_read_oscillatory_wave_data():
    filename = "test_oscillatory_wave.csv"
    with open(filename, 'w') as file:
        file.write("1,2\n3,4\n5,6\n7,8\n9,10")
    
    expected_data = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
    data, mean_amplitude, max_amplitude = read_oscillatory_wave_data(filename)
    np.testing.assert_array_equal(data, expected_data)
    assert mean_amplitude == np.mean(expected_data[:, 1])
    assert max_amplitude == np.max(expected_data[:, 1])
    os.remove(filename)

# Test case for read_standing_wave_data() function
def test_read_standing_wave_data():
    filename = "test_standing_wave.csv"
    with open(filename, 'w') as file:
        file.write("1,4\n2,9\n3,16\n4,25\n5,36")
    
    expected_data = np.array([[1, 4], [2, 9], [3, 16], [4, 25], [5, 36]])
    data, wave_speeds = read_standing_wave_data(filename)
    np.testing.assert_array_equal(data, expected_data)
    np.testing.assert_array_almost_equal(wave_speeds, np.sqrt(expected_data[:, 1] / expected_data[:, 0]))
    os.remove(filename)
    
# Test case for read_sound_data() function
def test_read_sound_data():
    filename = "test_sound_data.csv"
    with open(filename, "w") as file:
        file.write("Length (m),Trial 1,Trial 2,Trial 3\n")
        file.write("0.5,10,20,30\n")
        file.write("1.0,5,15,25\n")

    # Expected raw data
    expected_data = np.array(
        [
            [0.5, 10.0, 20.0, 30.0],
            [1.0, 5.0, 15.0, 25.0],
        ]
    )

    data, stats = read_sound_data(filename)

    # Check that the raw data matches
    np.testing.assert_array_equal(data, expected_data)

    # Manually compute expected statistics
    lengths = expected_data[:, 0]
    trials = expected_data[:, 1:]

    inv_length = 1.0 / lengths
    averages = np.mean(trials, axis=1)
    mean_dev = np.mean(np.abs(trials - averages[:, np.newaxis]), axis=1)
    st_dev = np.std(trials, axis=1)
    max_vals = np.max(trials, axis=1)
    min_vals = np.min(trials, axis=1)
    delta = max_vals - min_vals
    count = np.full_like(averages, trials.shape[1])

    expected_stats = np.column_stack(
        (inv_length, averages, mean_dev, st_dev, max_vals, min_vals, delta, count)
    )

    # Allow for small floating-point differences
    np.testing.assert_array_almost_equal(stats, expected_stats)

    os.remove(filename)


if __name__ == '__main__':
    unittest.main()
