Georgian Language Toolkit
=========================

A place to put handy scripts for dealing with Georgian language.

Please include an update to the README with a description of your script in all pull requests.


Ruby
====
string.rb - extends the ruby string library to add some additional functions for Georgian language
# def latinize(map = LANG_MAP_TO_GEO) - converts a georgian string to latin characters
# def georgianize(map = LANG_MAP_TO_ENG) - converts latin string to georgian characters
# def get_language - returns 'ka' or 'en', whichever langauge predominates in the string
# def is_georgian? - returns true if string is georgian characters
# def is_latin? - returns true if string is latin characters
# def georgian_morph(type = 'basic') - does some morphing on georgian word patterns, but needs development to be of use for anyone