"""
"""
from collections import defaultdict

from pelican import signals
from pelican.contents import Content, Article, Tag

def _new_tag(tag_text, article, global_tags):
    """
    Given the TAG_TEXT, an ARTICLE it applies to, and the defaultdict
    of GLOBAL_TAGS, add the relevant tags.

    Returns the Tag(...) for TAG_TEXT.
    """
    tag = Tag(tag_text, article.settings)
    tags = getattr(article, 'tags', [])
    tags.append(tag)
    article.tags = list(set(tags))
    global_tags[tag].append(article)

    return tag

def add_tags(content):
    """
    Create tags for our content.

    For each standard article, create tags for
    * default key
    * form
    * time signature
    * n composers
    * style

    Create lists of all of these on the global content object
    """
    global_tags = content.tags

    for article in content.articles:

        for metatag in ['key', 'form', 'time', 'composer', 'style']:

            if not getattr(content, metatag, False):
                setattr(content, metatag, set())

            if getattr(article, metatag, False):
                if metatag in ['composer']: # Multi tag
                    as_tags = []
                    for tag_text in getattr(article, metatag).split(','):
                        tag = _new_tag(tag_text, article, global_tags)
                        as_tags.append(tag)
                        getattr(content, metatag).add(tag)
                        setattr(article, metatag, as_tags)
                else:
                    tag = _new_tag(getattr(article, metatag), article, global_tags)
                    setattr(article, metatag, tag)
                    getattr(content, metatag).add(tag) # Add to our global list



    content.tags = global_tags

def register():
    signals.article_generator_finalized.connect(add_tags)
