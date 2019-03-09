from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.contrib.operators.singularity_operator import SingularityOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.utcnow(),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG('singularity_sample', default_args=default_args, schedule_interval=timedelta(minutes=10))

t1 = BashOperator(
    task_id='print_date',
    bash_command='date',
    dag=dag)

t2 = BashOperator(
    task_id='sleep',
    bash_command='sleep 5',
    retries=3,
    dag=dag)

t3 = SingularityOperator(command='/bin/sleep 30',
                        image='docker://busybox:1.30.1',
                        task_id='singularity_op_tester',
                        dag=dag)

t4 = BashOperator(
    task_id='print_hello',
    bash_command='echo "hello world!!!"',
    dag=dag)

t1.set_downstream(t2)
t1.set_downstream(t3)
t3.set_downstream(t4)
