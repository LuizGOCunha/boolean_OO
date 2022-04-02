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
    stackdict={"react": '"frontend" OR "front end"',
                "python": '"backend" OR "back end"'}
    python_b = {
        # High: asks for python, the two biggest frameworks, and one of the other smaller frameworks
        "high" : '("python" OR "phyton" OR "py") AND ("django") AND ("flask") AND ("py*") AND ',
        # Medium: asks for python and one of the frameworks
        "mid" : '("python" OR "phyton" OR "py") AND ("django" OR "flask" OR "py*") AND ',
        # Low: asks for python or one of its frameworks
        "low" : '("python" OR "phyton" OR "py" OR "django" OR "flask" OR "py*") AND '
    }
    react_b = {
        # High: asks for react, javascript, and one of the many other frameworks
        "high" : '("react" OR "reactjs" OR "react.js") AND ("javascript" OR "js") AND ("*js") AND ',
        # Medium: asks for react, javascript or other framework
        "mid" : '("react" OR "reactjs" OR "react.js") AND ("javascript" OR "js" OR "*js") AND ',
        # Low: asks for react or javascript or any other framework even.
        "low" : '("react" OR "reactjs" OR "react.js" OR "javascript" OR "js" OR "*js") AND '
    }
    tech_b = {'python':python_b,
              'react':react_b}
    developer_b = {
        # High: Asks for the job title, max seniority, a professional focused on the tech, and fullstack
        "high" : f'("developer" OR "coder" OR "software engineer") AND ("senior") AND ("{tech} developer" OR "{tech} engineer") AND ("fullstack") AND ',
        # Mid: Asks for the job title or a professional of the tech, max or mid seniority, and the appropriate stack
        "mid" : f'("developer" OR "coder" OR "software engineer" OR "{tech} developer" OR "{tech} engineer") AND ("senior" OR "mid") AND ({stackdict[tech]}) AND ',
        # Low: Asks for the job title or professional of the tech
        "low" : f'("developer" OR "coder" OR "software engineer" OR "{tech} developer" OR "{tech} engineer") AND '
    }
    devops_b = {
        "high" : "This is a high level devops search",
        "mid" : "This is a mid level devops search",
        "low" : "This is a low level devops search"
    }
    techlead_b = {
        # High: Asks for project leadership, leadership in the technology and max seniority
        "high" : f'("techlead" OR "tech lead" OR "project management") AND ("{tech} lead" OR "{tech} leader") AND ("senior") AND ',
        # Mid: Asks for projects leadership or in the tech, asks for max or mid seniority
        "mid" : f'("techlead" OR "tech lead" OR "project management" OR "{tech} lead" OR "{tech} leader") AND ("senior" OR "mid") AND ',
        # Low: Asks for project leadership or in the tech
        "low" : f'("techlead" OR "tech lead" OR "project management" OR "{tech} lead" OR "{tech} leader") AND '
    }
    job_b = {'developer': developer_b,
           'devops': devops_b,
           'techlead':techlead_b}
           # Tobe honest, i don't have many ideas on how to vary the language search, but i'll try
    english_b = {
        "high": '("english" OR "ingles") AND ("fluent" OR "native speaker")',
        "mid": '("english" OR "ingles")',
        "low": '("english" OR "ingles")'
    }
    portuguese_b = {
        "high": '("portugues" OR "portugues") AND ("fluente" OR "nativo")',
        "mid": '("portugues" OR "portugues")',
        "low": '("portugues" OR "portugues")'
    }
    spanish_b = {
        "high": '("spanish" OR "espanhol" OR "espanol") AND ("fluido" OR "nativo")',
        "mid": '("spanish" OR "espanhol" OR "espanol")',
        "low": '("spanish" OR "espanhol" OR "espanol")'
    }
    language_b = {'english':english_b,
                'portuguese':portuguese_b,
                'spanish':spanish_b}
    boolean = tech_b[tech][level] + job_b[job][level] + language_b[language][level]
    return boolean