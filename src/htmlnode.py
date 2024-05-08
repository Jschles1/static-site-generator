class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        attrs = []
        for item in self.props.items():
            attrs.append(f'{item[0]}="{item[1]}"')
        return " ".join(attrs)

    def __repr__(self) -> str:
        print("HTML Node:")
        print(f"Tag: {self.tag}")
        print(f"Value: {self.value}")
        print(f"Props: {self.props}")


class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        if self.tag == None:
            return self.value

        opening_tag = f"<{self.tag}"
        if self.props:
            opening_tag = opening_tag + " " + self.props_to_html() + ">"
        else:
            opening_tag = opening_tag + ">"
        closing_tag = f"</{self.tag}>"

        return f"{opening_tag}{self.value}{closing_tag}"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("No tag provided")
        if len(self.children) == 0:
            raise ValueError("No children provided")

        opening_tag = f"<{self.tag}"
        if self.props:
            opening_tag = opening_tag + " " + self.props_to_html() + ">"
        else:
            opening_tag = opening_tag + ">"
        closing_tag = f"</{self.tag}>"

        children_nodes = "".join(
            list(map(lambda node: node.to_html(), self.children)))

        return f"{opening_tag}{children_nodes}{closing_tag}"
