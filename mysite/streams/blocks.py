"""Streamfields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else"""

    title = blocks.CharBlock(required=True, help_text='Add your title')
    text = blocks.TextBlock(required=True, help_text='Add additional text')

    class Meta: #noqa
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)"""
    
    title = blocks.CharBlock(required=True, help_text="Add your title")
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If ButtonPage: It will be used first")),

            ]
        )
    )

    class Meta: #noqa
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Staff Cards"

class RichTextBlock(blocks.RichTextBlock):
    """RichText with all the features"""

    class Meta: #noqa
        template = "streams/richtext_block.html"
        icon = "doc-full"
        label = "Full RichText"

class SimpleRichTextBlock(blocks.RichTextBlock):
    """RichText without (limited) all the features"""

    def __init__(self, required=True, help_text=None, editor='default', features=None, validators=(), **kwargs):
        super().__init__(**kwargs) # run the default first
        self.features = [          # now override the features
            "bold",
            "italic",
            "link",
        ]
        
    class Meta: #noqa
        template = "streams/simple_richtext_block.html"
        icon = "edit"
        label = "Simple RichText"

class CTABlock(blocks.StructBlock):
    """A simple call to action section."""
    title = blocks.CharBlock(requried=True, max_length=60)
    text = blocks.RichTextBlock(required=True, features=["bold", "italic"])
    button_page = blocks.PageChooserBlock(required=False)
    button_url = blocks.URLBlock(required=False)
    button_text = blocks.CharBlock(required=True, default='Learn More', max_length=40)

    class Meta: #noqa
        template = "streams/cta_block.html"
        icon = "placeholder"
        label = "Call to action"