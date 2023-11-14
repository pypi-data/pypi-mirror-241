import re
import inspect
import logging
import warnings
from .y4a_telegram import send_message

warnings.filterwarnings("ignore", category=UserWarning)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)


def telegram_alert(context) -> None:
    """
    Airflow DAG failure notification to Telegram
    """

    telegram_owners = {
        'giangpt': 'trgiangpham',
        'hieulm': 'hieuminhla',
        'linhvu': 'vukhanhlinh0115',
        'huongtmt': 'tuyethuong',
        'phinguyenvan': 'PhiNguyen8009',
        'toannh': 'Huu_Toan',
        'trieuna': 'TrienAnhNguyen',
        'hoaidtm': 'hoaido236',
        'duikha': 'DuiKhaa',
        'longgh': 'Giap_Long',
        'huypv': 'huypv',
        'huytln': 'huytrinh194',
        'quandang': 'mquan_dang',
        'nguyentnt': 'emilysdata',
        'clong': 'liuliukiki',
        'j_ai_biec': 'liuliukiki',
    }

    airflow_owner = context['dag'].default_args['owner']
    if airflow_owner in telegram_owners:
        owner = '@' + telegram_owners[airflow_owner]
    else:
        owner = '@' + airflow_owner

    message = f"\u26d4 *{context['task_instance']}*\n"
    message += f"Owner: {owner}\n"
    message += f"DAG ID: *{context['task_instance'].dag_id}*\n"
    message += f"Task ID: *{context['task_instance'].task_id}*\n"
    message += f"Execution Time: *{context['task_instance'].execution_date}*\n"
    message += f"Error: *{context['exception']}*"[:500] + "\n"

    local_log_url = str(context['task_instance'].log_url)
    local_domain = re.findall(
        r'localhost:[0-9]+',
        local_log_url,
    )[0]
    if 'da_serving' in context['task_instance'].dag_id:
        sever_domain = 'https://airflow-serving.yes4all.com'
    elif 'da_processing' in context['task_instance'].dag_id:
        sever_domain = 'https://airflow-serving.yes4all.com'
    elif 'project_serving' in context['task_instance'].dag_id:
        sever_domain = 'https://airflow-serving.yes4all.com'
    else:
        sever_domain = 'https://airflow-ingestion.yes4all.com'

    log_url = sever_domain + local_log_url.split(local_domain)[-1]

    message += f"Log URL: [Link]({log_url})"

    telegram_token = "6318613524:AAG3_JGEsTZbSvcupG5aJk-jZPzghuf3yZ4"
    chat_id = "-868321875"

    send_message(
        text=message,
        bot_token=telegram_token,
        chat_id=chat_id,
    )


def auto_dag_id() -> str:
    """
    Auto naming for the Airflow DAG ID based on the file directory

    :return: name of the Airflow DAG ID
    """

    current_frame = inspect.currentframe()
    current_path = inspect.getfile(current_frame.f_back)
    airflow_path = current_path.split('/airflow/dags/')[-1]
    airflow_path = airflow_path.replace(
        'sop_ingestion',
        'de',
    )
    airflow_path = airflow_path.replace(
        'sop_da_serving',
        'da_serving',
    )
    airflow_path = airflow_path.replace(
        'sop_da_processing',
        'da_processing',
    )
    airflow_path = airflow_path.replace(
        'sop_project_serving',
        'project_serving',
    )
    dag_id = airflow_path\
        .replace('.py', '')\
        .lower().strip()
    dag_id = re.sub(
        r'[^a-zA-Z0-9/]+',
        '_',
        dag_id,
    )
    dag_id = dag_id.replace('/', '.')

    return dag_id
