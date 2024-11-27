# generate_page.py
#
# Use jinja2 to load templates, then generate a single index.html file in the
# page_source directory

import jinja2
import json

with open("portfolio_data/index.template.html") as tf:
    template = jinja2.Template(tf.read())

with open("portfolio_data/static.json") as sf:
    static_data = json.load(sf)

page_data = {
        "static": static_data,
        }

with open("portfolio_website/index.html", "w") as sf:
    sf.write(template.render(**page_data))
