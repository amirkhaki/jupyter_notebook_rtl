#!/usr/bin/env python3

import sys
import json
import nbformat

if len(sys.argv) < 3:
    print("usage: python3 ./main.py /path/to/notebook.ipynb /path/to/out.ipynb")

ntbk = sys.argv[1]
rtl = sys.argv[2]
NBFORMAT_VERSION=4

ntbk = nbformat.read(ntbk, NBFORMAT_VERSION)
begin = "<div class=\"override-text-align\" dir=\"rtl\">  \n\n"
end = "\n</div>"
for cell in ntbk.cells:
    if cell['cell_type'] != 'markdown':
        continue
    if cell['metadata'].get('direction', None) != 'rtl':
        continue
    cell.source = begin+cell.source
    cell.source += end
loving_js = '''%%js
var style=document.createElement('style');
style.type='text/css';
style.appendChild(document.createTextNode('.override-text-align p {text-align: right;}'));
document.getElementsByTagName('head')[0].appendChild(style);
'''
jsout = '''{
      "application/javascript": [
       "var style=document.createElement('style');\\n",
       "style.type='text/css';\\n",
       "style.appendChild(document.createTextNode('.override-text-align p {text-align: right;}'));\\n",
       "document.getElementsByTagName('head')[0].appendChild(style);\\n"
      ],
      "text/plain": [
       "<IPython.core.display.Javascript object>"
      ]
     }'''
jsout = json.loads(jsout)
jsout = nbformat.v4.new_output("display_data", data=jsout)
jscell = nbformat.v4.new_code_cell(source=loving_js, outputs=[jsout])
ntbk.cells.append(jscell)
nbformat.write(ntbk, rtl)
