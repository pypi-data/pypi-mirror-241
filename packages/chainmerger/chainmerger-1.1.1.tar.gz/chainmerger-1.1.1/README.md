
[![PyPI - Version](https://img.shields.io/pypi/v/chainmerger.svg)](https://pypi.org/project/chainmerger/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# chainmerger
merge chainalysis's exported transaction csv files into one xlsx file with separate sheets per exchange

# installation
```
pip install chainmerger
```

# usage
```
chainmerger -i <input directory> -o <output directory>
```

### default directories

If input dir is not specified:
```
~/chainmerger_Input
```
If no output dir is specified:
```
~/chainmerger_Input/chainmerger_Output
```
Else:
```
<input dir> / <output dir>
```

# example
![example](/example.png)