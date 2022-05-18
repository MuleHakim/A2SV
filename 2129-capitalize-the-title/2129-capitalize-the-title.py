class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.split()
        result = ""
        i = 0
        while i<len(title):
            if len(title[i])<3:
                w = title[i].lower()
                result += w
                result += " "
            else:
                w = title[i].lower()
                w = w.capitalize()
                result += w
                result += " "
            i += 1
        return result.strip()