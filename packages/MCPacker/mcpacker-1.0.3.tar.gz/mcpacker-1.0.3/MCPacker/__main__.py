# SPDX-FileCopyrightText: 2022-present Didier Malenfant <coding@malenfant.net>
#
# SPDX-License-Identifier: MIT

import sys

from .MCPacker import MCPacker


def main():
    packer = None

    try:
        # -- Remove the first argument (which is the script filename)
        packer = MCPacker(sys.argv[1:])

        if packer is not None:
            packer.main()
    except Exception as e:
        print(e)
    except KeyboardInterrupt:
        print('Execution interrupted by user.')
        pass

    if packer is not None:
        packer.shutdown()


if __name__ == '__main__':
    main()
