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

The package exports a single function `rmsfact()` which returns a single randomly-chosen "fact".

```python
import rmsfact

rmsfact.rmsfact()
```
