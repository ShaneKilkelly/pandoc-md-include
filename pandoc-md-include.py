#!/usr/bin/env python

import sys
import os
import re
import json
import subprocess

Matcher = re.compile('<!-- %include\("(.*)"\) -->')
this_script = os.path.abspath(sys.argv[0])

def main():
    input_str = sys.stdin.read()
    input_data = json.loads(input_str)
    output_blocks = []
    for block in input_data['blocks']:
        key = block['t']
        value = block['c']
        if key == 'RawBlock' and value[0] == u'html':
            m = Matcher.match(value[1])
            if m is not None:
                source_file = m.group(1)
                output_text = subprocess.check_output([
                    'pandoc',
                    source_file,
                    '--filter', this_script,
                    '-t', 'json'
                ])
                data = json.loads(output_text)
                for sub_block in data['blocks']:
                    output_blocks.append(sub_block)
            else:
                output_blocks.append(block)
        else:
            output_blocks.append(block)
    input_data['blocks'] = output_blocks
    print(json.dumps(input_data))


if __name__ == "__main__":
    main()
