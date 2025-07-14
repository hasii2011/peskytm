
from typing import List

from os import linesep as osLineSep

from subprocess import run
from subprocess import CompletedProcess

# execute the external process
cp: CompletedProcess = run(["mount"], capture_output=True, encoding="utf-8")

# capture the output
output: List[str] = cp.stdout.split(osLineSep)

# extract the interesting lines of output
tmLines: List[str] = []
for mountLine in output:
    if mountLine.startswith('com.apple.TimeMachine'):
        tmLines.append(mountLine)

# remove the parts that we need
timeMachineVolumes: List[str] = []
for tmLine in tmLines:
    parsedTM: List[str] = tmLine.split(' ')
    timeMachineVolumes.append(parsedTM[0])

# we now have the specific output
print(f'{timeMachineVolumes}')
