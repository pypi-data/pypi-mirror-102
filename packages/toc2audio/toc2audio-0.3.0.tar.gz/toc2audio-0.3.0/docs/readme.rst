toc2audio
=========

.. WE CAN NOT DO ".. include::" because it would be not valid for PYPI

.. _HTML: https://en.wikipedia.org/wiki/HTML
.. _markdown: https://en.wikipedia.org/wiki/Markdown

.. _MP3: https://en.wikipedia.org/wiki/MP3
.. _M4A: https://en.wikipedia.org/wiki/MPEG-4_Part_14
.. _MP4: https://en.wikipedia.org/wiki/Mp4
.. _Opus: https://en.wikipedia.org/wiki/Opus_(audio_format)
.. _Vorbis: https://en.wikipedia.org/wiki/Vorbis

.. _AAC: https://en.wikipedia.org/wiki/Advanced_Audio_Coding
.. _HE-AAC: https://es.wikipedia.org/wiki/HE-AAC
.. _HE-AACv2: https://es.wikipedia.org/wiki/HE-AAC#HE-AAC_v2

.. _CBR: https://en.wikipedia.org/wiki/Constant_bitrate

.. _bookmarks:
.. _bookmark: https://en.wikipedia.org/wiki/Bookmark

.. _Affero GNU Public License v3: https://www.gnu.org/licenses/agpl-3.0.en.html

.. _FFmpeg: https://en.wikipedia.org/wiki/FFmpeg

.. _the greatest thing since sliced bread: https://en.wikipedia.org/wiki/Sliced_bread#In_popular_culture

This tool parses a Table of Contents file and:

- Optionally, shows HTML_ in your browser and print it too on the
  console, for copy&paste or redirection to complete your
  show notes.

- **TODO:** Optionally, adds the TOC generated HTML_ to an audio
  file.

- Optionally, adds timestamps (chapters) from your TOC file to
  an audio file.

- Optionally, adds timeoffsets to all timestamps (in the
  HTML_ and in the chapters) in order to compensate from initial
  presentation or teasers, advertisements during the audio, etc.

If the audio file already has chapter/TOC metadata, we will
replace it as requested.

Table of Contents format
------------------------

The Table of Contents must be written in markdown_.

toc2audio will parse any markdown_ file and will, optionally,
insert the generated HTML_ and chapters metadata in your audio
file. If you want to use timestamps (chapters), you must use lines
in this format:

[HH:MM:SS] Chapter title

HH:MM:SS is hours:minutes:seconds. The "hours" field is optional.
You can specify fields with one or two digits.

The first line of the markdown_ file will be the title of the
table of contents stored in the audio file if you store chapters
information in it. If that first line is a markdown_ header line,
the markdown_ header tags will be dropped in the (optionally)
stored TOC title.

An example would be:

  .. code-block:: text

     # First line will be the title of the TOC (header marks removed)

     * [00:50] Presentation

         Here I describe the topics we will talk about.

     * [02:11] Topic 1

         Blah blah blah blah...

     * [17:29] Topic 2

         Blah blah blah blah...

.. note::

   Notice that when list items have multiple paragraphs, each
   subsequent paragrap **MUST BE indented** by either **FOUR**
   spaces or a tab, as documented in `Markdown Syntax
   Documentation
   <https://daringfireball.net/projects/markdown/syntax#list>`__
   and in the `documentation
   <https://python-markdown.github.io/#differences>`__ of
   `Python-Markdown <https://python-markdown.github.io/>`__
   project.

Time offset
-----------

You can apply a global time offset to all timestamps in the TOC
markdown_ document using the :code:`--offset` command line
parameter.

Supported audio containers
--------------------------

Supported audio containers are:

- Opus_. If you can choose an audio format freely, you should
  choose Opus_. It is the current (2021) state-of-art for general
  purpose audio (voice and music) and free of patents. It is
  "`the greatest thing since sliced bread`_".

- Vorbis_.

- MP3_.

  .. warning::

     In many MP3_ players, the MP3_ file **MUST BE** CBR_ in order
     for the chapter metadata seeking to be accurate.

- M4A_ (MP4_ audio).

  Usually, MP4_ audiobooks have a **m4b** extension to advertise
  the presence of bookmarks_. Nevertheless, the file is bitwise
  identical to **m4a**. Some software doesn't recognize **m4b**
  files, so I use a **m4a** suffix.

  Usually, the audio format will be AAC_, HE-AAC_ or HE-AACv2_,
  but I don't really care. I manipulate the generic MP4_
  container, I don't pay attention to the audio data. I guess I
  could even add chapters to video data.

  .. warning::

    This feature requires availability of FFmpeg_ software.

Author and License
------------------

The author of this package is Jesús Cea Avión.

- email: jcea@jcea.es.

- Webpage: https://www.jcea.es/.

- Blog: https://blog.jcea.es/.

- Twitter: `@jcea <https://twitter.com/jcea>`__.

This code is licensed under `Affero GNU Public License v3`_
(AGPLv3)


