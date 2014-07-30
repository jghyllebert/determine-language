import json
import sys
from algorithm import Algorithm


def validate_file(fp):
    if fp.name.rsplit('.', 1)[1] == "txt":
        return True
    return False


def validate_contents(string):
    try:
        json.loads(string)
        return True
    except ValueError:
        return False


def parse_file(fp):
    #Check if file validates and the content
    if validate_file(fp):
        lines = fp.read().replace('\n', '')
        if validate_contents(lines):
            #do JSON stuff, bonus points right here
            pass
        else:
            parse_text = Algorithm(lines)
            return parse_text.determine_language()


def main():
    print parse_file(open(sys.argv[1]))


if __name__ == "__main__":
    main()