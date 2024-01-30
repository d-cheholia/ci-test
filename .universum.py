#!/usr/bin/env python3
from universum.configuration_support import Configuration, Step
from universum.configuration_support import Configuration, Step

configs = Configuration([Step(name='Print Hello', command=['echo', 'hello'])])

configs = Configuration([Step(name="clang-format", code_report=True, command=[
    "python3", "-m", "universum.analyzers.clang_format", "--executable", "clang-format", "--files", "*.cpp",
    "--result-file", "${CODE_REPORT_FILE}"
],artifacts='code_report_results/clang-format.json')])

if __name__ == '__main__':
    print(configs.dump())