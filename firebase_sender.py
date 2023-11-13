#https://electro-211fc-default-rtdb.firebaseio.com/
from firebase import firebase
import json
import random
import time

class FirebaseSender:
    def __init__(self, url = "https://electro-211fc-default-rtdb.firebaseio.com/"):
        self.firebase = firebase.FirebaseApplication(url)
    
    def post(self, key = "", value = ""):
        self.firebase.put("/", key, value)
    
    def post_score(self, player1_score, player2_score):
        scores = {"player1_score": player1_score, "player2_score": player2_score}
        self.firebase.put("/", "scores", scores)

    def get_score(self):
        return self.firebase.get("/", "scores")
    
    def get(self, key=""):
        newDict = list(self.firebase.get("/", key))
        return newDict
        
if __name__ == "__main__":
    firebase_instance = FirebaseSender()
    while True:
        print(firebase_instance.get_score()['player1_score'])
    
    
