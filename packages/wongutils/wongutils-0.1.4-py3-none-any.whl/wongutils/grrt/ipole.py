__copyright__ = """Copyright (C) 2023 George N. Wong"""
__license__ = """
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import subprocess
import numpy as np
from scipy.optimize import brentq


def evaluate_flux_difference(munit, dumpfiles, target_flux, logname=None, unpol=False, **kwargs):
    """ TODO (move to parent module?) """
    Ftots = []
    for dumpfile in dumpfiles:
        try:
            Ftot_unpol, Ftot = get_fluxes(dumpfile, munit=munit, unpol=unpol, **kwargs)
            if unpol:
                Ftots.append(Ftot_unpol)
            else:
                Ftots.append(Ftot)
        except:
            pass
    Ftot = np.array(Ftots).mean()
    print(f"tried {munit} and got {Ftot} (target {target_flux})")
    if logname is not None:
        fp = open(logname, 'a')
        fp.write(f"iteration {munit} -> {Ftot} (target {target_flux})\n")
        fp.close()
    return Ftot - target_flux


def get_seed_value(dumpfiles, target_flux, munit_low, munit_high, logname=None, xtol=0.05, **kwargs):
    """ TODO write documentation """
    flux_differences = []
    munits = np.logspace(np.log10(munit_low), np.log10(munit_high), 11)
    munit_low = None
    munit_high = None
    for mi, munit in enumerate(munits):
        flux_differences.append(evaluate_flux_difference(munit, dumpfiles, target_flux, logname=logname, **kwargs))
        if flux_differences[-1] > 0:
            if mi > 0:
                munit_high = munit
            else:
                munit_high = munit
                munit_low = munit / 10.
            break
        munit_low = munit
    precise_text = f">> starting more precise fit with ({munit_low}, {munit_high})"
    print(precise_text)
    if logname is not None:
        fp = open(logname, 'a')
        fp.write(precise_text + "\n")
        fp.close()
    return fit_munit(dumpfiles, target_flux, munit_low, munit_high, logname=logname, xtol=xtol, **kwargs)


def fit_munit(dumpfiles, target_flux, munit_low, munit_high, logname=None, xtol=None, fit_as_log=False, **kwargs):
    """ TODO (move to parent module?) """
    if xtol is None:
        xtol = munit_low/10.
    def fa(x): return x
    def fb(x): return x
    if fit_as_log:
        def fa(x): return np.exp(x)
        def fb(x): return np.log(x)
    root = brentq(lambda x: evaluate_flux_difference(fa(x), dumpfiles, target_flux, logname=logname, **kwargs), fb(munit_low), fb(munit_high), xtol=xtol)
    munit = fa(root)
    if logname is not None:
        fp = open(logname, 'a')
        fp.write(f"result {munit}\n\n")
        fp.close()
    return munit


def run_ipole(dumpfile, rlow=1, outfile=None, rhigh=40, thetacam=163, target=None, munit=1.e25, freqcgs=230.e9, res=160, verbose=False, unpol=False, tracef=None, executable="./ipole", onlyargs=False):
    """ TODO """

    if target is None:
        target = "m87"
    target = target.lower()

    if target == "m87":
        mbh = 6.5e9
        dsource = 16.8e6
    elif target == "sgra":
        mbh = 4.1e6
        dsource = 8127
    else:
        print(f"! unrecognized target \"{target}\"")

    freqarg = f"--freqcgs={freqcgs}"
    mbharg = f"--MBH={mbh}"
    munitarg = f"--M_unit={munit}"
    dsourcearg = f"--dsource={dsource}"
    incarg = f"--thetacam={thetacam}"
    rlowarg = f"--trat_small={rlow}"
    rhigharg = f"--trat_large={rhigh}"
    dumpfilearg = f"--dump={dumpfile}"
    resarg = f"--nx={res} --ny={res}"

    args = [executable, freqarg, mbharg, munitarg, dsourcearg, incarg, rlowarg, rhigharg, dumpfilearg, resarg]

    if tracef is not None:
        args += [f"--trace_outf={tracef}"]

    if outfile is None:
        args += ["-quench"]
    else:
        args += [f"--outfile={outfile}"]

    if unpol:
        args += ["-unpol"]

    if onlyargs:
        return args

    if verbose:
        print(" ... running \"" + " ".join(args) + "\"")

    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = [z for y in [str(x)[2:-1].split('\\n') for x in proc.communicate()] for z in y]

    return output


def get_fluxes(dumpfile, rlow=1, rhigh=40, thetacam=163, target=None, munit=1.e25, freqcgs=230.e9, res=160, verbose=False, unpol=False):
    """ TODO """

    exe = "./ipole"

    if target is None:
        target = "m87"
    target = target.lower()

    if target == "m87":
        mbh = 6.5e9
        dsource = 16.8e6
    elif target == "sgra":
        mbh = 4.1e6
        dsource = 8127
    else:
        print(f"! unrecognized target \"{target}\"")

    freqarg = f"--freqcgs={freqcgs}"
    mbharg = f"--MBH={mbh}"
    munitarg = f"--M_unit={munit}"
    dsourcearg = f"--dsource={dsource}"
    incarg = f"--thetacam={thetacam}"
    rlowarg = f"--trat_small={rlow}"
    rhigharg = f"--trat_large={rhigh}"
    dumpfilearg = f"--dump={dumpfile}"
    resarg = f"--nx={res} --ny={res}"

    args = [exe, freqarg, mbharg, munitarg, dsourcearg, incarg, rlowarg, rhigharg, dumpfilearg, resarg]
    args += ["-quench"]
    if unpol:
        args += ["-unpol"]

    if verbose:
        print(" ... running \"" + " ".join(args) + "\"")

    proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = [z for y in [str(x)[2:-1].split('\\n') for x in proc.communicate()] for z in y]
    Ftot_line = [l for l in output if 'unpol xfer' in l][0]
    st = Ftot_line.split()
    Ftot_unpol = float(st[-2+st.index('unpol')][1:])
    Ftot = float(st[-4+st.index('unpol')])

    return Ftot_unpol, Ftot


