import graphene
from graphene_django import DjangoObjectType
from profiles.models import Profile, Photos, Contacts


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


class PhotosType(DjangoObjectType):
    class Meta:
        model = Photos
        fields = "__all__"


class ContactsType(DjangoObjectType):
    class Meta:
        model = Contacts
        fields = "__all__"


class Query(graphene.ObjectType):
    all_profiles = graphene.List(ProfileType)

    def resolve_all_profiles(root, info):
        return Profile.objects.all()

