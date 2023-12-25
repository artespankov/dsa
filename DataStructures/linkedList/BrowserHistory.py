# LL-based browser history design


class PageNode:
    def __init__(self, url: str, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev


class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = PageNode(homepage)
        self.current_page = self.homepage

    def visit(self, url: str) -> None:
        visited_page = PageNode(url, prev=self.current_page)
        self.current_page.next = visited_page
        self.current_page = visited_page

    def back(self, steps: int) -> str:
        history_page = self.current_page
        while steps and history_page.prev:
            history_page = history_page.prev
            steps -= 1
        self.current_page = history_page
        return self.current_page.url

    def forward(self, steps: int) -> str:
        history_page = self.current_page
        while steps and history_page.next:
            history_page = history_page.next
            steps -= 1
        self.current_page = history_page
        return self.current_page.url

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# TEST cases

# INPUT
# ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
# [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]

# OUTPUT:
# [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

# EXPLANATION:
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"