#Create html from string

class String:
    def __init__(self):
        pass

    def html(self,str1):
        import logging
        logging.basicConfig(filename=f"{str1}.html",filemode='x',level=logging.INFO)
        logging.info(f'''
        <html>
            <head>
            </head>
            <body>
                {str1}
            </body>
        </html>''')


string1=String()
string1.html("abhi")