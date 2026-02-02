from util import Util
import random
from curl_cffi import requests

config = Util.get_config()

SOLVER_KEY = config["solverKey"]
PUBLIC_KEY = config["publicKey"]

def get_token(roblox_session: requests.Session, blob, proxy, cookies):
    session = requests.Session()
    solution = requests.post("https://api.devioussolver.com/solve", json={"api_key": SOLVER_KEY, "proxy": proxy, "blob_exchange": blob, "public_key": PUBLIC_KEY, "cookies": cookies}, timeout=120).json()

    return solution.get("token")
    
# you can change the "api.devioussolver.com/solve" for others funcaptcha solvers i think