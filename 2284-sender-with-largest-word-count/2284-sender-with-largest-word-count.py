class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        dict_ = {}
        for i in range(len(messages)):
            if senders[i] in dict_.keys():
                dict_[senders[i]] += messages[i].count(" ") + 1
            else:
                dict_[senders[i]] = messages[i].count(" ") + 1
        result = ""       
        count = max(dict_.values())
        senders = list(set(senders))
        for i in range(len(senders)):
            if dict_[senders[i]]==count and senders[i]>result:
                result = senders[i]
        return result