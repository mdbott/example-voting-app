from locust import TaskSet,task
import random
class VotingTasks(TaskSet):
    # vote = null
    # vote function
    def vote(self,vt):
        self.client.post("/",{"vote":vt})

    # initial random vote between cats or dogs
    @task(2)
    def votecat(self):
        self.vote("a")

    # change vote task
    @task(3)
    def votedg(self):
        self.vote("b")
