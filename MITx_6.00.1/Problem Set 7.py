class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()    
    def isWordIn(self, text):
        text = self.replacePunctuation(text)
        cleaned = text.lower().split()
        return self.word in cleaned
    def replacePunctuation(self, text):
        import string
        for p in string.punctuation:
            text = text.replace(p, ' ')
        return text
        
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

class PhraseTrigger(Trigger):
 
    def __init__(self, phrase):
        self.phrase = phrase
 
    def isPhraseIn(self,text):
        return self.phrase in text
 
    def evaluate(self, story):
        if self.isPhraseIn(story.getTitle()):
            return True
        if self.isPhraseIn(story.getSummary()):
            return True
        if self.isPhraseIn(story.getSubject()):
            return True
        return False



class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()    
    def isWordIn(self, text):
        text = self.replacePunctuation(text)
        cleaned = text.lower().split()
        return self.word in cleaned
    def replacePunctuation(self, text):
        import string
        for p in string.punctuation:
            text = text.replace(p, ' ')
        return text
        
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getTitle())
        
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSubject())

class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        return self.isWordIn(story.getSummary())

class PhraseTrigger(Trigger):
 
    def __init__(self, phrase):
        self.phrase = phrase
 
    def isPhraseIn(self,text):
        return self.phrase in text
 
    def evaluate(self, story):
        if self.isPhraseIn(story.getTitle()):
            return True
        if self.isPhraseIn(story.getSummary()):
            return True
        if self.isPhraseIn(story.getSubject()):
            return True
        return False

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    results = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story) is True:
                results.append(story)
                break  
    
    return results    



def makeTrigger(triggerMap, triggerType, params, name):
    trigger = None

    if triggerType == "TITLE":
        trigger = TitleTrigger(params[0])
    elif triggerType == "SUBJECT":
        trigger = SubjectTrigger(params[0])
    elif triggerType == "SUMMARY":
        trigger = SummaryTrigger(params[0])
    elif triggerType == "NOT":
        trigger = NotTrigger(triggerMap[params[0]])
    elif triggerType == "AND":
        trigger = AndTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "OR":
        trigger = OrTrigger(triggerMap[params[0]], triggerMap[params[1]])
    elif triggerType == "PHRASE":
        trigger = PhraseTrigger(" ".join(params))

    triggerMap[name] = trigger
    return trigger





































