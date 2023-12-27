from utils.settings import *
from utils.process import process_work
from utils.utils.logger import Logger
import os
import shutil

def run_zhem(conf_path: str, if_force: int):
    # load settings
    setting_module = Settings(conf_path)
    logger = Logger()

    '''
    check output_path, remove the output path if it has exists
    '''
    output_path = setting_module.settings['output_path']
    if if_force and os.path.exists(output_path):
        if if_force:
            shutil.rmtree(output_path)
            logger.log_text(f"The output path {output_path} already exists. The program has been terminated because the force mode is not used. Please check and replace it with a non-existent path.", desc='error')
        else:
            logger.log_text(f"The output path {output_path} already exists, please check and replace it with a non-existent path.", desc='warning')
    os.makedirs(output_path, exist_ok=True)

    # process work
    ret_args = process_work(setting_module, logger)
    return ret_args