import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://3791612e-f3ba-4abc-927d-c92ae5ff6aea.westus2.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "8fQomtrNOLgHDISBo3tZoOMrtnREHaz0"

# Two sets of data to score, so we get two results back
data = {
    "Inputs": 
	{
	"data":
	[
      {
        "age": 25,
        "job": "teacher",
        "marital": "married",
        "education": "high.school",
        "default": "no",
        "housing": "no",
        "loan": "yes",
        "contact": "cellular",
        "month": "may",
        "day_of_week": "mon",
        "duration": 300,
        "campaign": 1,
        "pdays": 999,
        "previous": 1,
        "poutcome": "failure",
        "emp.var.rate": 1.1,
        "cons.price.idx": 93.994,
        "cons.conf.idx": -46.2,
        "euribor3m": 4.967,
        "nr.employed": 5228.1
      },
   ]
}
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
