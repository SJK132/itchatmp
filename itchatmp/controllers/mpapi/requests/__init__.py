from itchatmp.config import COROUTINE

# if you have itchatmphttp installed
# we will use coroutine requests instead
if COROUTINE:
    try:
        from itchatmphttp import requests
    except ImportError:
        raise ImportError('You must installed itchatmphttp to use coroutine features')
else:
    import requests
    requests.packages.urllib3.disable_warnings()
    adapters = requests.adapters.HTTPAdapter(pool_connections=100, pool_maxsize=100)
    requests = requests.session()
    requests.mount('https://', adapters)
    requests.verify = False
