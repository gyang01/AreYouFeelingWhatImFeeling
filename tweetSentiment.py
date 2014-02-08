import unirest
import json

def getResult(feeling):
    response = unirest.post("https://community-sentiment.p.mashape.com/text/",
                        
                            headers={
                                "X-Mashape-Authorization": "rHozCQvZPwVGYmnHEd48nqJ7rix398tY"
                            },
                            params={ 
                            "txt": feeling
                            }
                        );
    return response;


def getConfidence(feeling):
    response=getResult(feeling).body
    return response['result']['confidence']

def getPositive(feeling):
    response=getResult(feeling).body
    return response['result']['sentiment']

