import jinja2

with open("template/index.template.html") as tf:
    template = jinja2.Template(tf.read())

with open("page_source/index.html", "w") as sf:
    sf.write(template.render())