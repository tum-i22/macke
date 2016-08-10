"""
Start a complete analysis with the MACKE toolchain on a given bitcode file
"""
import argparse
from .config import check_config
from .Macke import Macke


def main():
    """
    Parse command line arguments, initialize and start a complete MACKE run
    """
    parser = argparse.ArgumentParser(
        description="""\
        Run modular and compositional analysis with KLEE engine on the given
        bitcode file. Depending on the program size, this may take a while.
        """
    )

    parser.add_argument(
        'bcfile',
        metavar=".bc-file",
        type=argparse.FileType('r'),
        help="Bitcode file, that will be analyzed"
    )

    parser.add_argument(
        '--comment',
        nargs='?',
        default="",
        help="Additional comment, that will be stored in the output directory")

    parser.add_argument(
        '--parent-dir',
        nargs='?',
        default="/tmp/macke",
        help="The output directory of the run is put inside this directory")

    check_config()

    args = parser.parse_args()

    m = Macke(args.bcfile.name, args.comment, parentdir=args.parent_dir)
    m.run_complete_analysis()

if __name__ == "__main__":
    main()
