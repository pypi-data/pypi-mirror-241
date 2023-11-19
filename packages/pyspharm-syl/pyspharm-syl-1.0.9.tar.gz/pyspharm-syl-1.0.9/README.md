# pyspharm-syl

This is a derivative of pyspharm compiled with the help of intel oneAPI, built on pyspharm version 1.0.9.

## Requires

- python >= 3.8 < 3.12
- Numpy >= 1.24.3
- intel-fortran-rt

## Platform Support

- win_amd64: python 3.8, 3.9, 3.10, 3.11.  

- linux_x86_64: python 3.8, 3.9, 3.10, 3.11. 


> **As of November 2021**
>
> The default build system for `F2PY` has traditionally been through the enhanced `numpy.distutils` module. This module is based on `distutils` which will be removed in `Python 3.12.0` in **October 2023**; `setuptools` does not have support for Fortran or `F2PY` and it is unclear if it will be supported in the future. Alternative methods are thus increasingly more important.

## Build Method

Windows x86-64

```
python setup.py build config_fc --fcompiler=intelvem
python setup.py bdist_wheel
```

Linux
```
python setup.py build config_fc --fcompiler=intelem
python setup.py bdist_wheel
```

## Original description

Source: https://github.com/jswhit/pyspharm

Requires: Numpy (http://numeric.scipy.org),
and a fortran compiler supported by numpy.f2py,

Please read LICENSE.spherepack

Installation: 

python setup.py install

(to change default fortran compiler you can use e.g.
 python setup.py build config_fc --fcompiler=g95)

View documentation by pointing your browser to html/index.html.

Example programs are provided in the examples directory.

Copyright: (applies only to python binding, Spherepack fortran
source code licensing is in LICENSE.spherepack)

Permission to use, copy, modify, and distribute this software and its
documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appear in all copies and that
both that copyright notice and this permission notice appear in
supporting documentation.
THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS SOFTWARE,
INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, INDIRECT OR
CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF
USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR
OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

-- Jeff Whitaker <Jeffrey.S.Whitaker@noaa.gov>
