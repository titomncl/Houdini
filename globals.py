import os

USER_PATH = os.environ['USERPROFILE'].replace('\\', '/')
PFE_PATH = os.environ["PFE_ENV"]
DEV_PATH = os.environ["DEV_ENV"]
PROJECT = os.environ["PFE_PROJET"].split("/")[-1]
