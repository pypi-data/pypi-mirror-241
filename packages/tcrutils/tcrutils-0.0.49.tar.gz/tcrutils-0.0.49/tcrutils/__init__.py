"""Useful stuff for tcr projects."""

from .src.tcr_color import c, color, colour
from .src.tcr_console import console
from .src.tcr_constants import *
from .src.tcr_decorator import autorun, convert
from .src.tcr_dict import dict_zip, merge_dicts
from .src.tcr_extract_error import extract_error
from .src.tcr_getch import getch
from .src.tcr_iterable import batched, cut_at
from .src.tcr_misspellings import asert, trei
from .src.tcr_null import Null
from .src.tcr_path import path
from .src.tcr_print_iterable import print_iterable
from .src.tcr_regex import RegexPreset
from .src.tcr_run import run_sac
from .src.tcr_timestr import timestr

__all__ = [x for x in globals() if not x.startswith('_') and x != 'src']

from .src.tcr_console import breakpoint
from .src.tcr_decorator import test, timeit
from .src.tcr_error import error
from .src.tcr_F import F
from .src.tcr_other import oddeven
from .src.tcr_run import RunSACAble
