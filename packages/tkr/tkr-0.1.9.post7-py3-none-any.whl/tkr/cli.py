__all__: tuple = (
  'main',
)

import argparse
import pathlib

def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description='tkr: Python Toolkit')
    parser.add_argument('key', type=str, help='tkr coreattrs new key')
    parser.add_argument('value', type=str, help='tkr coreattrs new key value')

    args: object = parser.parse_args()
    path_abs: str = f'{pathlib.Path(__file__).parent.absolute()}/core/coreattrs.json'

    data: dict = {args.key: args.value}
    with open(path_abs, 'a') as file:
      file.append(data)

if __name__ == '__main__':
    main()