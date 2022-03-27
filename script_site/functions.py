# Here we create our boolean maker function
# There are 3 main sources of information we need for our function:
# Tech, Job and Language
# It is not ideal to look for Location, as the Boolean will bring false positives (looking for the name anywhere)
# It is possible to look for platform, but it is only useful in a broad search engine (Google)
# These three aspects will be organized in the string like this:
# ("Tech") AND ("Job") And ("Language")
# After that, it is necessary to know the quality level of your search.
# High quality searches will bring high quality candidates, but in very low amount
# Low quality searches will bring low quality candidates, but in great quantity
# It is ideal to start with high quality, then proceed to low quality


def booleanmaker(tech,job,language,level):
    python_b = {
        "1" : "This is a high level python search",
        "2" : "This is a mid level python search",
        "3" : "This is a low level python search"
    }
    react_b = {
        "1" : "This is a high level react search",
        "2" : "This is a mid level react search",
        "3" : "This is a low level react search"
    }
    tech_b = {'python':python_b,
              'react':react_b}
    developer_b = {
        "1" : "This is a high level developer search",
        "2" : "This is a mid level developer search",
        "3" : "This is a low level developer search"
    }
    devops_b = {
        "1" : "This is a high level devops search",
        "2" : "This is a mid level devops search",
        "3" : "This is a low level devops search"
    }
    techlead_b = {
        "1" : "This is a high level techlead search",
        "2" : "This is a mid level techlead search",
        "3" : "This is a low level techlead search"
    }
    job_b = {'developer': developer_b,
           'devops': devops_b,
           'techlead':techlead_b}
    english_b = {
        "1": "This is a high level english search",
        "2": "This is a mid level english search",
        "3": "This is a low level english search"
    }
    portuguese_b = {
        "1": "This is a high level portuguese search",
        "2": "This is a mid level portuguese search",
        "3": "This is a low level portuguese search"
    }
    spanish_b = {
        "1": "This is a high level spanish search",
        "2": "This is a mid level spanish search",
        "3": "This is a low level spanish search"
    }
    language_b = {'english':english_b,
                'portuguese':portuguese_b,
                'spanish':spanish_b}
    boolean = tech_b[tech][level] + job_b[job][level] + language_b[language][level]
    return boolean