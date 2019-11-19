import re

def KeyWordMatch(start_word,end_word,trial_text):
    try:
        try:
            matched_text = re.search(r'{}(.*?){}'.format(start_word,end_word),trial_text).group(1)
        except AttributeError:
            matched_text = re.search(r'{}(.*?)$'.format(start_word),trial_text).group(1)
        matched_text = matched_text.lstrip()
        matched_text = matched_text.replace('?','')
    except AttributeError:
        matched_text = 'Not Specified'
    
    return matched_text