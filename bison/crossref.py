import urllib2 as urllib
from lxml import etree
import logging as log
import requests
from xml.dom import minidom
 
def content(parent, tags=[]):
    try:
        return tag(parent, tags).firstChild.data.encode('utf-8')
    except:
        return None 

def tag(parent, tags = []):
    if len(tags) == 0:
        return parent
    else:
        try:
            return tag(parent.getElementsByTagName(tags[0])[0], tags[1:])
        except:
            return None

def get_by_id(doi, crossref_key):
    res = { 'doi' : doi, 'reference_type' : 'Article' }
 
    url = 'http://www.crossref.org/openurl/?id=doi:'+doi+'&noredirect=true&pid='+crossref_key+'&format=unixref'
    log.debug('Retriving URL <%s>', url)
    f = urllib.urlopen(url)
    xml = minidom.parse(f)
 
    journal = tag(xml, ['doi_records','doi_record','crossref','journal'])
 
    res['journal'] = content(journal, ['journal_metadata','abbrev_title'])

    res['year'] = content(journal, ['journal_issue','publication_date','year'])
    res['month'] = content(journal, ['journal_issue','publication_date','month'])
    res['issue'] = content(journal, ['journal_issue','issue'])
    res['volume'] = content(journal, ['journal_issue','journal_volume', 'volume'])
 
    res['title'] = content(journal, ['journal_article','titles','title'])
 
    authors = []
    contributors = tag(journal, ['journal_article', 'contributors'])
    for name in contributors.getElementsByTagName('person_name'):
        given_name = content(name, ['given_name'])
        surname = content(name, ['surname'])
        authors.append('{0} {{{1}}}'.format(given_name, surname))

    res['author'] = ' and '.join(authors)
 
    first_page = content(journal, ['journal_article','pages','first_page'])
    last_page = content(journal, ['journal_article','pages','last_page'])
    if last_page != None:
        res['pages'] = '{0}--{1}'.format(first_page, last_page)
    else:
        res['pages'] = first_page

    """ PhysRev new format """
    item_number = content(journal, ['publisher_item','item_number'])
    if res['pages'] == None:
        res['pages'] = item_number
    else:
        log.warn('key clash between pages and item_numer')
        res['item_numer'] = item_number

    res['url'] = 'http://dx.doi.org/{res[doi]}'.format(res=res)
    
    urlfind = requests.get(res['url'])
    url = urlfind.url
    if '.aps.org/abstract/' in url:
        res['downloadurl'] = url.replace('/abstract/', '/pdf/')
        res['filename'] = res['doi'].split('/')[-1] + '.pdf'
    if '10.1016' in doi:
        try:
            tree = etree.HTML(urlfind.text)
            res['downloadurl'] = tree.xpath('//a[@id="pdfLink"]')[0].get('href')
            res['filename'] = res['doi'].split('/')[-1] + '.pdf'
        except:
            pass

    res['citekey'] = res['doi'].split('/')[-1]
    del res['url']

    return res

