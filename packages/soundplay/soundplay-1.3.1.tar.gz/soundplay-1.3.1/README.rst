soundplay
=========
*playsound, but modern!*

Installation
------------
Install via pip:

.. code-block:: bash

    $ pip install soundplay

Done.

If you insist on the (slightly) harder way of installing, from source,
you know how to do it already and don't need my help.

The latest version of the source code can be found at:
https://github.com/paxcoder/soundplay

Quick Start
-----------
Once you've installed, you can really quickly verified that it works with just this:

.. code-block:: python

    >>> from soundplay import playsound
    >>> playsound('/path/to/a/sound/file/you/want/to/play.mp3') 

Documentation
-------------
The soundplay is working like playsound.  contains only one thing - the function ( named) playsound.

It requires one argument - the path to the file with the sound you'd like to play. This may be a local file, or a URL.

There's an optional second argument, block, which is set to True by default. Setting it to False makes the function run asynchronously.

On Windows, uses windll.winmm. WAVE and MP3 have been tested and are known to work. Other file formats may work as well.

On OS X, uses AppKit.NSSound. WAVE and MP3 have been tested and are known to work. In general, anything QuickTime can play, playsound should be able to play, for OS X.

On Linux, uses GStreamer. Known to work on Ubuntu 14.04 and ElementaryOS Loki. I expect any Linux distro with a standard gnome desktop experience should work.
Copyright
---------
This software is Copyright (c) 2021 Taylor Marks <taylor@marksfam.com>.

See the bundled LICENSE file for more information.
