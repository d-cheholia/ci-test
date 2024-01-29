#!/usr/bin/env python3
from universum.configuration_support import Configuration, Step

configs = Configuration([Step(name='Print Hello', command=['echo', 'hello']),
                         Step(name='Clang format', command=['bash', '-c', 'clang-format --dry-run --Werror ./src/*.cpp'])])

if __name__ == '__main__':
    print(configs.dump())