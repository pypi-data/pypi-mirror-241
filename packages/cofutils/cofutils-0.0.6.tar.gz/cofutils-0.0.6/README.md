# Introduction for Cof utils
There're several useful tools for experiments, such as cofrun, coflogger, and logspy.

## Install
#### By Pypi
`pip install cofutils`

#### By Source
```
git clone https://gitee.com/haiqwa/cofutils.git
pip install .
```
## Usage

### Cof Memory Report
Print GPU memory states by pytorch cuda API
* `MA`: memory current allocated
* `MM`: max memory allocated
* `MR`: memory reserved by pytorch

```python
from cofutils import cofmem

cofmem("before xxx")
# ...
cofmem("after xxx")
```

```bash
(deepspeed) haiqwa@gpu9:~/documents/cofutils$ python ~/test.py 
[2023-11-11 15:32:46.873]  [Cof INFO]: before xxx GPU Memory Report (GB): MA = 0.00 | MM = 0.00 | MR = 0.00
[2023-11-11 15:32:46.873]  [Cof INFO]: after xxx GPU Memory Report (GB): MA = 0.00 | MM = 0.00 | MR = 0.00
```
### Cof Logger
Cof logger can print user message according to print-level.
In *.py:
```
from cofutils import coflogger
coflogger.debug("this is debug")
coflogger.info("this is info")
coflogger.warn("this is warn")
coflogger.error("this is error")
```
Print-level is determined by environment variable `COF_DEBUG`:
```
COF_DEBUG=WARN python main.py
```
The default print-level is `INFO`. By the way, only the node of 'rank=0' can output log in distributed environment

### Cof CSV
Dump data into csv format.

* Get a unique csv writer by calling cofcsv
* Write data in dict type. You can append data at anywhere and anytime
* Save data as `[name].csv` under the `root_dir`. After that cofcsv will clear data in default
```python
from cofutils import cofcsv

data = {'a':1, 'b':2, 'c':3}
test_csv = cofcsv('test')
test_csv.write(data)
data = {'a':4, 'b':5, 'c':6}
test_csv.write(data)
cofcsv.save(root_dir='csv_output')
```

### Cof Timer
Cof timer is similar to the `Timer` in `Megatron-LM`

It support two log modes:
* Organize the result into a string and output it into `STDOUT` which is easy to view for users 
* Directly return the result time table

If you call `.log` to output time, then the timer will reset automatically 
```python
from cofutils import coftimer
from cofutils import coflogger
import time
test_1 = coftimer('test1')
test_2 = coftimer('test2')

for _ in range(3):
    test_1.start()
    time.sleep(1)
    test_1.stop()

coftimer.log(normalizer=3, timedict=False)


for _ in range(3):
    test_2.start()
    time.sleep(1)
    test_2.stop()

time_dict = coftimer.log(normalizer=3, timedict=True)
coflogger.info(time_dict)
```

```bash
(deepspeed) haiqwa@gpu9:~/documents/cofutils$ python ~/test.py 
[2023-11-11 16:15:43.942]  [Cof INFO]: time (ms) | test1: 1001.20 | test2: 0.00
NoneType: None
[2023-11-11 16:15:46.946]  [Cof INFO]: {'test1': 0.0, 'test2': 1001.2083053588867}
```

### Cofrun is all you need!
User can easily launch distributed task by `cofrun`. What users need to do is to provide a template bash file and configuration json file.

You can see the examples in `example/`

```
(deepspeed) haiqwa@gpu9:~/documents/cofutils/example$ cofrun -h
usage: cofrun [-h] [--file FILE] [--input INPUT] [--template TEMPLATE] [--output OUTPUT] [--test] [--list] [--range RANGE]

optional arguments:
  -h, --help            show this help message and exit
  --file FILE, -f FILE  config file path, default is ./config-template.json
  --input INPUT, -i INPUT
                        run experiments in batch mode. all config files are placed in input directory
  --template TEMPLATE, -T TEMPLATE
                        provide the path of template .sh file
  --output OUTPUT, -o OUTPUT
                        write execution output to specific path
  --test, -t            use cof run in test mode -> just generate bash script
  --list, -l            list id of all input files, only available when input dir is provided
  --range RANGE, -r RANGE
                        support 3 formats: [int | int,int,int... | int-int], and int value must be > 0
```

Let's run the example:

```
cofrun -f demo_config.json -T demo_template.sh
```
And the execution history of cofrun will be written into `history.cof`
