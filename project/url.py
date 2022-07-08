urlpatterns = [
    ...,
    path('google_oauth/redirect/', RedirectOauthView)
]
urlpatterns = [
    ...,
    path('google_oauth/callback/', CallbackView)
]