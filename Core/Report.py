def plug_in():
    html_text = """
        <!DOCTYPE html>
        <html>
            <head>
                <title>Page Title</title>
            </head>
            <body>
                <h1>This is a Heading</h1>
                <p>This is a paragraph.</p>
            </body>
        </html>
    """
    with open('html_file.html', 'w') as html_file:
        html_file.write(html_text)