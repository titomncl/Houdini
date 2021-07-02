import os

HOU_EXT = ".hip"

USER_PATH = os.environ['USERPROFILE'].replace('\\', '/')
PFE_PATH = os.environ["PFE_ENV"]
DEV_PATH = os.environ["DEV_ENV"]
ROOT_PATH = os.environ["ROOT_PATH"]
PROJECT = PFE_PATH.split("/")[-1]
