import warnings
warnings.warn("Importing discussion.rest_api instead of lms.djangoapps.discussion.rest_api is deprecated", stacklevel=2)

from lms.djangoapps.discussion.rest_api import *
