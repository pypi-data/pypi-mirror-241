[![Generic badge](https://img.shields.io/badge/Licence-MIT-blue.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Maintained-yes-green.svg)](https://shields.io/)
[![Generic badge](https://img.shields.io/badge/Python-3.10-yellow.svg)](https://shields.io/)


## Package
Package for getting and analyzing tending Google searches

## Usage
```python
from google_trendy import *

tracker = GoogleTrends()
tracker.get_trends(10)
for trend in tracker.trends:
    print(trend.title)


# Example Output
National Collegiate Athletics Association, Cross country running, University of North Texas, North Texas Mean Green
Cross country running, National Collegiate Athletics Association, NCAA Division III, Union College, Union Garnet Chargers, Liberty League
Slippery Rock University, Cross country running, National Collegiate Athletics Association, NCAA Division II
Cross country running, National Collegiate Athletics Association, Big Ten Conference, Illinois Fighting Illini
Cross country running, National Collegiate Athletics Association, Track and field
Cross country running, NCAA Division III, National Collegiate Athletics Association, Bridgewater State University
National Collegiate Athletics Association, Cross country running, University of Pennsylvania, Penn Quakers football, Student athlete, Penn State Nittany Lions Women's Cross Country, Student
Cross country running, National Collegiate Athletics Association, NCAA Division I
Wrexham A.F.C., Accrington Stanley F.C., EFL League Two
Cross country running, Dominica, Championship, Primary school

```
