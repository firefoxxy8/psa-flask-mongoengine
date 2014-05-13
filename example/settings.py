MONGODB_SETTINGS = {'DB': 'demo_db'}

SECRET_KEY = 'random-secret-key'
SESSION_COOKIE_NAME = 'demo_session'
SESSION_PROTECTION = 'strong'

SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/done/'
SOCIAL_AUTH_USER_MODEL = 'example.models.user.User'
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social.backends.soundcloud.SoundcloudOAuth2',
    'social.backends.lastfm.LastFmAuth',
)
