# Iterated-sums signature in Rust

This is an implementation of the one-dimensional iterated-sums signature in Rust,
with Python 3 bindings.

## Installation
### From PyPI
Normally, this package can be installed by running
```bash
pip3 install o3iss
```

### From source
Curretly we provide wheels for Linux, macOS and 64-bit Windows.
If your system is not included in any of these targets, you will have to compile the package yourself.
This will require you to have a Rust compiler, which can be obtained from [https://www.rust-lang.org/tools/install].

Start by cloning this repository by running
```bash
git clone https://github.com/ntapiam/o3iss.git
```

Then, enter the directory and run
```bash
python3 setup.py install
```
This should compile and install the package on your system.

## Usage
This implementation offers only a single function: `iss.compute` with signature `(np.ndarray, int) -> np.ndarray`
where both the input and ouput arrays are one-dimensional.

In `v0.1.2`, we introduced partial support for the `sklearn` framework.
Example (assuming that `sktime` is present):
```python3
from iss import IssClassifier
from sktime.datasets import load_gunpoint
from sktime.utils.data_processing import from_nested_to_2d_array


Xtrain, ytrain = load_gunpoint(split="train", return_X_y=True)
Xtest, ytest = load_gunpoint(split="test", return_X_y=True)
Xtrain, Xtest = (
    from_nested_to_2d_array(Xtrain).to_numpy(),
    from_nested_to_2d_array(Xtest).to_numpy(),
)
ytrain, ytest = ytrain.astype(int), ytest.astype(int)

clf = IssClassifier(level=3, n_jobs=7)
clf.fit(Xtrain, ytrain)
print(clf.score(Xtest, ytest))
>> 0.9133333333333333
```

# TO DO
- [ ] Multidimensional signature
- [ ] Proper `sklearn` integration
- [x] Produce a proper Python 3 package
