#!/usr/bin/env python3

__all__ = ['main']

import sys

def main(argv=None):

    import argparse
    from . import image_to_text
    from . import image_and_text_to_text

    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser('input-image')
    parser.add_argument('query', nargs='?')
    args = parser.parse_args(argv)

    file = sys.stdin.buffer

    if args.query is None:
        text = image_to_text(file)
    else:
        text = image_and_text_to_text(file, args.query)
    print(text)

if __name__ == '__main__':
    main(sys.argv[1:])
