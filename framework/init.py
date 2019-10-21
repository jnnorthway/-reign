import os
import logging
import sys

for arg in sys.argv:
    if arg == '-d':
        logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

def check_env(env):
    assert os.environ.get(env) is not None, "%s environment variable not set." % env
    logging.debug("environment variable %s = %s", env, os.environ.get(env))

def set_env():
    os.environ["r_root"] = os.path.dirname(os.path.abspath(__file__))
    check_env("r_root")
    lib_path = "%s/../lib" % os.environ.get("r_root")
    os.environ["r_lib"] = lib_path
    check_env("r_lib")

def init():
    set_env()

init()