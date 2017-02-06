latex-diceware
==============

Wordlists and some other files for my nicely formatted diceware lists.

Visit the [diceware](http://world.std.com/~reinhold/diceware.html) site, the obligatory [XKCD](https://xkcd.com/936/), and get some dice.

There are two sources of words:

### Beolingus:

The “deutsche(n) Wortliste(n)” and the “Diceware English word list” are based on the [Beolingus](http://dict.tu-chemnitz.de/) online dictionary:

* Copyright (c) :: Frank Richter <frank.richter.tu-chemnitz.de>,
* 1995 - 2010
* License :: GPL Version 2 or later; GNU General Public License
* URL :: http://dict.tu-chemnitz.de/

These finished word lists PDFs,
* deutsche Wortliste für Diceware, für W20.pdf
* deutsche Wortliste für Diceware, für W6.pdf
* Diceware English word list for use with d20.pdf
are licensed as GPL 3 or later, not GPL 2.

### EFF

[Joseph Bonneau](https://www.eff.org/about/staff/joseph-bonneau) of the [EFF](https://www.eff.org/) has published an [article](https://www.eff.org/deeplinks/2016/07/new-wordlists-random-passphrases) with new word lists. As i had fixed a few of the problems noted in the article, and wanted to fix another one – “dirty” words unsuitable to hand out to customers – it seemed obvious to combine my formatting with their word lists.

The results are the three lists
* EFF large wordlist.pdf
* EFF short wordlist 1.pdf
* EFF short wordlist 2.pdf

These are licensed as CC-BY

## Python script

The python script is used to replace the place holder “foobar” in the latex file templates with words from wordlists.
It is licensed as GPL 3 or later.
