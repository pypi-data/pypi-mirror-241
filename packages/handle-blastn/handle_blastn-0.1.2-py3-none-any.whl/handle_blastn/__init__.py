import _progs
import wonderparse as _wp

from ._clines import *
from ._summaries import *


def main(args=None):
    _wp.easymode.simple_run(
        args=args,
        program_object=_progs,
        prog='handle_blastn',
    )

if __name__ == '__main__':
	main()