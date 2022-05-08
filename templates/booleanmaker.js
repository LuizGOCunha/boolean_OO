function booleanmaker(tech,job,language,level){
    var stackdict={"react": '"frontend" OR "front end"',
                "python": '"backend" OR "back end"'};
    var python_b = {
        // High: asks for python and the two biggest frameworks
        "high" : '("python" OR "phyton" OR "py" OR "py*") AND ("django") AND ("flask") AND ',
        // Medium: asks for python and one of the frameworks
        "mid" : '("python" OR "phyton" OR "py" OR "py*") AND ("django" OR "flask" OR "py*") AND ',
        // Low: asks for python or one of its frameworks
        "low" : '("python" OR "phyton" OR "py" OR "django") AND '
    }
    var react_b = {
        // High: asks for react, javascript, and one of the many other frameworks
        "high" : '("react" OR "reactjs" OR "react.js") AND ("javascript" OR "js") AND ("*js") AND ',
        // Medium: asks for react, javascript or other framework
        "mid" : '("react" OR "reactjs" OR "react.js") AND ("javascript" OR "js" OR "*js") AND ',
        // Low: asks for react or javascript or any other framework even.
        "low" : '("react" OR "reactjs" OR "react.js" OR "*js") AND ("javascript" OR "js") AND '
    }
    // Dict of all tech's and their phrases to be used in the boolean
    var tech_b = {'python':python_b,
              'react':react_b}
    var developer_b = {
        // High: Asks for the job title or a professional of the tech, max seniority or fullstack
        "high" : `("developer" OR "coder" OR "software engineer" OR "${tech} developer" OR "${tech} engineer") AND ("senior" OR "fullstack") AND `,
        // Mid: Asks for the job title or a professional of the tech, max or mid seniority, and the appropriate stack
        "mid" : `("developer" OR "coder" OR "software engineer" OR "${tech} developer" OR "${tech} engineer") AND ("senior" OR "mid" OR ${stackdict[tech]}) AND `,
        // Low: Asks for the job title or professional of the tech
        "low" : `("developer" OR "coder" OR "software engineer" OR "${tech} developer" OR "${tech} engineer") AND `
    }
    var devops_b = {
        // High: Asks for knowledge in linux servers, in cloud, in some specific cloud providers, in server deployment applications and in databases
        "high" : '("linux" OR "servers" OR "debian") AND ("cloud" OR "AWS" OR "Azure" OR "heroku") AND ("containers" OR "docker" OR "kubernetes") AND ("SQL" OR "databases") AND ',
        // Mid: Asks for knowledge in general linux server deployment, in general cloud computing and server deployment applications
        "mid" : '("linux" OR "servers" OR "debian" OR "containers" OR "docker" OR "kubernete") AND ("cloud" OR "AWS" OR "Azure" OR "heroku") AND ',
        // Low: Asks for knowledge in general deployment
        "low" : '("linux" OR "servers" OR "debian" OR "containers" OR "docker" OR "kubernete" OR "cloud" OR "AWS" OR "Azure" OR "heroku" ) AND '
    }
    var techlead_b = {
        // High: Asks for project leadership or leadership in the technology and max seniority
        "high" : `("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "${tech} lead" OR "{tech} leader") AND `,
        // Mid: Asks for projects leadership or in the tech, asks for max or mid seniority
        "mid" : `("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "${tech} lead" OR "{tech} leader") AND `,
        // Low: Asks for project leadership or in the tech
        "low" : `("techlead" OR "tech lead" OR "technical lead" OR "project management" OR "${tech} lead" OR "{tech} leader") AND `
    }
    // Dict of all jobs and their phrases to be used in the boolean
    var job_b = {'developer': developer_b,
           'devops': devops_b,
           'techlead':techlead_b}
    // To be honest, i don't have many ideas on how to vary the language search, but i'll try
    var english_b = {
        "high": '("english" OR "ingles") AND ("fluent" OR "native speaker")',
        "mid": '("english" OR "ingles")',
        "low": '("english" OR "ingles")'
    }
    var portuguese_b = {
        "high": '("portugues" OR "portugues") AND ("fluente" OR "nativo")',
        "mid": '("portugues" OR "portugues")',
        "low": '("portugues" OR "portugues")'
    }
    var spanish_b = {
        "high": '("spanish" OR "espanhol" OR "espanol") AND ("fluido" OR "nativo")',
        "mid": '("spanish" OR "espanhol" OR "espanol")',
        "low": '("spanish" OR "espanhol" OR "espanol")'
    }
    // Dict of all languages and their phrases to be used in the boolean
    var language_b = {'english':english_b,
                'portuguese':portuguese_b,
                'spanish':spanish_b}
    var boolean = tech_b[tech][level] + job_b[job][level] + language_b[language][level]
    return boolean;
    }

