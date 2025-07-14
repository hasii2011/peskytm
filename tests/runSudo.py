
from subprocess import run
from subprocess import CompletedProcess


fsToUnMount: str = 'com.apple.TimeMachine.2021-09-26-120444.backup@/dev/disk7s2'
# password: str = input("Enter password:")

cp: CompletedProcess = run(['sudo', 'umount', '-f', fsToUnMount], capture_output=True, encoding="utf-8")

print(f'{cp.returncode=}')
print(f'{cp.stdout=}')
