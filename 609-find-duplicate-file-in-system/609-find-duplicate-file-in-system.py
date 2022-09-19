class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dict_ = {}
        output = []
        for i in range(len(paths)):
            sp_lst = paths[i].split()
            for j in range(1,len(sp_lst)):
                root = sp_lst[0] + "/"
                idx = sp_lst[j].index("(")
                if sp_lst[j][idx+1:-1] in dict_.keys():
                    dict_[sp_lst[j][idx+1:-1]] +=  "*" + root + sp_lst[j][:idx]
                else:
                    dict_[sp_lst[j][idx+1:-1]] = root + sp_lst[j][:idx]
        for i in dict_.values():
            if "*" in i:
                output.append(i.split("*"))
        return output