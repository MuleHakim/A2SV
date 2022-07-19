class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        for i in range(len(emails)):
            index = emails[i].index("@")
            if "+" in emails[i]:
                index1 = emails[i].index("+")
                emails[i] = emails[i].replace(emails[i][index1:index],"")
            index = emails[i].index("@")
            if "." in emails[i][:index]:
                emails[i] = emails[i][:index].replace(".","") + emails[i][index:]
        output = list(set(emails))
        return len(output)