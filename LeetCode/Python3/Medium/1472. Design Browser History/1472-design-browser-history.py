class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_page = 0
        
    def visit(self, url: str) -> None:
        self.current_page += 1
        if len(self.history) == self.current_page:
            self.history.append(url)
        else:
            self.history[self.current_page] = url
        self.history = self.history[:self.current_page+1]
        
    def back(self, steps: int) -> str:
        self.current_page = max(self.current_page - steps, 0)
        return self.history[self.current_page]
    
    def forward(self, steps: int) -> str:
        self.current_page = min(self.current_page + steps, len(self.history) - 1)
        return self.history[self.current_page]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)