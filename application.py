from bot.functions import check_update
import sys
from bot.functions import check_update

if __name__ == "__main__":
    if "test" in sys.argv or "--test" in sys.argv:
        check_update(is_test=True)
    else:
        check_update(is_test=False)