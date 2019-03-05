# Singularity Example

I'm working on a basic Singularity integration, and so far I have:

```bash
$ airflow test -sd . singularity_sample singularity_op_tester 2019-03-05
```
```bash
$ airflow test -sd . singularity_sample singularity_op_tester 2019-03-05
[2019-03-05 18:27:22,120] {__init__.py:51} INFO - Using executor SequentialExecutor
[2019-03-05 18:27:22,268] {__init__.py:298} INFO - Filling up the DagBag from /home/vanessa/Documents/Dropbox/Code/labs/cherry/airflow-example/singularity
[2019-03-05 18:27:22,388] {__init__.py:1090} INFO - Dependencies all met for <TaskInstance: singularity_sample.singularity_op_tester 2019-03-05T00:00:00+00:00 [None]>
[2019-03-05 18:27:22,392] {__init__.py:1090} INFO - Dependencies all met for <TaskInstance: singularity_sample.singularity_op_tester 2019-03-05T00:00:00+00:00 [None]>
[2019-03-05 18:27:22,392] {__init__.py:1308} INFO - 
--------------------------------------------------------------------------------
Starting attempt 1 of 2
--------------------------------------------------------------------------------

[2019-03-05 18:27:22,392] {__init__.py:1330} INFO - Executing <Task(SingularityOperator): singularity_op_tester> on 2019-03-05T00:00:00+00:00
[2019-03-05 18:27:22,401] {singularity_operator.py:98} INFO - Preparing Singularity container docker://busybox:1.30.1
[]
['singularity', 'instance', 'start', 'docker://busybox:1.30.1', 'gloopy_house_7897']
[2019-03-05 18:27:23,508] {singularity_operator.py:140} INFO - Created instance instance://gloopy_house_7897 from docker://busybox:1.30.1
```
