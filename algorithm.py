import re
import os

KEYWORDS = {}
BASE_DIR = os.path.dirname(__file__)
config_dir = os.path.join(BASE_DIR, "config")

#Get all files in the config folder
for filename in os.listdir(config_dir):
    lines = open(config_dir + '/' + filename, 'r')

    for line in lines.readlines():
        term = line.split('\n')[0]  # We only want the word
        KEYWORDS[term] = filename.split('.')[0]

KEYWORDS = KEYWORDS.items()


class Algorithm():

    def __init__(self, message):
        self.message = message

    def _determine_keywords(self):
        #We're only interested in words that contain more than 4 characters
        return re.findall('[a-zA-Z]{4,}', self.message)

    def determine_language(self):
        keywords_in_message = self._determine_keywords()
        languages = [
            #[language, count]
        ]

        for keyword in keywords_in_message:
            try:
                #Locate the keyword in the KEYWORDS dictionary
                place_in_keyword_dict = [x[0] for x in KEYWORDS].index(keyword)
            except ValueError:
                #The keyword was not in the dictionary, go to the next keyword
                continue

            try:
                #Check if this language is already in our tuple, if yes add one
                place_in_languages = [x[0] for x in languages].index(KEYWORDS[place_in_keyword_dict])
                languages[place_in_languages][1] += 1
            except ValueError:
                #Not used yet, add the language with the weight of 1
                languages.append([KEYWORDS[place_in_keyword_dict][1], 1])

        if len(languages) == 0:
            return "I don't know"
        else:
            sorted(languages, key=lambda language: language[1])  # Get highest ranked language
            return languages[0][0]