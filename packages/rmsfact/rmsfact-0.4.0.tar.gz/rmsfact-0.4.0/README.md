# rmsfact

A port of the R package [`rmsfact`](https://cran.r-project.org/package=rmsfact) by Dirk Edelbuettel.

Display a randomly selected quote about Richard M. Stallman based on the collection in the 'GNU
Octave' function 'fact()' which was aggregated by Jordi Gutiérrez Hermoso based on the (now defunct)
site stallmanfacts.com (which is accessible only via <http://archive.org>).


# Installation

``` python
pip install rmsfact
```


# Usage

The package exports a single function `rmsfact()` which returns a single randomly-chosen "fact" as
a `str`.

```python
import rmsfact

rmsfact.rmsfact()
```

You can also run `python -m rmsfact` from a shell.


# Building from source

In the event you want to build the package from source, clone the repository...

```
git clone https://github.com/lewinfox/rmsfact.git
```

... `cd` into the project directory...

```
cd rmsfact
```

...and install with `make`

```
make install
```

This builds the package and then runs `python -m pip install .`


# Making changes

To add a new fact you can edit `rmsfact/data/rmsfact.txt`.

```
echo "A new fact" >> rmsfact/data/rmsfact.txt
```

The `Makefile` provides a couple of useful targets, one of which is `make build_binary_data` which
executes the script `rmsfact/data/build_rms_fact.py` to convert `rmsfact/data/rmsfact.txt` into a
`.dat` file using `pickle`. This `.dat` file is then read when the package is loaded.

Executing `make build` will rebuild the data file and produce the source and binary packages under
a `dist/` directory. You may need to `python -m pip install build` first.

```
make build
```

## Other makefile targets

* `make install_dev`: Install with `pip -e`
