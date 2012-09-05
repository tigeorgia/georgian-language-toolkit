import re
import codecs

###########################################################
# locate personal IDs
###########################################################

def validate_personal_id(pid):
    """Checks whether the passed string conforms to the
    Georgian standard for Personal ID numbers (11 digits).
    Raises a ValueError if the ID does not validate.

    @param pid: String to check
    @type pid: str
    """
    pattern = re.compile('^\d{11,11}$') # A personal number is 11 digits
    if len(pid) != 11 or pattern.match(pid) == None:
        raise ValueError(u"Incorrect ID number format: {0}".format(pid))

def extract_ids(from_file):
    """Iterator that goes through an input file and returns
    all the strings that match the format of a Georgian
    Personal ID (11 digits).

    @param from_file: file to read
    @type from_file: str
    @return: Generator of PIDs in file
    @rtype: str
    """
    with codecs.open(from_file,mode='r',encoding='utf-8') as ifile:
        for line in ifile:
            for word in line.split():
                try:
                    validate_personal_id(word)
                    yield word
                except ValueError:
                    pass
