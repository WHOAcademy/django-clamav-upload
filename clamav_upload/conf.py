from django.conf import settings as _settings

# Default ClamD TCP socket port
CLAMD_TCP_SOCKET = getattr(_settings, 'CLAMD_TCP_SOCKET', 3310)
# Default CLamd TCP socket addres
CLAMD_TCP_ADDR = getattr(_settings, 'CLAMD_TCP_ADDR', '127.0.0.1')
