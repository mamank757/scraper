import requests

def ambil_data():
    url = "https://2025.epusluh.id/api/v1/lcs?url=%2Flcs&page=1&per_page=10"
    
    # Masukkan Token dan Cookie yang paling baru di sini
    headers = {
        "Authorization": "Bearer 5174356|4LqsGwgPCbJmBmFtLrFEqV1IPQmSgSElBCb6WwH966d72182",
        "Cookie": "https://2025.epusluh.id/api/v1/lcs?url=%2Flcs&page=1&per_page=10",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "Origin": "https://dev.epusluh.id",
        "Referer": "https://dev.epusluh.id/",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-site",
    }

    try:
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=15)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data_json = response.json()
            # Mencoba mengambil data dari list
            items = data_json.get('data', {}).get('data', [])
            
            if items:
                # Mengambil judul dari item pertama
                teks_final = items[0].get('title') or items[0].get('caption') or "Data Ada, Field Kosong"
                
                with open("data.txt", "w", encoding="utf-8") as f:
                    f.write(str(teks_final))
                print(f"Berhasil! Data: {teks_final}")
            else:
                with open("data.txt", "w") as f:
                    f.write("Data list kosong di dalam JSON.")
        else:
            with open("data.txt", "w") as f:
                f.write(f"Masih Error {response.status_code}. Cek Token/Cookie.")
                
    except Exception as e:
        with open("data.txt", "w") as f:
            f.write(f"Fatal Error: {str(e)}")

if __name__ == "__main__":
    ambil_data()
