from sgmllib import SGMLParser

class Html_Filter(SGMLParser):
    def reset(self):
        SGMLParser.reset(self)
        self.images = []
        self.divs = []

    def start_meta(self, attrs):
        img = [v for k, v in attrs if k=='content' and v.find('image.slidesharecdn.com')>0]
        if img:
            self.images.extend(img)

    def start_div(self, attrs):
        div = [v for k, v in attrs if k=='data-index']
        if div:
            self.divs.extend(div)

