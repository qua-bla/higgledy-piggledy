from lxml import etree

def value(tree, key):
    try:
        return tree.xpath('//meta[@name="' + key + '"]')[0].get('content')
    except:
        return None

def get_by_content(html_content):
    ref = {}

    tree = etree.HTML(html_content)
    ref['doi'] = value(tree, 'citation_doi')
    ref['journal'] value(tree, 'citation_journal_title')

    return ref
