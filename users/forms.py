from django import forms as fr

from mlechniy_put.constants import DbFieldsLength


class UserCreateForm(fr.Form):
    email = fr.EmailField()
    password = fr.CharField(max_length=20)
    first_name = fr.CharField(max_length=DbFieldsLength.CHAR_FIELD)
    last_name = fr.CharField(max_length=DbFieldsLength.CHAR_FIELD)
    patronymic = fr.CharField(max_length=DbFieldsLength.CHAR_FIELD, required=False)
    phone = fr.CharField(max_length=DbFieldsLength.PHONE_LENGTH)
    age = fr.IntegerField()
    post_address_author = fr.CharField(
        max_length=DbFieldsLength.TEXT_FIELD, required=False
    )
    edu_organization_name = fr.CharField(
        max_length=DbFieldsLength.CHAR_FIELD, required=False
    )
    edu_organization_address = fr.CharField(
        max_length=DbFieldsLength.TEXT_FIELD, required=False
    )
    teacher_full_name = fr.CharField(
        max_length=DbFieldsLength.CHAR_FIELD, required=False
    )
    teacher_position = fr.CharField(
        max_length=DbFieldsLength.CHAR_FIELD, required=False
    )
    story_file = fr.FileField()
    story_title = fr.CharField(max_length=DbFieldsLength.CHAR_FIELD)
