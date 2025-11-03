# Programming in Science - Lab 9

This template repository is the starter project for **Programming in Science Lab 9**. Written in Python and tested with Pytest.

### Question(s)

1. **(20%)** Read values from a file:
   
   - Write a function `read_values_from_file(filename)` that reads numerical values from a text file and stores them in a NumPy array.
   
   #### Example:
   ```python
   read_values_from_file("values.txt")  # Returns a NumPy array of values
   ```
   ✅ **Hints:** Ensure the file contains one numerical value per line.

2. **(20%)** Read Oscillatory Wave Data:
   
   - Write a function `read_oscillatory_wave_data(filename)` that reads a file containing wave data with length and amplitude values. Compute the mean and maximum amplitude.
   
   #### Example:
   ```python
   read_oscillatory_wave_data("wave_data.csv")
   ```
   ✅ **Hints:** Use NumPy to read the CSV and compute statistics.

3. **(20%)** Read Standing Wave Data:
   
   - Write a function `read_standing_wave_data(filename)` that reads a file containing standing wave data with length and tension values. Compute the wave speed using:
   
   Wave speed is calculated using the formula:

   **v = sqrt(T / μ)**

   where **T** is tension and **μ** (mass per unit length) is assumed to be 1.
   
   where \( \mu \) (mass per unit length) is assumed to be 1.
   
   #### Example:
   ```python
   read_standing_wave_data("standing_wave.csv")
   ```
   ✅ **Hints:** Use NumPy to read the CSV and compute the wave speed.

4. **(40%)** Read Sound Data & Compute Detailed Statistics:

   - Write a function `read_sound_data(filename)` that reads a CSV file containing sound measurements.
   - The file (e.g., `sound_data.csv`) has:
     - A header row
     - Column 0: `Length (m)`
     - Columns 1..N: trial measurements for that length (e.g., frequencies)

   Your function must:

   1. Read all numeric data (skip the header) into a NumPy array called `data`.
   2. For each row (each length), compute the following **across the trial columns**:

      - **1/L** – reciprocal of the length  
      - **Average** – mean of the trial values  
      - **Mean Dev** – mean **absolute** deviation from the average  
      - **St Dev** – standard deviation of the trial values (use `np.std`)  
      - **Max** – maximum trial value  
      - **Min** – minimum trial value  
      - **Delta** – `Max - Min`  
      - **Count** – number of trial measurements in that row  

   3. Store these eight quantities in a second NumPy array called `stats`, where each row corresponds to one length and the columns are in this exact order:

      `1/L, Average, Mean Dev, St Dev, Max, Min, Delta, Count`

   4. Return both arrays:

   ```python
   data, stats = read_sound_data("sound_data.csv")
   ```

   ✅ **Hints:**

   Use np.loadtxt(..., delimiter=",", skiprows=1) to read the CSV while ignoring the header.

   Use slicing to separate the length column from the trial columns:

   lengths = data[:, 0]

   trials = data[:, 1:]

   Functions that will help:

   np.mean, np.abs, np.std, np.max, np.min, np.column_stack.  

### Run Command

To run the tests, use the following command:

```
pytest
```

