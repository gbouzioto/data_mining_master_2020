import os
import sys
import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import factories as f

if __name__ == "__main__":
    phd = list(f.PHDFactory.generate_phds())
    datetime.datetime.strftime("23 December")
