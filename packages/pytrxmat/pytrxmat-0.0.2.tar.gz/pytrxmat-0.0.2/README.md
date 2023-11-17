# pytrxmat

## Overview

pytrxmat is a Python package designed to facilitate the access and manipulation of data stored in trx.mat files commonly used in behavior screens. These files contain raw tracking data and postprocessing results for multiple larvae in experimental studies.
Installation

```bash
pip install pytrxmat
```

## Usage

### TRX Class

The main component of pytrxmat is the TRX class, which provides a convenient interface to interact with trx.mat files.

### Initialization

```python
from pytrxmat.trx import TRX

# Instantiate the TRX class with the path to your 'trx.mat' file
trx = TRX('path/to/trx.mat')
```

### Accessing Fields

The TRX class allows you to retrieve various fields from the trx.mat file, including scalar, string, time series, and composite array fields.

### Scalar Fields

```python
# Get a scalar field (e.g., 'numero_larva_num')
scalar_data = trx.get('numero_larva_num')
```

### Time Series Fields

```python
# Get a time series field (e.g., 'x_tail')
time_series_data = trx.get('x_tail')
```

### Composite Array Fields

```python
# Get a composite array field (e.g., 'duration_large')
composite_array_data = trx.get_composite_array('duration_large')
```

### String Fields

```python
# Get string fields (e.g., 'neuron' and 'protocol')
string_data = trx.get_string(['neuron', 'protocol'])
```

## File Format

The trx.mat file format is a standardized way of storing experimental data in the Decision and Bayesian Computation lab at the Pasteur Institute. The file contains multiple fields, each corresponding to different aspects of the larvae's behavior. The fields include univariate and multivariate time series, classification labels and probabilities, behavior summaries, and metadata such as full paths, IDs, and neuron information.

## Contribution

Contributions to this project are welcome. Feel free to open issues for bug reports or feature requests. If you'd like to contribute code, please submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.