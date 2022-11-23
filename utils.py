

def read_html(filename):
    my_file = "html_views/" + filename
    html = ''
    try:
        f = open(my_file, 'r')
        for line in f.readlines():
            html += line
            html += "\n"
        f.close()
    except:
        html += '<h1>File was not found.</h1>'
    finally:
        return html
