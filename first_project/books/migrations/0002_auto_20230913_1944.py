# from django.db import migrations


# def combine_names(apps, schema_editor):
#     # We can't import the Person model directly as it may be a newer
#     # version than this migration expects. We use the historical version.
#     User = apps.get_model("users", "User")
#     for user in User.objects.all():
#         user.fullname = f"{user.first_name} {user.last_name}"
#         user.save()


# class Migration(migrations.Migration):
#     dependencies = [
#         ("yourappname", "0001_initial"),
#     ]

#     operations = [
#         migrations.RunPython(combine_names),
#     ]
