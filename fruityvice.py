import json
import urllib.request
import urllib.parse

def make_url(fruit):
        url = "http://www.fruityvice.com/api/fruit/"
        return url + fruit


def main():
    totalsDict = {"Carbohydrates": 0, "Protein": 0, "Fat": 0, "Calories": 0, "Sugar": 0}
    while True:
        fruit = input("Specify a fruit (or press ENTER to quit): ")
        if fruit == "":
            break
        url = make_url(fruit)
        req = urllib.request.Request(url, headers={ "User-Agent": "Mozilla/5.0" })     # pretends to be Firefox
        response = urllib.request.urlopen(req)                                         # this makes a network call
        raw = response.read()                                                          # read the raw response
        data = json.loads(raw)                                                         # Convert it to Python data
        nutritionData = data["nutritions"]
        totalsDict["Carbohydrates"] += nutritionData["carbohydrates"]
        totalsDict["Protein"] += nutritionData["protein"]
        totalsDict["Fat"] += nutritionData["fat"]
        totalsDict["Calories"] += nutritionData["calories"]
        totalsDict["Sugar"] += nutritionData["sugar"]
        # print(type(nutritionData))
        # print(nutritionData)
    print("Total Carbohydrates:", totalsDict["Carbohydrates"])
    print("Total Protein:", totalsDict["Protein"])
    print("Total Fat:", totalsDict["Fat"])
    print("Total Calories:", totalsDict["Calories"])
    print("Total Sugar:", totalsDict["Sugar"]) 

if __name__ == "__main__":
    main()