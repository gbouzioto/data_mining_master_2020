import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import factories as f

if __name__ == "__main__":
    fac = list(f.FacultyFactory.generate_faculties(n=10))
    pass
