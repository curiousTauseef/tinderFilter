import json
import urllib

import tinder_api as tinder
import face_recognition as kairos
import config


def main():
    # git authorized
    tinder.get_authorized()

    # get_reccomendations
    reccomendations = tinder.get_reccomendations()

    # for every reccomendation...
    user_urls = []
    for reccomendation in reccomendations:
        # get list of urls
        user_urls = tinder.get_user_urls(reccomendation["_id"])

        # for every url...
        for url in user_urls:
            # if the photo has a one and only one face
            if kairos.get_num_faces(url) != -1:
                # ethnicity (white || asian || hispanic || black || other)
                ethnicity = kairos.get_ethnicity(url)
                if ethnicity == "asian":
                    print("ASIAN!")
                    urllib.request.urlretrieve(url, "./photos/asian/" + reccomendation["_id"] + ".jpg")
                    tinder.like(reccomendation["_id"])
                if ethnicity == "white":
                    print("Not Asian :( (white)")
                    urllib.request.urlretrieve(url, "./photos/white/" + reccomendation["_id"] + ".jpg")
                if ethnicity == "black":
                    print("Not Asian :( (black)")
                    urllib.request.urlretrieve(url, "./photos/black/" + reccomendation["_id"] + ".jpg")
                if ethnicity == "hispanic":
                    print("Not Asian :( (hispanic)")
                    urllib.request.urlretrieve(url, "./photos/hispanic/" + reccomendation["_id"] + ".jpg")
                if ethnicity == "other":
                    print("Not Asian :( (other)")
                    urllib.request.urlretrieve(url, "./photos/other/" + reccomendation["_id"] + ".jpg")


                if ethnicity == "error":
                    print("Could not find face")



if __name__ == "__main__":
    main()
