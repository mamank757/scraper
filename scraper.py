import requests
import json

def ambil_data():
    url = "https://2025.epusluh.id/api/v1/lcs?url=%2Flcs&page=1&per_page=10"
    
    headers = {
        "Authorization": "Bearer 5174356|4LqsGwgPCbJmBmFtLrFEqV1IPQmSgSElBCb6WwH966d72182",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data_json = response.json()
            # Kita coba ambil field 'title' dari data pertama
            try:
                # Menyesuaikan struktur JSON Epusluh
                items = data_json.get('data', {}).get('data', [])
                if items:
                    teks_final = items[0].get('title', 'Judul Tidak Ditemukan')
                else:
                    teks_final = "Data JSON Kosong"
            except:
                teks_final = "Gagal Parsing JSON"
                
            print(f"Hasil yang didapat: {teks_final}")
            
            # PAKSA buat file data.txt meskipun isinya pesan error
            with open("data.txt", "w", encoding="utf-8") as f:
                f.write(str(teks_final))
        else:
            # Jika gagal login/akses, tulis status errornya ke file
            with open("data.txt", "w") as f:
                f.write(f"Error Status: {response.status_code}")
                
    except Exception as e:
        with open("data.txt", "w") as f:
            f.write(f"Fatal Error: {str(e)}")

if __name__ == "__main__":
    ambil_data()
