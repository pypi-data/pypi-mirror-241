import sys

from .warp.core import Interpreter

# This is done so when users `import interpreter`,
# they get an instance of interpreter:

sys.modules["warpcoreai"] = Interpreter()

# **This is a controversial thing to do,**
# because perhaps modules ought to behave like modules.

# But I think it saves a step, removes friction, and looks good.