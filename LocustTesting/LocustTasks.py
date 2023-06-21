from locust import HttpUser
from VotingTask import VotingTasks
from ResultTask import ResultTasks


class MyVoteLocust(HttpUser):
    tasks = [VotingTasks]
    min_wait = 10
    max_wait = 100
    #host = ’http://localhost:5000’
    host = "http://voting.example.com"


class MyServicesLocust(HttpUser):
    tasks = [ResultTasks]
    min_wait = 10
    max_wait = 100
    #host = ’http://localhost:5001’
    host = "http://results.example.com"
