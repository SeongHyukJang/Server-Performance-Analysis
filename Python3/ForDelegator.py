import subprocess
import delegator


lst = subprocess.run(['ls','-l'])
print(lst)