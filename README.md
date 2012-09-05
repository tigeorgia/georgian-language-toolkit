Georgian Language Toolkit
=========================

A place to put handy scripts for dealing with Georgian language.

Please include an update to the README with a description of your script in all pull requests.


Ruby
====
-string.rb - extends the ruby string library to add some additional functions for Georgian language
-def latinize(map = LANG_MAP_TO_GEO) - converts a georgian string to latin characters
- def georgianize(map = LANG_MAP_TO_ENG) - converts latin string to georgian characters
- def get_language - returns 'ka' or 'en', whichever langauge predominates in the string
- def is_georgian? - returns true if string is georgian characters
- def is_latin? - returns true if string is latin characters
- def georgian_morph(type = 'basic') - does some morphing on georgian word patterns, but needs development to be of use for anyone


Python/Django
=============
- glt.py - toolkit to deal with Georgian language
 * CHARMAP_GEO2LAT - mapping of Georgian characters to Latin characters
 * CHARMAP_LAT2GEO - mapping of Latin characters to Georgian characters
 *  CHARMAP_UNI2LAT - mapping of various unicode characters to Latin characters
 * def to_georgian - convert a Latin string into the Georgian equivalent
 * def to_latin - convert a Georgian string to the Latin equivalent
 *  def slughifi - replacement for Django's slugify which cannot deal nicely with unicode chars.
 * def lastname_first - converts given name so the lastname comes first (correct georgian declination)
 * def firstname_first - converts given name so the firstname comes first (correct georgian declination)
- pid.py - locate Georgian personal ID numbers
 * def validate_personal_id - Checks a string for basic conformity to Georgia's personal ID number format
 * def extract_ids - Goes through a text file word-by-word looking for strings that validate as IDs.
