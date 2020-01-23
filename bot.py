import nsplshr
import urllib.request
import credentials as cr
from time import sleep as zzz
from twitter import *
from os import unlink

t = Twitter(auth=OAuth(cr.TT_ACCESS_TOKEN, cr.TT_ACCESS_TOKEN_SECRET,cr.TT_API_KEY, cr.TT_API_SECRET_KEY))


def tweetimage():
    photo = nsplshr.getImages(cr.UNSPLASH_CLIENT_ID).body[0]
    user = 'https://unsplash.com/@' + photo['user']['username']
    link = photo['links']['html']
    download_link = photo['links']['download']
    img_dir = f"./imgs/{photo['id']}.jpg"
    tweet = f"{user}\n{link}\n{download_link}"
    urllib.request.urlretrieve(download_link, img_dir)

    with open(img_dir, "rb") as imagefile:
        imagedata = imagefile.read()
    t_upload = Twitter(domain='upload.twitter.com', auth=OAuth(cr.TT_ACCESS_TOKEN, cr.TT_ACCESS_TOKEN_SECRET,cr.TT_API_KEY, cr.TT_API_SECRET_KEY))
    try:
        id_img1 = t_upload.media.upload(media=imagedata)["media_id_string"]
    except Exception:
        tweetimage()
    t.statuses.update(status=tweet, media_ids=",".join([id_img1]))
    unlink(img_dir)
    zzz(3600)
    tweetimage()

tweetimage()
