from locust import TaskSet,task
import random
class VotingTasks(TaskSet):
    # vote = null
    # vote function
    def vote(self,vt):
        self.client.post("/",{"vote":vt})

    # semi random vote between cats or dogs 40% cats 60% dogs
    @task(2)
    def votecat(self):
        self.vote("a")

    # change vote task
    @task(3)
    def votedg(self):
        self.vote("b")
