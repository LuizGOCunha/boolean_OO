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
        # High: asks for python and the two biggest frameworks
        "high" : '("python" OR "phyton" OR "py" OR "py*") AND ("django") AND ("flask") AND ',
        # Medium: asks for python and one of the frameworks
        "mid" : '("python" OR "phyton" OR "py" OR "py*") AND ("django" OR "flask" OR "py*") AND ',
        # Low: asks for python or one of its frameworks
        "low" : '("python" OR "phyton" OR "py" OR "django") AND '
    }
    react_b = {
        # High: asks for react, javascript, and one of the many other frameworks
        "high" : '("react" OR "reactjs" OR "react.js") AND ("javascript" OR "js") AND ("*js") AND ',
        # Medium: asks for react, javascript or other framework
        "mid" : '("react" OR "reactjs" OR "react.js") AND ("javascript" OR "js" OR "*js") AND ',
        # Low: asks for react or javascript or any other framework even.
        "low" : '("react" OR "reactjs" OR "react.js" OR "*js") AND ("javascript" OR "js") AND '
    }
    # Dict of all tech's and their phrases to be used in the boolean
    tech_b = {'python':python_b,
              'react':react_b}
    developer_b = {
        # High: Asks for the job title or a professional of the tech, max seniority or fullstack
        "high" : f'("developer" OR "coder" OR "software engineer" OR "{tech} developer" OR "{tech} engineer") AND ("senior" OR "fullstack") AND ',
        # Mid: Asks for the job title or a professional of the tech, max or mid seniority, and the appropriate stack
        "mid" : f'("developer" OR "coder" OR "software engineer" OR "{tech} developer" OR "{tech} engineer") AND ("senior" OR "mid" OR {stackdict[tech]}) AND ',
        # Low: Asks for the job title or professional of the tech
        "low" : f'("developer" OR "coder" OR "software engineer" OR "{tech} developer" OR "{tech} engineer") AND '
    }
    devops_b = {
        # High: Asks for knowledge in linux servers, in cloud, in some specific cloud providers, in server deployment applications and in databases
        "high" : '("linux" OR "servers" OR "debian") AND ("cloud" OR "AWS" OR "Azure" OR "heroku") AND ("containers" OR "docker" OR "kubernetes") AND ("SQL" OR "databases") AND ',
        # Mid: Asks for knowledge in general linux server deployment, in general cloud computing and server deployment applications
        "mid" : '("linux" OR "servers" OR "debian" OR "containers" OR "docker" OR "kubernete") AND ("cloud" OR "AWS" OR "Azure" OR "heroku") AND ',
        # Low: Asks for knowledge in general deployment
        "low" : '("linux" OR "servers" OR "debian" OR "containers" OR "docker" OR "kubernete" OR "cloud" OR "AWS" OR "Azure" OR "heroku" ) AND '
    }
    techlead_b = {
        # High: Asks for project leadership or leadership in the technology and max seniority
        "high" : f'("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "{tech} lead" OR "{tech} leader") AND ',
        # Mid: Asks for projects leadership or in the tech, asks for max or mid seniority
        "mid" : f'("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "{tech} lead" OR "{tech} leader") AND ',
        # Low: Asks for project leadership or in the tech
        "low" : f'("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "{tech} lead" OR "{tech} leader") AND '
    }
    # Dict of all jobs and their phrases to be used in the boolean
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
    # Dict of all languages and their phrases to be used in the boolean
    language_b = {'english':english_b,
                'portuguese':portuguese_b,
                'spanish':spanish_b}
    # This is taking into consideration that they would be searching for devops without tech, but now they're searching devops+tech, so...
    # if job == 'devops':
    #     boolean = job_b[job][level] + language_b[language][level]
    # else: 
    boolean = tech_b[tech][level] + job_b[job][level] + language_b[language][level]
    return boolean