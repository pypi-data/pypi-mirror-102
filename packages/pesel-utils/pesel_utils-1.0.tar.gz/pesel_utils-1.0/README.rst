pesel-utils
===========

Just a bunch of utilities for PESEL numbers.

Usage
-----

::

    import pesel_utils

    pesel_utils.is_valid("51030830369") //=> True
    pesel_utils.check_birthdate("51030830369") //=> 1953/3/8
    pesel_utils.check_gender("51030830369") //=> 'female'

