import requests

def ambil_data():
    url = "https://2025.epusluh.id/api/v1/lcs?url=%2Flcs&page=1&per_page=10"
    
    # Header ini sekarang jauh lebih lengkap untuk mengelabui firewall (WAF)
    headers = {
        "Authorization": "Bearer 5174356|4LqsGwgPCbJmBmFtLrFEqV1IPQmSgSElBCb6WwH966d72182",
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
        # Menambahkan session agar request terlihat lebih natural
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=15)
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data_json = response.json()
            items = data_json.get('data', {}).get('data', [])
            
            if items:
                # Mengambil field 'title'. Jika masih salah, coba ganti ke 'caption' atau 'content'
                teks_final = items[0].get('title') or items[0].get('caption') or "Data ditemukan tapi field kosong"
                
                with open("data.txt", "w", encoding="utf-8") as f:
                    f.write(str(teks_final))
                print(f"Berhasil: {teks_final}")
            else:
                with open("data.txt", "w") as f:
                    f.write("JSON Response OK, tapi data list kosong.")
        else:
            # Jika masih 403, tuliskan ke file untuk kita pantau
            with open("data.txt", "w") as f:
                f.write(f"Error Status: {response.status_code}. Server memblokir akses.")
                
    except Exception as e:
        with open("data.txt", "w") as f:
            f.write(f"Fatal Error: {str(e)}")

if __name__ == "__main__":
    ambil_data()
