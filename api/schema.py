from graphene import ObjectType, String, Schema

from profiles.mutations import ProfileMutation
from users.query import Query as UsersQuery
from follows.query import Query as FollowsQuery
from profiles.query import Query as ProfilesQuery



class Query(UsersQuery, FollowsQuery, ProfilesQuery, ObjectType):
    hello = String(default_value="stringer")

class Mutation(ProfileMutation):
  pass

schema = Schema(query=Query, mutation=Mutation)
  