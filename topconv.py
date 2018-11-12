#!/bin/python2.7
import parmed as pmd
import argparse as ap

parser = ap.ArgumentParser(description='Convert Amber prmtop & inpcrd file to Gromacs topology file.')
parser.add_argument('-p', dest='prmtop', required=True, metavar='[.prmtop]', help='[INPUT]  Amber prmtop file')
parser.add_argument('-c', dest='inpcrd', required=True, metavar='[.inpcrd]', help='[INPUT]  Amber inpcrd file')
parser.add_argument('-t', dest='top', required=False, metavar='[.top]', help='[OUTPUT] Gromacs Topology file')
parser.add_argument('-g', dest='gro', required=False, metavar='[.gro]', help='[OUTPUT] Gromacs Structure file')

args = parser.parse_args()

if (not args.top) and (not args.gro):
	print('No output file.')
	quit()

amber = pmd.load_file(args.prmtop, args.inpcrd)

if args.top:
	amber.save(args.top, overwrite=True, combine='all')

if args.gro:
	amber.save(args.gro, overwrite=True)
