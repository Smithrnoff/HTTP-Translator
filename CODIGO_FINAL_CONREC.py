from bs4 import BeautifulSoup
import translators as ts
import translators.server as tss
import regex
import os

dir = r"C:\Downloaded Web Sites\www.classcentral.com\report"
for root, dirnames, filenames in os.walk(dir):
    for filename in filenames:
        if filename.endswith('.htm') or filename.endswith('.html'):
            fullName = os.path.join(root,filename)
            print("TRANSLATING : " + fullName)
            with open(fullName,mode='r',encoding='utf-8') as source:

                soup = BeautifulSoup(source, 'html.parser')

                pat = regex.compile("(?<!</?[^>]*|&[^;]*)[a-zA-Z]")

                for i in soup.find_all(string=pat):

                    strings = list(i.strings)

                    for s in strings:

                        try:

                            SolIndex = s.find('.com')

                            if SolIndex == -1:

                                #translation_text = ts.translate_text(s,translator='google',from_language='en',to_language='hi',limit_of_length=50000)
                                translation_text = tss.translate_text(s,translator='google',from_language='en',to_language='hi',limit_of_length=50000)
                                s.replace_with(translation_text)
                
                            else:
                                s.replace_with(s)

                        except IndexError:

                            s.replace_with(s)

                        new_text = soup.prettify()
                

            with open(fullName, mode='w',encoding='utf-8') as new_file:

                new_file.write(str(new_text))
                print("TRANSLATED")
