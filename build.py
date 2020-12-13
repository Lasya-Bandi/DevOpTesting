

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.django")

default_task = "publish"


@init
def initialize():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myapp.settings")
