
def link(url, text, new_tab = None):
    """Converts a url and text into a html link
    """
    if new_tab:
        link = '<a href="{url}" target="_blank">{text}</a>'.format(url=url, text=text)
    else:
        
        link = '<a href="{url}">{text}</a>'.format(url=url, text=text)
    return link
