Changelog
=========

.. include:: links.rst

* 0.6.0 - Work in progress

* 0.5.0 - 2021-04-16

  - MP3_: Force a rewrite of the audio file only when the metadata
    is updated.

  - MP3_: Only clean old chapter information if we are adding new
    chapter information. Leave metadata alone if the user doesn't
    want to change it.

  - Add "toc2audio" identification in the audio file comment
    section.

  - MP4_: Preserve metadata of the original file, except the
    chapter information we are inserting.

  - Chapter titles: new lines transformed to spaces. Tabs
    transformed to spaces. Multiple spaces replaced by a single
    space.

  - When adding chapters to audio file, print the chapter list on
    the terminal.

  - **COMPATIBILITY WARNING:** Drop HTML tags in chapter titles.
    Keep only the text.

  - Better audio player chapter compatibility using Opus_ and
    Vorbis_ audio files.

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

  - New theme for Sphinx: `sphinx_rtd_theme
    <https://github.com/readthedocs/sphinx_rtd_theme>`__.

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
