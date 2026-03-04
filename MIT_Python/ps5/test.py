
import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime, timedelta
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid
    def get_title(self):
        return self.title
    def get_description(self):
        return self.description
    def get_link(self):
        return self.link
    def get_pubdate(self):
        return self.pubdate

#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        Trigger.__init__(self)
        self.phrase = phrase

    def is_phrase_in(self, text):
        for i in text:
            if i in string.punctuation:
                text = text.replace(i, " ")
        l = text.split()
        for i in range(0, len(l)):
            l[i] = l[i].strip(string.punctuation)

        text = " ".join(l)
        text_lower = text.lower() + " "
        phrase_lower = self.phrase.lower() + " "
        print("text = " + text_lower)
        print("phrase = " + phrase_lower)
        if phrase_lower in text_lower:
            return True
        else:
            return False

# Problem 3

class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        if PhraseTrigger(self.phrase).is_phrase_in(story.title):
            return True
        else:
            return False


# Problem 4
#TODO: DescriptionTrigger

class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        PhraseTrigger.__init__(self, phrase)

    def evaluate(self, story):
        if PhraseTrigger(self.phrase).is_phrase_in(story.description):
            return True
        else:
            return False

# TIME TRIGGERS

# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, data):
        Trigger.__init__(self)
        a = datetime.strptime(data, "%d %b %Y %H:%M:%S")
        self.data = a


# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    def __init__(self, trigger_time):
        # TimeTrigger.__init__(self, data)
        b = datetime.strptime(trigger_time, "%d %b %Y %H:%M:%S")
        b = b.replace(tzinfo=pytz.timezone("EST"))
        self.trigger_time = b

    def evaluate(self, story):
        if story.pubdate < self.trigger_time:
            return True
        else:
            return False


class AfterTrigger(TimeTrigger):
    def __init__(self, trigger_time):
        # TimeTrigger.__init__(self, date_string)
        b = datetime.strptime(trigger_time, "%d %b %Y %H:%M:%S")
        b = b.replace(tzinfo=pytz.timezone("EST"))
        self.trigger_time = b

    def evaluate(self, story):
        if story.pubdate > self.trigger_time:
            return True
        else:
            return False


class NotTrigger(Trigger):
    def __init__(self, trigger):
        Trigger.__init__(self)
        self.trigger = trigger

    def evaluate(self, story):
        return not self.trigger.evaluate(story)


class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        Trigger.__init__(self)
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, story):
        if self.trigger1.evaluate(story) == True and self.trigger2.evaluate(story) == True:
            return True
        else:
            return False



if __name__ == '__main__':

    class TrueTrigger:
        def evaluate(self, story): return True

    class FalseTrigger:
        def evaluate(self, story): return False

    tt = TrueTrigger()
    tt2 = TrueTrigger()
    ft = FalseTrigger()
    ft2 = FalseTrigger()

    yy = AndTrigger(tt, tt2)
    yn = AndTrigger(tt, ft)
    ny = AndTrigger(ft, tt)
    nn = AndTrigger(ft, ft2)
    b = NewsStory("guid", "title", "description", "link", datetime.now())

    print(yy.evaluate(b))
    print(yn.evaluate(b))
    print(ny.evaluate(b))
    print(nn.evaluate(b))
    # self.assertFalse(yn.evaluate(b), "AND of 'always true' and 'always false' should be false")
    # self.assertFalse(ny.evaluate(b), "AND of 'always false' and 'always true' should be false")
    # self.assertFalse(nn.evaluate(b), "AND of 'always false' and 'always false' should be false")
