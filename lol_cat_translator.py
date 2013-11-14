import re
import random
# possible additions
# o --> oo
class LolCatTranslator(object):

    def __init__(self, trans_file="lolcatwords.csv"):
        self.trans_dict = {}
        with open(trans_file) as f:
            f = f.read().split("\n")
            for row in f:
                word, trans = row.split(",")
                self.trans_dict[word] = trans
        self.endings = {"i": ["ai"], "er": ["ah", "r"], "le": ["ul", "el"], "y": ["eh", "ah"], "ing": ["in"], "th": ["f"], "ight": ["ite", "iet"]}

    def translate_word(self, word):
        if word in self.trans_dict:
            return self.trans_dict[word]
        for ending in self.endings:
            if word.endswith(ending):
                word = word[:-len(ending)] + random.choice(self.endings[ending])
        # ends in [const]e --> e[const]
        if re.search("\w+[aeiou][^aeiou]e$", word) is not None and len(word) > 3:
            word = word[:-2] + word[-1] + word[-2]
        # vowel u --> vowel w
        if re.search("\w+[aeiou]u\w+", word) is not None:
            word = word.replace("u", "w")
        # starts with th --> t
        if word.startswith("th"):
            word = "t" + word[2:]
        # th in middle --> tt, dd, or f
        if re.search("\w+th\w+\w", word) is not None:
            word = word.replace("th", random.choice(["tt","dd","f"]))
        # adds s to end of some words
        if not word.endswith('s') and len(word) > 3 and random.random() > 0.8:
            word += 's'
        # ends in s --> z if random > 0.6 and word length > 3
        if re.search("\w+[^s]s$", word) is not None and len(word) > 3 and random.random() > 0.6:
            word = word[:-1] + "z"

        return word

    def translate_message(self, msg):
        msg = msg.replace("I am", "Iz")
        msg = msg.replace("I'm", "Iz")
        msg = msg.replace("a ", "")
        words = re.findall("\w+", msg)
        for word in words:
            msg = msg.replace(word, self.translate_word(word))
        if words[0].lower == "can":
            subject = words[1]
            msg = message.replace(word[0] + " " + word[1], word[1].title() + " can")
        if msg.endswith("!"):
            msg = msg + "!" * random.randint(1,5) + "1"
        # sometimes add srsly to the end of msg
        if random.random() > 0.9:
            msg = msg + " srsly."
        return msg

def test():
    t = LolCatTranslator()
    words = ["they", "hi", "hello","little", "night", "nothing", "the","this","cloud","laud","came","earths"]
    for word in words:
        print t.translate_word(word)
    print t.translate_message("I am so tired!")
    print t.translate_message("How are you? I'm fine.")
