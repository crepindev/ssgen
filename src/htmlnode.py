class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            props_str = ""
            for key in self.props:
                key_value = self.props[key]
                props_str += f' {key}="{key_value}"'
            return props_str
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, props=props)

    def to_html(self):
        if self.value is None:
            raise ValueError("no value provided")
        elif self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        

class ParentNode(HTMLNode):
    def __init__(self, tag=None, children=None, props=None):
        super().__init__(tag=tag, children=children, props=props)
        if self.tag is None:
            raise ValueError("no tag provided")
        elif self.children is None:
            raise ValueError("no children provided")
    
    def to_html(self):
        parent_tag_open = f"<{self.tag}>"
        parent_tag_close = f"</{self.tag}>"
        child_str = ""
        for child in self.children:
            if child.children is None:
                child_str += f"{child.to_html()}"             
            else:
                child.to_html()
        print(f"DEBUG >>> {parent_tag_open}{child_str}{parent_tag_close}")
        return f"{parent_tag_open}{child_str}{parent_tag_close}"
    