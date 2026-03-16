import requests

def ambil_data():
    url = "https://2025.epusluh.id/api/v1/lcs?url=%2Flcs&page=1&per_page=10"
    
    # Headers persis hasil cURL kamu
    headers = {
        'authority': '2025.epusluh.id',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
        'authorization': 'Bearer 5174356|4LqsGwgPCbJmBmFtLrFEqV1IPQmSgSElBCb6WwH966d72182',
        'origin': 'https://dev.epusluh.id',
        'referer': 'https://dev.epusluh.id/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site'
    }

    try:
        # Menggunakan session agar koneksi lebih stabil
        session = requests.Session()
        response = session.get(url, headers=headers, timeout=20)
        
        print(f"Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            # Mencoba navigasi ke field data
            items = data.get('data', {}).get('data', [])
            
            if items:
                # Ambil field 'title' atau 'content'
                # Kita coba ambil field 'title' dulu
                hasil = items[0].get('title') or items[0].get('content') or "Data ditemukan tanpa judul"
                
                with open("data.txt", "w", encoding="utf-8") as f:
                    f.write(str(hasil))
                print(f"Berhasil: {hasil}")
            else:
                with open("data.txt", "w") as f:
                    f.write("JSON OK, tapi list data kosong.")
        else:
            with open("data.txt", "w") as f:
                f.write(f"Gagal 403: Cloudflare memblokir IP GitHub.")
                
    except Exception as e:
        with open("data.txt", "w") as f:
            f.write(f"Error: {str(e)}")

if __name__ == "__main__":
    ambil_data()
