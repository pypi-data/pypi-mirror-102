# LyChoRhyce

The LyChoRhyce program reads LCR-formatted song text files and generates
beatiful HTML files, ready to be printed or converted into PDF files.

## The LCR format

LCR (Lyrics, Chords and Rhythm) is a textual format for describing songs in a
simpler way than sheet music. You write text like this:

~~~ txt
Scarborough Fair

Authors = Simon & Garfunkel
Meter = 3/4
Key = Em

---

Verse 1 =
| Em~ Are ` ` you | going ` ` to | D~ Scar- ` \ bo- ` rough | Em~ Fair? ` ` |
| G~ ` Par- ` sley, | Em~ sage, ` ` rose- | G~ ma- ` A~ ry ` and | Em~ thyme ` ` |
| ` ` Re- | mem- ` ` ber | G~ me ` ` to | one ` who ` lives | D~ there ` ` |
| Em~ she ` ` once | D~ was ` ` a | true ` love ` of | Em~ mine ` ` |
~~~

and it gets converted to this:

![full render](https://lcr4songs.readthedocs.io/en/latest/lcr/overview/overview1.png)

The output is similar to popular
[CRD song sheets](https://www.ultimate-guitar.com/contribution/help/rubric#iii2),
and the source text and operations are similar to the
[ChordPro](https://www.chordpro.org/chordpro/chordpro-file-format-specification/)
format. The main added value is the rhythmic information: it shows measure
boundaries (the black vertical lines) and beat boundaries (the grey lines).

Then again, the rhythmic information is optional. We could have only measures but not beats:

![measure-only render](https://lcr4songs.readthedocs.io/en/latest/lcr/overview/overview2.png)

or no rhythm information at all, and we are back to CRD and ChordPro:

![no-rhythm render](https://lcr4songs.readthedocs.io/en/latest/lcr/overview/overview3.png)

The
[Time in Music Notation](https://lcr4songs.readthedocs.io/en/latest/lcr/time-in-music-notation/)
article has a fuller comparison of the main music notations.

## Other features

The format also has the following features:

- arbitrary fields in the song header
- song sections (verse, chorus etc.) with title and description
- multiple songs in one file
- optional column layout
- page layout in PDF and print

## Copyright

The LyChoRhyce program is copyright (c) 2021 Nicola 'teknico' Larosa.
Licensed under GPLv3 only, see the LICENSE.md file for details.

The LCR format documentation by [Nicola 'teknico' Larosa](https://sr.ht/~teknico/)
is licensed under the Creative Commons
[Attribution-ShareAlike 4.0 International](http://creativecommons.org/licenses/by-sa/4.0/)
license.

![CC-BY-SA](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)
