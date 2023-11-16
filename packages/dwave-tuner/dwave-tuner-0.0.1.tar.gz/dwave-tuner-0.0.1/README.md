# D-Wave Tuner

`dwave-tuner` simplifies the process of tuning annealing parameters, allowing
you to concentrate on your model and specific problem. Simply specify the
number of embeddings, chain strengths, and annealing times, and watch as
dwave-tuner tailors the tuning experience to your needs.

## Features
- **Effortless parameter tuning**: Grid scan chain strengths and annealing
  times with a given number of embeddings.
- **Caching for efficiency**: D-Wave responses are cached by default, enhancing 
  performance by utilizing cached results unless you modify the scan or alter
  the parameters.
- **User-Friendly**: Minimal configuration; just specify your preferences in a
  dictionary, and let `dwave-tuner` handle the details.
- **Basic Benchmarking**: Includes rudimentary benchmarking functionality.
  - **Visualization**: Plot success probabilities vs. chain strength or
    annealing time to gain insights into tuning results.
  - **Model Comparison**: Compare success probabilities of optimal D-Wave
    parameters for a set of models, such as those with increasing model size.

## Example Usage
```python
import dwavetuner
from dwavetuner import analysis
```

Specify the scan parameters:
```python
parameters = {
    'num_embeddings': 10,
    'num_chain_strengths': 1,
    'num_reads': 1000,
    'num_reps': 1
}
```

Create a `Scanner` to schedule the `Job`s:
```python
scanner = dwavetuner.Scanner(my_model.bqm, label='my_model', **parameters)
```

Perform a grid scan and plot the tuning results:
```python
scanner.grid_scan()
analysis.ScanPlot(scanner)
```

Alternatively, use these self-explanatory `parameters`:
```python
# Scan chain strengths
parameters = {
    'num_embeddings': 10,
    'chain_strengths_start': 0.24,
    'chain_strengths_end': 0.44,
    'num_chain_strengths': 10,
    'num_reads': 100,
    'num_reps': 1
}

# Scan annealing times
parameters = {
    'chain_strength': 0.28,
    'num_annealing_times': 10,
    'num_reads': 100,
    'num_reps': 5
}
```

## Author

Orkun Şensebat

git@senseb.at