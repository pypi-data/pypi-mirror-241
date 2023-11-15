"""Module to parse arguments passed by Thunderhead Results"""
import argparse
import sys, os
from typing import Optional

arguments: Optional[argparse.Namespace] = None

if 'sphinx' not in sys.argv[0]:
    _arugment_parser : argparse.ArgumentParser = argparse.ArgumentParser()

    _arugment_parser.add_argument('--path', nargs="+", dest="pathfinder", help="Names of Pathfinder Results .pfr files")
    _arugment_parser.add_argument('--fds', nargs="+", dest="pyrosim", help="Names of PyroSim Results .smv files")
    _arugment_parser.add_argument("--ventus", nargs="+", dest="ventus", help="Names of Ventus Results files")

    arguments = _arugment_parser.parse_known_args()[0]