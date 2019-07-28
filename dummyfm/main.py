import numpy as np
from scipy.interpolate import interp1d
import argparse

def main():
    parser = argparse.ArgumentParser("Dummy forward model")
    parser.add_argument("finput", type=str,
        help="The input file name")
    parser.add_argument("-n", type=int, default=1000,
        help="The number of output values (default: 1000)")
    parser.add_argument("-o", type=str, default="output.txt",
        help="The output file name (default: 'output.txt')")
    parser.add_argument("-t", type=str, default="cubic",
        help="Interpolation type (default: 'cubic')")
    args = parser.parse_args()

    # normalize the input arguments
    args.t = args.t.lower().strip()
    args.o = args.o.strip()

    # check if args.t is among the options
    interp_types = ["cubic", "quadratic", "linear"]
    if args.t not in interp_types:
        raise RuntimeError("Argument -t must be one of %s" % str(interp_types))

    # execute the main program
    execprog(args)

def execprog(args):
    finput = args.finput
    nout = args.n
    foutput = args.o
    interp_kind = args.t.lower().strip()

    # read the input
    yinp = np.loadtxt(finput).ravel()
    ninp = len(yinp)
    xinp = np.linspace(0.0, 1.0, ninp)

    # interpolate
    xout = np.linspace(0.0, 1.0, nout)
    finterp = interp1d(xinp, yinp, kind=interp_kind)
    yout = finterp(xout)

    # write the output to the output file
    np.savetxt(foutput, yout)
