import sys
import utils
from pathlib import Path
import importlib.util


# We're running as a Python main module, so the first item in sys.argv
# will be 'figur', the name of the module.
[_, func, *args] = sys.argv
cwd = Path.cwd()
figur = "figur.py"
script_path = utils.find_file_name(figur)

if not script_path:
    sys.exit(1)
    print(f"No {figur} file!")

spec = importlib.util.spec_from_file_location("figur.script", script_path)
script = importlib.util.module_from_spec(spec)
spec.loader.exec_module(script)

functions = set(
    v
    for v in dir(script)
    if not (
        v.startswith("__")
        or v in set("sys rich name args subprocess inspect".split(" "))
    )
)


if func in functions:
    utils.dispatch(getattr(script, func), *args)

else:
    print(f"No command found for {func} " + args.join(""))
    sys.exit(1)
