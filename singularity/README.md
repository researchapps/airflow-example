# Singularity Example

I'm working on a basic Singularity integration, and so far I have:

```bash
$ airflow test -sd . singularity_sample singularity_op_tester 2019-03-05
```
```bash
$ airflow test -sd . singularity_sample singularity_op_tester 2019-03-05
[2019-03-06 13:18:40,073] {__init__.py:51} INFO - Using executor SequentialExecutor
[2019-03-06 13:18:40,236] {__init__.py:298} INFO - Filling up the DagBag from /home/vanessa/Documents/Dropbox/Code/labs/cherry/airflow-example/singularity
[2019-03-06 13:18:40,371] {__init__.py:1090} INFO - Dependencies all met for <TaskInstance: singularity_sample.singularity_op_tester 2019-03-05T00:00:00+00:00 [None]>
[2019-03-06 13:18:40,375] {__init__.py:1090} INFO - Dependencies all met for <TaskInstance: singularity_sample.singularity_op_tester 2019-03-05T00:00:00+00:00 [None]>
[2019-03-06 13:18:40,376] {__init__.py:1308} INFO - 
--------------------------------------------------------------------------------
Starting attempt 1 of 2
--------------------------------------------------------------------------------

[2019-03-06 13:18:40,376] {__init__.py:1330} INFO - Executing <Task(SingularityOperator): singularity_op_tester> on 2019-03-05T00:00:00+00:00
[2019-03-06 13:18:40,387] {singularity_operator.py:98} INFO - Preparing Singularity container docker://busybox:1.30.1
[2019-03-06 13:18:41,361] {singularity_operator.py:140} INFO - ['singularity', 'instance', 'start', 'docker://busybox:1.30.1', 'phat_animal_9868']
[2019-03-06 13:18:41,361] {singularity_operator.py:141} INFO - Created instance instance://phat_animal_9868 from docker://busybox:1.30.1
[2019-03-06 13:18:41,361] {singularity_operator.py:143} INFO - Running command /bin/sleep 30
[2019-03-06 13:19:11,412] {singularity_operator.py:150} INFO - Stopping instance instance://phat_animal_9868
[2019-03-06 13:19:11,624] {singularity_operator.py:162} INFO - Output from command ()
```
