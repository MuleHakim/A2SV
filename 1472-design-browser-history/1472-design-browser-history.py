class BrowserHistory:

    def __init__(self, homepage: str):
        self.urls = [homepage]
        self.idx = 0
        self.upperbound = 0

    def visit(self, url: str) -> None:
        if self.idx == len(self.urls) - 1:
            self.urls.append(url)
            self.idx += 1
        else:
            self.idx += 1
            self.urls[self.idx] = url
        self.upperbound = self.idx

    def back(self, steps: int) -> str:
        self.idx = max(0, self.idx-steps)
        return self.urls[self.idx]

    def forward(self, steps: int) -> str:
        self.idx = min(self.idx+steps, self.upperbound)
        return self.urls[self.idx]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)