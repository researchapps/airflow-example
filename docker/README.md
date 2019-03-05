# Docker Example

The example comes from the Airflow repository. I removed the "url" variable
for the DockerOperator because I would just pull from Docker Hub. Then
I was able to run the pipeline from this folder like:

```bash
$ airflow test -sd . docker_sample docker_op_tester 2019-03-05
```
