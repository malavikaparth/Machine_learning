import nltk
nltk.download('punkt')

import re
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
print(word_tokenize('Hi there!'))

#sent_tokenize() TO convert document to snetences
#regex_tokenize() To tokenize a string or dic based on regular expression latter
#TweetTokenizer() TO find hashtags '!!!!' etc.
scene_one = 'E.T. the Extra-Terrestrial is an audiobook and ' \
            'soundtrack companion album for the 1982 blockbuster film ' \
            'directed by Steven Spielberg. Composed by John Williams, the ' \
            'album was narrated by Michael Jackson (pictured), and distributed by MCA Records. ' \
            'The original song "Someone in the Dark", sung by Jackson, bookends the album.' \
            ' The album was released on November 15, 1982 – before Jackson\'s ' \
            'album Thriller was released later that month – which led to a lawsuit by his ' \
            'label, Epic Records, over the soundtrack being released first. ' \
            'The soundtrack album was withdrawn, and the release of the single ' \
            '"Someone in the Dark" was prohibited. The album also featured a poster of ' \
            'Jackson with an animatronic model of E.T.; the image ' \
            'appeared on the cover of Ebony magazine the following ' \
            'month. Despite its curtailed release, E.T. ' \
            'the Extra-Terrestrial reached number 37 on the Billboard 200 and ' \
            'number 82 on the UK Albums Chart. Well-received critically, ' \
            'it won Jackson a Grammy Award for Best Recording for Children'

sentences = sent_tokenize(scene_one)
#print(sentences)
tokenized_sent = word_tokenize(sentences[3])
#print(tokenized_sent)
scene_2 = "SOLDIER #1:" \
          "SOLDIER #2:" \
          "SOLDIER #3:" \
          "SOLDIER #4:"

pattern1 = r'\[a-z]+'
print(re.search(pattern1,scene_2 ))
