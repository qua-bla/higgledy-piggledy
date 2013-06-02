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
        entry['eprint'] = entry.id.split('/abs/')[-1]
        entry['date'] = entry.published[0:10]
        entry['author'] = ' and '.join(author.name for author in entry.authors)
        entry['eprintclass'] = 'cs.DS'
        entry['eprinttype'] = 'arxiv'
        entry['version'] = entry['eprint'].split('v')[-1]
        entry['url'] = entry.id
        entry['abstract'] = entry.summary

        log.info('Found `%s` by `%s`', entry['title'], entry['author'])

        entry['filename'] = entry['eprint'].replace('/', '_') + '.pdf'

        for link in entry.links:
            try:
                if link.title == 'pdf':
                    entry['downloadurl'] = link.href
            except AttributeError:
                pass

    return entry
