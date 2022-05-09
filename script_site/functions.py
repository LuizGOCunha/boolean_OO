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




def booleanmaker(tech1,tech2,job,language,level):
    # Turns level into integer so i can alter it as necessary without too much hassle
    level = int(level)
    # Instantiate the tech variable, so i can create the dicts without unassignement errors
    tech = ""
    # Create stack variable that will also be used in the dict, default value will lead to fullstack option
    stack = ""
    stackdict={"react": 'OR "frontend" OR "front end"',
                "python": 'OR "backend" OR "back end"',
                "": ' OR "fullstack"'}
    python_b = {
        # High: asks for python and the two biggest frameworks
        3 : '("python" OR "phyton" OR "py" OR "py*") AND ("django") AND ("flask") AND ',
        # Medium: asks for python and one of the frameworks
        2 : '("python" OR "phyton" OR "py" OR "py*") AND ("django" OR "flask" OR "py*") AND ',
        # Low: asks for python or one of its frameworks
        1 : '("python" OR "phyton" OR "py" OR "django") AND ',
        # Lowest (in case it's low level multiple tech search): asks for anything python
        0 : '("python" OR "phyton" OR "py" OR "py*" OR "django") AND '
    }
    react_b = {
        # High: asks for react, javascript, and one of the many other frameworks
        3 : '("react" OR "reactjs" OR "react.js") AND ("javascript" OR "js") AND ("*js") AND ',
        # Medium: asks for react, javascript or other framework
        2 : '("react" OR "reactjs" OR "react.js") AND ("javascript" OR "js" OR "*js") AND ',
        # Low: asks for react or javascript or any other framework even.
        1 : '("react" OR "reactjs" OR "react.js" OR "*js") AND ("javascript" OR "js") AND ',
        # Lowest: asks for anything react.
        0 : '("react" OR "reactjs" OR "react.js" OR "*js") AND'
    }
    # Dict of all tech's and their phrases to be used in the boolean
    tech_b = {'python':python_b,
              'react':react_b}
    developer_b = {
        # High: Asks for the job title or a professional of the tech, max seniority or fullstack
        3 : f'("developer" OR "coder" OR "software engineer" OR "{tech} developer" OR "{tech} engineer") AND ("senior" OR "fullstack") AND ',
        # Mid: Asks for the job title or a professional of the tech, max or mid seniority, and the appropriate stack
        2 : f'("developer" OR "coder" OR "software engineer" OR "{tech} developer" OR "{tech} engineer") AND ("senior" OR "mid" {stackdict[stack]}) AND ',
        # Low: Asks for the job title or professional of the tech
        1 : f'("developer" OR "coder" OR "software engineer" OR "{tech} developer" OR "{tech} engineer") AND '
    }
    devops_b = {
        # High: Asks for knowledge in linux servers, in cloud, in some specific cloud providers, in server deployment applications and in databases
        3 : '("linux" OR "servers" OR "debian") AND ("cloud" OR "AWS" OR "Azure" OR "heroku") AND ("containers" OR "docker" OR "kubernetes") AND ("SQL" OR "databases") AND ',
        # Mid: Asks for knowledge in general linux server deployment, in general cloud computing and server deployment applications
        2 : '("linux" OR "servers" OR "debian" OR "containers" OR "docker" OR "kubernete") AND ("cloud" OR "AWS" OR "Azure" OR "heroku") AND ',
        # Low: Asks for knowledge in general deployment
        1 : '("linux" OR "servers" OR "debian" OR "containers" OR "docker" OR "kubernete" OR "cloud" OR "AWS" OR "Azure" OR "heroku" ) AND '
    }
    techlead_b = {
        # High: Asks for project leadership or leadership in the technology and max seniority
        3 : f'("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "{tech} lead" OR "{tech} leader") AND ',
        # Mid: Asks for projects leadership or in the tech, asks for max or mid seniority
        2 : f'("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "{tech} lead" OR "{tech} leader") AND ',
        # Low: Asks for project leadership or in the tech
        1 : f'("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "{tech} lead" OR "{tech} leader") AND '
    }
    # Dict of all jobs and their phrases to be used in the boolean
    job_b = {'developer': developer_b,
           'devops': devops_b,
           'techlead':techlead_b}
           # Tobe honest, i don't have many ideas on how to vary the language search
    english_b = {
        3: '("english" OR "ingles")',
        2: '("english" OR "ingles")',
        1: '("english" OR "ingles")'
    }
    portuguese_b = {
        3: '("portugues" OR "portugues")',
        2: '("portugues" OR "portugues")',
        1: '("portugues" OR "portugues")'
    }
    spanish_b = {
        3: '("spanish" OR "espanhol" OR "espanol")',
        2: '("spanish" OR "espanhol" OR "espanol")',
        1: '("spanish" OR "espanhol" OR "espanol")'
    }
    # Dict of all languages and their phrases to be used in the boolean
    language_b = {'english':english_b,
                'portuguese':portuguese_b,
                'spanish':spanish_b}
    if tech1 and tech2:
        # Here i am lowering the level because if i just look for 2 techs in high level it will bring back very few people.
        level = level-1
        tech = tech1
        boolean = tech_b[tech1][level] 
        tech = tech2
        boolean = boolean + tech_b[tech2][level] 
        # Here i will increase the level once more because the job and language parameters don't suffer from the same problems
        level = level+1
        boolean = boolean + job_b[job][level] + language_b[language][level]
    elif tech1:
        tech = tech1
        boolean = tech_b[tech][level] + job_b[job][level] + language_b[language][level]
    elif tech2:
        tech = tech2
        boolean = tech_b[tech][level] + job_b[job][level] + language_b[language][level]
    else:
        boolean = job_b[job][level] + language_b[language][level]
    return boolean