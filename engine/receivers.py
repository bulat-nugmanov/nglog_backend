from rest_framework.authtoken.models import Token


# def create_auth_token(sender, instance=None, created=False, **kwargs):
#   if created:
#        Token.objects.create(user=instance)
# receiver function for authentication purposes
# gets called when a signal is sent by user_logged_in()
def auth_token_callback(sender, user, request, **kwargs):
    print "Successful login!"
    if not Token.objects.filter(key=request.data["auth_token"]).exists():
        Token.objects.create(user=user).save()

