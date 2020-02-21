import time
import logging
import time

from functools import wraps


# logging.basicConfig(level=logging.INFO, file='sample.log')
logging.basicConfig(level=logging.INFO)


def state_manager(api, name):
    def wrap(f):
        @wraps(f)
        def action_f(*args):
            api.update_task_by_name("processing", 1, name)
            try:
                f(*args)
                api.update_task_by_name("processing", 0, name)
            except:
                api.update_task_by_name("processing", -1, name)
                raise

        return action_f

    return wrap


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
