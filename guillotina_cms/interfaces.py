# -*- encoding: utf-8 -*-
from zope.interface import Interface
from guillotina.schema.interfaces import IObject
from guillotina import schema


class ICMSLayer(Interface):
    """Marker interface layer Plone.CMS."""


class IRichTextField(IObject):
    """Rich text field"""


class IRichTextFieldSchema(Interface):
    """Rich text field schema"""
    content_type = schema.ASCII(
        title='Content type'
    )
    data = schema.Text(
        title='Real data'
    )
    encoding = schema.ASCII(
        title='Get the real encoding'
    )


# Components for REST API


class IObjectWorkflow(Interface):
    pass
