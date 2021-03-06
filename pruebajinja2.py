#! usr/bin/pytonh3

import os
import jinja2

CONFIG_PATH = os.getcwd()  # set this to your local needs.

# override the values with job context 
job_ctx = {
    "uboot_error_messages": [
        'NO BOOTLOADER FOUND',
        'NOT ENOUGH MEMORY SPACE'
    ],
    "connection_tags": {
        "serial" : ['tag1',
                    'tag2',
                    'tag3'
        ]
    },
    "connection_commands": {
        "serial": "serial-command",
        "ssh": "ssh-command"
    },
    "connection_list":[
        'serial',
        'ssh'
    ]
}

# estas lineas de codigo se emplean para cargar el template y los templates de los quejoffdf hereda
# en la variable emv, en concreto dentro del metodo get_template se tiene el template 
with open("mibase.jinja2", "r") as details:
    data = details.read()
    string_loader = jinja2.DictLoader({"mibase.jinja2": data})
type_loader = jinja2.FileSystemLoader([CONFIG_PATH])
env = jinja2.Environment(  # nosec - YAML, not HTML, no XSS scope.
    loader=jinja2.ChoiceLoader([string_loader, type_loader]),
    trim_blocks=True,
    autoescape=False,
)

definition_template = env.get_template("mibase.jinja2")
#render with the job context
print(definition_template.render(job_ctx))
