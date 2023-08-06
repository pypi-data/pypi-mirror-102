# rmsfact

A port of the R package [`rmsfact`](https://cran.r-project.org/package=rmsfact) by Dirk Edelbuettel.

Display a randomly selected quote about Richard M. Stallman based on the collection in the 'GNU
Octave' function 'fact()' which was aggregated by Jordi Gutiérrez Hermoso based on the (now defunct)
site stallmanfacts.com (which is accessible only via <http://archive.org>).

# Usage

The package contains a single class, `RMSFact()` which provides a single method `rmsfact()` which
takes no arguments and prints a randomly-selected "fact" to the console.

```python
import rmsfact

factory = rmsfact.RMSFact()

factory.rmsfact()
```
