# `imcflibs3` - IMCF Py3 helper collection 🐍 🔩 🔧 🪛

This package contains a small collection of Python 3.x functions dealing with
paths, I/O (file handles, ...), strings and so on.

Initially contained in the [`imcflibs`][1] package (note the missing *3*
there!), this has been forked into a separate project for being able to support
current Python versions - the *original* [`imcflibs`][1] package is nowadays
exclusively useful within the [Fiji][fiji] / [ImageJ2][imagej] ecosystem and
therefore limited to Python 2.7 (or rather Jython 2.7, see the [Jython 3
roadmap][jython3] for more details on this topic).

As some of our other packages (e.g. [micrometa][micrometa]) are depending on
stuff provided by [`imcflibs`][1], this [`imcflibs3`][3] package has been
created to provide those functions without the limitations mentioned above.
Obviously the [`imcflibs.imagej`][2] submodule doesn't make sense in a *CPython*
environment and therefore has been stripped completely from the [`imcflibs3`][3]
package.

## Note about package versions and compatibility

Package versions will go side-by-side with the corresponding releases of the
[`imcflibs`][1] package while skipping those releases that only affect the
[`imcflibs.imagej`][2] submodule(s). In other words, there might (will) be
version jumps of the [`imcflibs3`][3] package in case there have been releases
of the [`imcflibs`][1] one in between that were not affecting the functions
contained here.

Please note that this approach might change in the future if we discover the
missing versions to be a complicating factor in packaging / testing.

----

Developed and provided by the [Imaging Core Facility (IMCF)][imcf] of the
Biozentrum, University of Basel, Switzerland.

----

[1]: https://github.com/imcf/python-imcflibs
[2]: https://github.com/imcf/python-imcflibs/tree/master/src/imcflibs/imagej
[3]: https://github.com/imcf/python-imcflibs3
[fiji]: <https://fiji.sc>
[imagej]: <https://imagej.net>
[jython3]: <https://www.jython.org/jython-3-roadmap>
[micrometa]: <https://github.com/imcf/python-micrometa>
[imcf]: <https://imcf.one>
