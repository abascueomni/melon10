import requests

def get_melon_chart():
    url = "https://m.app.melon.com/chart/hourly/hourlyChartList.json"

    params = {
        "cpId": "AS40",
        "cpKey": "14LNM3",
        "v": "4.0",
        "resolution": 2,
        "appVer": "4.1.0.1",
        "osVersion": "11",
        "isRecom": "N",
        "pageSize": 10
    }

    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 11) AppleWebKit/537.36 Chrome/100.0.0.0 Mobile Safari/537.36",
        "Accept": "application/json, text/plain, */*",
    }

    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    return response.json()

def main():
    chart = get_melon_chart()

    chart_data = chart["response"]
    songs = chart_data["CHARTLIST"]

    print()
    print("MELON REALTIME TOP 10")
    print(f"Chart: {chart_data['RANKDAY']} {chart_data['RANKHOUR']}")
    print()

    for song in songs:
        rank = int(song["CURRANK"])
        previous_rank = int(song["PASTRANK"])
        title = song["SONGNAME"]
        artists = ", ".join(
            artist["ARTISTNAME"] for artist in song["ARTISTLIST"]
        )

        if previous_rank == 0:
            movement_text = "*"
        else:
            movement = previous_rank - rank

            if movement > 0:
                movement_text = f"↑ {movement}"
            elif movement < 0:
                movement_text = f"↓ {abs(movement)}"
            else:
                movement_text = "—"

        print(f"{rank}. [{movement_text}] {title} — {artists}")

if __name__ == "__main__":
    main()