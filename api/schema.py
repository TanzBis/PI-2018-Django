from graphene import ObjectType, String, Schema
from users.query import Query as UsersQuery
from follows.query import Query as FollowsQuery
from profiles.query import Query as ProfilesQuery


class Query(UsersQuery, FollowsQuery, ProfilesQuery, ObjectType):
    hello = String(default_value="stringer")


schema = Schema(query=Query)
