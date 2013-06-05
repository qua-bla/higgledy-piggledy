import urllib2 as urllib
import feedparser
import logging as log

def get_by_id(arxiv_id):
    url = 'http://export.arxiv.org/api/query?id_list=' + arxiv_id
    data = urllib.urlopen(url).read()
    
    #feedparser._FeedParserMixin.namespaces['http://a9.com/-/spec/opensearch/1.1/'] = 'opensearch'
    #feedparser._FeedParserMixin.namespaces['http://arxiv.org/schemas/atom'] = 'arxiv'
    feed = feedparser.parse(data)
    
    for entry in feed.entries:
        ref = {}
        ref['author'] = ' and '.join(author.name for author in entry.authors)
        ref['title'] = entry.title
        ref['eprint'] = entry.id.split('/abs/')[-1]
        ref['date'] = entry.published[0:10]
        ref['year'] = entry.published[0:4]
        ref['month'] = entry.published[5:7]
        ref['eprintclass'] = 'cs.DS'
        ref['eprinttype'] = 'arxiv'
        ref['version'] = ref['eprint'].split('v')[-1]
        ref['url'] = entry.id
        ref['abstract'] = entry.summary

        log.info('Found `%s` by `%s`', entry['title'], entry['author'])

        ref['filename'] = ref['eprint'].replace('/', '_') + '.pdf'

        for link in entry.links:
            try:
                if link.title == 'pdf':
                    ref['downloadurl'] = link.href
            except AttributeError:
                pass

    return ref

