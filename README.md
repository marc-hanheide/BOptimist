BOtimist
========

Optimistic Bash executor

```
usage: boptimist.py [-h] [--retry RETRY] [--sleep SLEEP] [--progressive]
                    [--shell]
                    args [args ...]

optimistically retry a Bash command a given number of times

positional arguments:
  args           The arguments to call

optional arguments:
  -h, --help     show this help message and exit
  --retry RETRY  Number of retries. Default: 5
  --sleep SLEEP  Number of seconds to sleep between tries. Default: 1
  --progressive  Should the sleep time increase linearly with every try?
                 Default: False
  --shell        Should the command run in a new shell (allows for complex
                 shell commands)? Default: False

(c) Marc Hanheide 2014, see https://github.com/marc-hanheide/BOptimist
```