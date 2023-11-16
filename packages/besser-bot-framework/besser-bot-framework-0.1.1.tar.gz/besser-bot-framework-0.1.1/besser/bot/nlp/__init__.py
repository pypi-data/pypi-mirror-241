"""Definition of the bot properties within the ``nlp`` (Natural Language Processing) section"""

from besser.bot.core.property import Property

SECTION_NLP = 'nlp'

NLP_LANGUAGE = Property(SECTION_NLP, 'nlp.language', str, 'en')
"""
The chatbot language. This is the expected language the users will talk to the chatbot. Using another language may 
affect the quality of some NLP processes.

The list of available languages can be found at `snowballstemmer <https://pypi.org/project/snowballstemmer/>`_.
Note that luxembourgish (lb) is also partially supported, as the language can be chosen, yet the stemmer is still a work in progress.

Languages must be written in `ISO 639-1 <https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes>`_ format (e.g., 'en'
for English)

name: ``nlp.language``

type: ``str``

default value: ``en``
"""

NLP_REGION = Property(SECTION_NLP, 'nlp.region', str, 'US')
"""
The language region. If specified, it can improve some NLP process You can find a list of regions 
`here <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_.

name: ``nlp.region``

type: ``str``

default value: ``US``
"""

NLP_TIMEZONE = Property(SECTION_NLP, 'nlp.timezone', str, 'Europe/Madrid')
"""
The timezone. It is used for datetime-related tasks, e.g., to get the current datetime. A list of timezones can be found
`here. <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>`_

name: ``nlp.timezone``

type: ``str``

default value: ``Europe/Madrid``
"""

NLP_STEMMER = Property(SECTION_NLP, 'nlp.stemmer', bool, True)
"""
Weather to use a stemmer or not. `Stemming <https://en.wikipedia.org/wiki/Stemming>`_ is the process of reducing 
inflected (or sometimes derived) words to their word stem, base or root form.

For example 'games' and 'gaming' are stemmed to 'game'.

It can improve the NLP process by generalizing user inputs.

name: ``nlp.stemmer``

type: ``bool``

default value: ``True``
"""

NLP_INTENT_THRESHOLD = Property(SECTION_NLP, 'nlp.intent_threshold', float, 0.4)
"""
The threshold for the Intent Classification problem. If none of its predictions have a score greater than the threshold,
it will be considered that no intent was detected with enough confidence (and therefore, moving to a fallback scenario).

name: ``nlp.intent_threshold``

type: ``float``

default value: ``0.4``
"""

