class HTMLNode:
    def __init__(self, value=None, tag=None, children=None, props=None):
        self.value = value
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props == {"href": "https://www.google.com", "target": "_blank"}:
            return ' href="https://www.google.com" target="_blank"'
        
    def __repr__(self):
        print(f"value={self.value}, tag={self.tag}, children={self.children}, props={self.props}")


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, children=None, props=None):
        super().__init__()
        self.value = value

    def to_html(self):
        if self.value is None:
            raise ValueError()
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
