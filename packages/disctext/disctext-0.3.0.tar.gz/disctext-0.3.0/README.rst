.. raw:: html

    <p align="center">
        <a href="#readme">
            <img alt="Grid-Header" src="https://github.com/akbar-amin/resources/blob/master/grid-header.gif">
        </a>
    </p>
    <p align="center">
        <a href="https://pypi.python.org/pypi/disctext"><img alt="Pypi version" src="https://img.shields.io/pypi/v/disctext.svg"></a>
        <a href="https://github.com/akbar-amin/disctext/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-blue"></a>
    </p>
  
********
Disctext
********

A simple tool for creating ASCII art and sharing it on Discord. 
`Disctext` uses `eventkit <https://eventkit.readthedocs.io/en/latest/index.html>`_ to construct a video-capture pipeline, where individual frames are transformed into text and displayed as Discord messages. 

Messages are packed into Markdown code blocks before they are sent. This was done to workaround Discord's auto-formatting, which would ruin the art with bolds, italics, etc.
However, code blocks also provide extra contrast and "color" via syntax highlighting.

Art Customizations:

* `Syntax Highlights <https://git.io/JYv64>`_
* Total area and/or width 
* Background inversion 

.. end-intro

Installation
------------

::

    pip install disctext

When using the command-line tool, make sure ``disctext`` can be found in PATH. 

For discord interaction, a bot token is required with permissions to send messages. 
Make sure to also have "Developer Mode" enabled in user settings to retrieve channel ids.

Usage
-----

Simply specify a video file along with a bot token and destination channel. 

.. code-block:: python

    import disctext
    from pathlib import Path 

    video = Path.home() / "downloads" / "video.mp4"
    disctext.run(video, <token>, <channel>)

Same example via command-line::

    disctext -v ".../downloads/video.m4" -t <token> -c <channel>


Refer to `disctext.run <https://github.com/akbar-amin/disctext/blob/27143e2a4cbc41b6f6a0d585dd57e3c617f88b7b/disctext/session.py#L71>`_ for optional arguments. 

Playback 
--------

1. Using the Discord search bar, search for one of the following: 

    a. The channel using the ``in`` query and sort by ``old``.
    b. The "now playing" message sent at start of every run and sort by ``new``.

2. Click the first result (most likely).
3. Click anywhere inside the cell and hold the down arrow key.

The playback speed is around 30 FPS, or messages-per-second in this case. 

It's worth noting that Discord loads messages as HTTP requests in chunks of 50, so there is a short pause (~120-200 ms) every 2 seconds. 
The pauses are most likely due to server response times, content download speed, etc. 
However, a workaround is to take advantage of request caching and run the playback twice, where the second playback should run smoother.

Demo
----

Aside from the original clips [#]_ [#]_, all recordings were done on Discord using the method above. Demos can be found in `this <https://discord.gg/jhvBB3n5Pc>`_ server as well. 


.. raw:: html

    <p align="center">
        <a href="#demo">
            <img alt="Grid-Demo" src="https://github.com/akbar-amin/resources/blob/master/grid.gif">
        </a>
    </p>
    
    
.. |grid1| image:: https://github.com/akbar-amin/resources/blob/master/grid-1.gif
.. |grid2| image:: https://github.com/akbar-amin/resources/blob/master/grid-2.gif
.. |grid3| image:: https://github.com/akbar-amin/resources/blob/master/grid-3.gif
.. |grid4| image:: https://github.com/akbar-amin/resources/blob/master/grid-4.gif
.. |grid5| image:: https://github.com/akbar-amin/resources/blob/master/grid-5.gif
.. |grid6| image:: https://github.com/akbar-amin/resources/blob/master/grid-6.gif
.. |grid7| image:: https://github.com/akbar-amin/resources/blob/master/grid-7.gif
.. |grid8| image:: https://github.com/akbar-amin/resources/blob/master/grid-8.gif
.. |grid9| image:: https://github.com/akbar-amin/resources/blob/master/grid-9.gif
.. |steamboat1| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-1.gif
.. |steamboat2| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-2.gif
.. |steamboat3| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-3.gif
.. |steamboat4| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-4.gif
.. |steamboat5| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-5.gif
.. |steamboat6| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-6.gif
.. |steamboat7| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-7.gif
.. |steamboat8| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-8.gif
.. |steamboat9| image:: https://github.com/akbar-amin/resources/blob/master/steamboat-9.gif
    

.. table::
    :align: center 
    :widths: grid

    
    +-----------------------------------------+-----------------------------------------+-----------------------------------------+
    | |grid1|                                 | |grid2|                                 | |grid3|                                 |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    +-----------------------------------------+-----------------------------------------+-----------------------------------------+
    | |grid4|                                 | |grid5|                                 | |grid6|                                 |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    +-----------------------------------------+-----------------------------------------+-----------------------------------------+
    | |grid7|                                 | |grid8|                                 | |grid9|                                 |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    +-----------------------------------------+-----------------------------------------+-----------------------------------------+


.. raw:: html

    <p align="center">
        <a href="#demo">
            <img alt="Steamboat-Demo" src="https://github.com/akbar-amin/resources/blob/master/steamboat.gif">
        </a>
    </p>





.. table::
    :align: center 
    :widths: grid

    +-----------------------------------------+-----------------------------------------+-----------------------------------------+
    | |steamboat1|                            | |steamboat2|                            | |steamboat3|                            |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    +-----------------------------------------+-----------------------------------------+-----------------------------------------+
    | |steamboat4|                            | |steamboat5|                            | |steamboat6|                            |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    +-----------------------------------------+-----------------------------------------+-----------------------------------------+
    | |steamboat7|                            | |steamboat8|                            | |steamboat9|                            |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    |                                         |                                         |                                         |
    +-----------------------------------------+-----------------------------------------+-----------------------------------------+




.. [#] *Grid [Psychedelic Animation]*. (2013, January 2). [Video]. `Youtube <https://www.youtube.com/watch?v=OWa5rzEOumQ>`_.

.. [#] *"Steamboat Willie"* Internet Archive, Walt Disney Animation Studios, 8 Nov. 1928, archive.org/details/SteamboatWillie. 