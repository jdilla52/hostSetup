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
        status = api.get_task_param("status", video.name)
        # set the current task to busy
        proc_state = api.get_task_param("processing", video.name)

        try:
            api.update_task_by_name("processing", 1, video.name)
            f(video, api)
            api.update_task_by_name("processing", 0, video.name)
            api.update_task_by_name("status", status + 1, video.name)
        except:
            print("somethings wrong")
            api.update_task_by_name("processing", proc_state - 1, video.name)
            print(proc_state)

    return action_f


def logger(f):
    @wraps(f)
    def wrap(*args):
        try:
            start_time = time.time()
            logging.info(f"RUNNING : {f.__name__} - args : {args}")
            outcome = f(*args)
            logging.info(f"COMPLETED : {f.__name__} in : {time.time() - start_time}")
            return outcome
        except:
            logging.error(f"FAILED {f.__name__} has failed : {args}")
            raise

    return wrap
