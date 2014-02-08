import unirest

def getResult(feeling):
    response = unirest.get("https://loudelement-free-natural-language-processing-service.p.mashape.com/nlp-text/?text=i%20hate%20myself",
                        
                           headers={
                            "X-Mashape-Authorization": "rHozCQvZPwVGYmnHEd48nqJ7rix398tY"
                           },
                           params={
                               "text":feeling
                           }
                           
                       );
    return response.body

def getConfidence(feeling):
    response=getResult(feeling)
    return response['sentiment-score']

def getPositive(feeling):
    response=getResult(feeling)
    return response['sentiment-text']

