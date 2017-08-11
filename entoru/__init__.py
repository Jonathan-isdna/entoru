# entoru - Single word English-Russian translation
# Copyright (C) <year>  <name of author>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import requests
from bs4 import BeautifulSoup

# Translate english to russian
def translate(word):
    # Gets webpage
    url = "http://context.reverso.net/translation/english-russian/" + word
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r.raise_for_status()

    # Decodes raw material
    # requests package doesn't seem to do it right....
    s = (r.content).decode(r.encoding)

    # parse for FIRST translation on webpage
    soup = BeautifulSoup(s, "html.parser")
    result = soup.find("span", attrs={"class":"entry", "dir":" ltr "})
    return result.text
