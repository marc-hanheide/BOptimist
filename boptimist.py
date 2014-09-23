#!/usr/bin/env python

import argparse
import sys
from subprocess import check_call, STDOUT, CalledProcessError
from time import sleep

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='optimistically retry a Bash command a given number of times',
        epilog='(c) Marc Hanheide 2014, see https://github.com/marc-hanheide/BOptimist'
    )
    parser.add_argument(
        '--retry',
        default=5,
        type=int,
        help='Number of retries. Default: 5')

    parser.add_argument(
        '--sleep',
        default=1,
        type=int,
        help='Number of seconds to sleep between tries. Default: 1')

    parser.add_argument(
        '--progressive',
        default=False,
        action='store_true',
        help='Should the sleep time increase linearly with every try? Default: False')

    parser.add_argument(
        '--shell',
        default=False,
        action='store_true',
        help='Should the command run in a new shell (allows for complex shell commands)? Default: False')

    parser.add_argument(
        'args',
        default=[],
        nargs='+',
        help='The arguments to call')

    opts = parser.parse_args()


    for t in range(0, opts.retry):
        sys.stderr.write('running for the ' + str(t) + ' time...\n')
        try:
            check_call(
                opts.args,
                stdin=None,
                stderr=STDOUT,
                shell=opts.shell,
                universal_newlines=False
            )
            sys.stderr.write(
                'process succeeded\n')
            break
        except CalledProcessError, e:
            if (t < opts.retry - 1):
                sys.stderr.write(
                    'process failed. return code: ' + str(e.returncode) + '. Let try again after some sleep.\n')
                if opts.progressive:
                    sleep(opts.sleep * (t+1))
                else:
                    sleep(opts.sleep)
            else:
                sys.stderr.write(
                    'process finally failed. return code: ' + str(e.returncode) + '\n')
