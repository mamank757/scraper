import requests

def ambil_data():
    url = "https://2025.epusluh.id/api/v1/lcs?url=%2Flcs&page=1&per_page=10"
    
    # Gunakan Bearer Token yang kamu temukan tadi
    headers = {
        "Authorization": "Bearer 5174356|4LqsGwgPCbJmBmFtLrFEqV1IPQmSgSElBCb6WwH966d72182",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json",
        "Origin": "https://dev.epusluh.id",
        "Referer": "https://dev.epusluh.id/"
    }

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            json_data = response.json()
            
            # Berdasarkan struktur API epusluh: data -> data -> list
            list_data = json_data.get('data', {}).get('data', [])
            
            if list_data:
                # Mengambil item pertama
                item = list_data[0]
                
                # Kita ambil 'title' atau 'caption' (biasanya field-nya ini)
                # Jika fieldnya beda, script ini akan menulis 'Field tidak ditemukan'
                teks_final = item.get('title') or item.get('caption') or "Field tidak ditemukan"
                
                print(f"Hasil: {teks_final}")
                
                with open("data.txt", "w", encoding="utf-8") as f:
                    f.write(str(teks_final))
            else:
                print("Data kosong dalam JSON.")
        else:
            print(f"Gagal! Status: {response.status_code}, Pesan: {response.text}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ambil_data()
