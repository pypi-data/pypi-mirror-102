Changelog
=========

.. _MP3: https://en.wikipedia.org/wiki/MP3
.. _ID3: https://en.wikipedia.org/wiki/ID3
.. _CBR: https://en.wikipedia.org/wiki/Constant_bitrate
.. _M4A: https://en.wikipedia.org/wiki/MPEG-4_Part_14
.. _MP4: https://en.wikipedia.org/wiki/Mp4
.. _Opus: https://en.wikipedia.org/wiki/Opus_(audio_format)
.. _Vorbis: https://en.wikipedia.org/wiki/Vorbis
.. _FFmpeg: https://en.wikipedia.org/wiki/FFmpeg

.. _HTML: https://en.wikipedia.org/wiki/HTML
.. _markdown: https://en.wikipedia.org/wiki/Markdown

.. _urls:
.. _url: https://en.wikipedia.org/wiki/URL
.. _PyPI: https://pypi.org/

* 0.5.0 - Work in progress

* 0.4.0.post1 - 2021-04-14

  - Correct project URLs_ in PyPI_.

* 0.4.0 - 2021-04-14

  - **COMPATIBILITY WARNING:** Drop the feature of the first line
    in the TOC markdown_ file being the TOC title. Only MP3_
    supports that. Now, when tagging mp3_, we use the audio ID3_
    title as the TOC title.

  - Install :code:`toc2audio` command line utility.

  - Add :code:`--version` command line parameter.

  - New URLs_ for the project documentation, changelog, etc.

  - New theme for Sphinx: sphinx_rtd_theme.

* 0.3.0 - 2021-04-14

  - An optional :code:`--offset` command line parameter allows to
    specify a global offset to add to all timestamps. Useful to
    specify the duration of the intro you will add to the audio
    you listened in order to write the show notes markdown_
    document.

  - Beside showing the TOC in your browser, the HTML_ is printed
    in the terminal. You can copy&paste or redirect it to complete
    your show notes.

  - A timestamp can be shown as compact format (MM:SS) or not
    compact format (00:MM:SS).

  - A timestamp is declared as compact or not compact when read
    from the TOC markdown_ document. The idea is to keep the same
    representation that the user used in the TOC markdown_
    document, after applying the optional time offsets.

* 0.2.0 - 2021-04-13

  - We can add chapters to M4A_ files now. This feature requires
    availability of FFmpeg_ software.

  - We can add chapters to Opus_ files now.

  - We can add chapters to Vorbis_ files now.

  - The chapter end time should be provided in the TOC object,
    instead of each audio tagger taking care of calculating it.

* 0.1.0 - 2021-04-09

  Initial release. It can add chapters to MP3_ files.

  .. warning::

     In many MP3_ players, the MP3_ file **MUST BE** CBR_ in order
     for the chapter metadata seeking to be accurate.
