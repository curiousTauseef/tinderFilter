import config
import requests
from decimal import Decimal

kairos_headers = {
    "app_id": config.kairos_app_id,
    "app_key": config.kairos_app_key
}

def get_num_faces(url):
    return 1
    payload = '{"image":"%s"}' % url
    ret = requests.post(config.kairos_host, data=payload, headers=kairos_headers)
    try:
        ret = ret.json()
        num_faces = len(ret["images"])
        return num_faces
    except:
        return -1

def get_ethnicity(url):
    payload = '{"image":"%s"}' % url
    ret = requests.post(config.kairos_host, data=payload, headers=kairos_headers)
    try:
        face = ret.json()["images"][0]["faces"][0]["attributes"]

        asian = Decimal(face["asian"])
        black = Decimal(face["black"])
        white = Decimal(face["white"])
        hispanic = Decimal(face["hispanic"])
        other = Decimal(face["other"])

        defining_feature = max(asian, black, white, hispanic, other)

        if defining_feature == asian:
            return "asian"
        if defining_feature == black:
            return "black"
        if defining_feature == white:
            return "white"
        if defining_feature == hispanic:
            return "hispanic"
        if defining_feature == other:
            return "other"

    except:
        return "error"
