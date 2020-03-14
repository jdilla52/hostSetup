import time
import logging
import time

from functools import wraps


# logging.basicConfig(level=logging.INFO, file='sample.log')
logging.basicConfig(level=logging.INFO)


def state_manager(f):
    @wraps(f)
    def action_f(video, api):
        # get the current status of the task at hand
        status = api.get_task_status(video.name)
        print(status)
        # set the current task to busy
        api.update_task_by_name("processing", 1, video.name)

        try:
            f(video, api)
            api.update_task_by_name("processing", 0, video.name)
            api.update_task_by_name("status", status + 1, video.name)
        except:
            api.update_task_by_name("processing", -1, video.name)

    return action_f


def logger(f):
    @wraps(f)
    def wrap(*args):
        try:
            start_time = time.time()
            logging.info(f"STARTED : {f.__name__}")
            logging.info(f"RUNNING : {f.__name__} - args : {args}")
            f(*args)
            logging.info(f"COMPLETED : {f.__name__} in : {time.time() - start_time}")
        except:
            logging.error(f"FAILED {f.__name__} has failed : ")

    return wrap
