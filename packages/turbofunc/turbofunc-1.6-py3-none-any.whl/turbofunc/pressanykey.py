import sys
try:
    import msvcrt
    windows = True
except ImportError:
    import tty
    import termios
    windows = False
def pressanykey(string="Press any key to continue...", verbose=True, crashOnFailure=False):
    """
    SOURCE: https://raw.githubusercontent.com/TheTechRobo/python-text-calculator/master/FOR%20CLEARING%20THE%20SCREEN%20AND%20PRESS%20ANY%20KEY%20TO%20CONTINUE.md
    Setting verbose to True will cause the function to output a warning message with print() when it fails.
    Setting crashOnFailure to True will cause the function to raise a RuntimeError when the pressanykey fails. This overrides the verbose parameter.
    Even if both functions are set to False, the function will end prematurely if it fails.
    Neither of the previous parameters will have any effect if the user is running Windows.
    """
    print(string, end="", flush=True)
    if windows:
       msvcrt.getch()
    else:
       fd = sys.stdin.fileno()
       try:
           settings = termios.tcgetattr(fd)
       except Exception as ename:
           if crashOnFailure:
               raise RuntimeError
           if verbose:
               print("Press any key failed.")
           return False
       try:
           tty.setraw(sys.stdin.fileno())
           sys.stdin.read(1)
       finally:
           termios.tcsetattr(fd, termios.TCSADRAIN, settings)
