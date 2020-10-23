"""Define DAGS for airflow
"""
import datetime as dt
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import yaml
from mpg123 import Mpg123, Out123

default_args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2020, 1, 1, 00, 00, 00),
    'concurrency': 1,
    'retries': 0,
    'catchup': False
}

with open("/usr/local/airflow/dags/mount/config.yml") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def play_sound(file, amount):
    """Plays a sound from a given file an amount of times

    Args:
        file (string): file directory
        amount (int): number of times to play the file
    """
    for _ in range(amount):
        mp3 = Mpg123(file)
        out = Out123()
        for frame in mp3.iter_frames(out.start):
            out.play(frame)


def play_start():
    """Take start_file and start_amount from config and run play_sound with it.
    """
    filedir = "/usr/local/airflow/dags/mount/%s" % config["start_file"]
    play_sound(filedir, config["start_amount"])


def play_end():
    """Take end_file and end_amount from config and run play_sound with it.
    """
    filedir = "/usr/local/airflow/dags/mount/%s" % config["end_file"]
    play_sound(filedir, config["end_amount"])


with DAG(
        "trigger_start_sound",
        default_args=default_args,
        schedule_interval="0 %s-%s * * %s" % (config["first_reminder"],
                                              config["last_reminder"],
                                              "1-5" if config["weekday_only"]
                                              else "*")
) as start_dag:
    opr_start_sound = PythonOperator(task_id="start_sound",
                                     python_callable=play_start)

with DAG(
        "trigger_end_sound",
        default_args=default_args,
        schedule_interval="%s %s-%s * * %s" % (config["duration"],
                                               config["first_reminder"],
                                               config["last_reminder"],
                                               "1-5" if config["weekday_only"]
                                               else "*")
) as end_dag:
    opr_end_sound = PythonOperator(task_id="end_sound",
                                   python_callable=play_end)
