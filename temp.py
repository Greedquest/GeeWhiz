import sys
import os
from pathlib import Path
currentFile = Path(os.path.realpath(__file__))
sys.path.append(str(currentFile.parent / "DataCollation"))
print(sys.path[-1])