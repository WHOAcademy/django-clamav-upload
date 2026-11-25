from django.apps import AppConfig

class ClamAVUploadConfig(AppConfig):
    name = 'clamav_upload'
    verbose_name = 'ClamAV Upload'
    # Pin the primary key type so host projects' DEFAULT_AUTO_FIELD never
    # makes this app's migrations look out of date.
    default_auto_field = 'django.db.models.AutoField'
