import fb_auth

""" Fill in the four pieces of info and change this file name to config.py """

fb_email = """EMAIL"""
fb_password = """PASSWORD"""
fb_access_token = fb_auth.get_fb_access_token(fb_email, fb_password)
fb_user_id = fb_auth.get_fb_id(fb_access_token)
host = 'https://api.gotinder.com'

kairos_host = "http://api.kairos.com/detect"
kairos_app_id = """KAIROS APP ID"""
kairos_app_key = """KAIROS APP KEY"""
