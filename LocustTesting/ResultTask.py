from locust import TaskSet,task
import random
class ResultTasks(TaskSet):
    # result function
    @task
    def result(self):
        self.client.get("/")
