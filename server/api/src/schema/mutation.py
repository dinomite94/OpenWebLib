import graphene
from . import db_types
from graphene_sqlalchemy import SQLAlchemyObjectType
from .query import Document

class CreateDocument(graphene.Mutation):
    class Arguments:
        title = graphene.String(description="Document title")

    ok = graphene.Boolean()
    document = graphene.Field(lambda: Document)

    def mutate(root, info, title):
        document = db_types.Document(title=title)
        db_types.db.session.add(document)
        db_types.db.session.commit()
        return CreateDocument(document=document,ok=True)

class RootMutation(graphene.ObjectType):
    create_document = CreateDocument.Field()