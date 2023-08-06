##############################################################################
hanjaq 0.0.3
##############################################################################

This Python package can be used to get information about Hanja characters:

- the possible meanings of a Hanja character
- Hangul representations of a Hanja character

This information was taken from a shared Anki deck called "1,800 Hancha
(Hanja 한자 漢字)", which contains the 1800 most common and important Hanja
that each Korean student should know by the end of high school. This deck can
be downloaded at the following URL: https://ankiweb.net/shared/info/588300654

This package was originally created to help with the programmatic creation of
Anki decks in which Hanja was used as a supportive tool.


==============================================================================
Features
==============================================================================

Import and use the function `get_hanja_information(character)` to
retrieve information about a Hanja character. This function returns a tuple
that contains the Hangul representation(s) of a Hanja character, and the
meaning(s) of the Hanja character.

.. code-block:: python

    >>> from hanjaq import get_hanja_information
    >>> get_hanja_information("字")
    ("자", "character, letter")

Not all Hanja characters are currently supported, only the 1800 most common
ones. A tuple of empty strings is returned if the Hanja character is not
recognized.

.. code-block:: python

    >>> from hanjaq import get_hanja_information
    >>> get_hanja_information("譎")
    ("", "")


==============================================================================
Install
==============================================================================

You can install this package using pip:

.. code-block:: sh

    $ pip install --user hanjaq


==============================================================================
License
==============================================================================

This project is released under the MIT license.
