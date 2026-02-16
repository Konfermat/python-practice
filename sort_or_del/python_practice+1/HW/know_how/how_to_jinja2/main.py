from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader

def render_template(template_name, context={}):
    template = template_env.get_template(template_name)
    return template.render(context).encode('utf-8')

def demo1():
    env = Environment(
        loader=PackageLoader('main'), 
        autoescape=select_autoescape()
        )
        
    template = env.get_template('mytemplate.html')

    print(template.render(the='variables', go='here'))

def demo2():        
    env = Environment(
        loader=FileSystemLoader('templates')
    )

    var1 = 'There was a "the" here'
    var2 = 'There was a "org" here'

    context = {'the': var1, 'org': var2}
    template = env.get_template('mytemplate.html')
    html_content = template.render(context)

    print(str(html_content))
    