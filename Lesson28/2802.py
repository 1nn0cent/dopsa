class Button:
    def __init__(self):
        self.clicks = 0
 
    def click(self):
        self.clicks += 1
 
    def reset(self):
        self.clicks = 0
 
    def click_count(self):
        return self.clicks
    
if __name__ == "__main__":
    bigbutton = Button()
    bigbutton.click()
    bigbutton.click()
    bigbutton.click()
    bigbutton.click()
    print(bigbutton.click_count())
    bigbutton.reset()
    bigbutton.click()
    print(bigbutton.click_count())
    