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
    
    def __eq__ (self, tn):
        if (self.tag == tn.tag and
            self.value == tn.value and
            self.children == tn.children and
            self.props == tn.props):
            return True
        return False
    
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
        child_str = ""
        for child in self.children:
            if isinstance(child, LeafNode): #if LeafNode, return the html of that instance
                child_str += f"{child.to_html()}"           
            elif isinstance(child, ParentNode): #if ParentNode, go a level deeper then apply tags
                child_str = child.to_html()
            else:
                raise Exception("not sure what happened... neither ParentNode nor LeafNode detected")
        return f"<{self.tag}>{child_str}</{self.tag}>"

    