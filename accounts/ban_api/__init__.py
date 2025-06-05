import requests

API_BASE_URL = "https://api-adresse.data.gouv.fr/search/"


def validate_address(address: str) -> dict:
    response = requests.get(API_BASE_URL, params={
        "q": address,
        "limit": 1
    })

    if response.status_code != 200:
        return {
            "valid": False
        }

    data = response.json()
    print(data)

    if "features" in data:
        features = data["features"]

        if isinstance(features, list) and len(features) > 0:
            properties = features[0]["properties"]
            geo = features[0]["geometry"]
            return {
                "valid": True,
                "latitude": geo["coordinates"][1],
                "longitude": geo["coordinates"][0],
                "label": properties["label"]
            }

    return {
        "valid": False
    }
