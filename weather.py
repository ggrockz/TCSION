import  requests
import json


def weather_main():

    base_url = "https://api.openweathermap.org/data/2.5/weather?"

    city_name = "bengaluru"
    api_key = "519f63ba255a98f7dac423aed65c8ccf"

    urls = base_url + "q=" + city_name + "&appid=" + api_key

    result = requests.get(urls)
    print(urls)

    #checking the status
    if result.status_code == 200:
        data = result.json()
        #getting main block
        main = data['main']
        temperature = main['temp']
        report = data['weather']
        print(f"Temperature: {temperature}")
        print(f"Weather Report: {report[0]['description']}")

    else:
        print("Error in HTTP")

weather_main()