# candypen

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT) 

A tiny tool module for multi-process programs.
## Install

candypen could be easily installed using pip:

```bash
$ pip install candypen
```

## Example

```python
import requests
from candypen import concurrent

# Define a source list for task function to parse.
def get_source():
    """Return a url list."""
    return ['http://www.baidu.com' for i in range(500)]

# Define the task function and add a thread_func decorator
# The thread_func decorator needs a source list, and other options (num_workers, has_result ...) as arguments
@concurrent.thread_func(source=get_source(), num_workers=100, has_result=True)
def my_task(task_source):
    """A customized task function.
    Process the task_source and return the processed results.

    Arguments
    :param task_source: the elem in the source list, which is a url here.
    :rtype: (int) A http status code.
    """
    url = task_source
    res = requests.get(url, timeout=5)
    return res.status_code

# Execute the task function.
results = my_task()
print(results)
```

Results of the example is as below:

```bash
[Info] 500 tasks in total.
[ ✔ ] 100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 500/500 [eta-0:00:00, 0.9s, 542.9it/s]
[200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, 200, ..., 200, 200, 200, 200]
```



## License

Licensed under the [MIT License](https://github.com/Tishacy/QSpider/blob/master/LICENSE).