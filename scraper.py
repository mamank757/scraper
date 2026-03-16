import requests
import json

def ambil_data():
    url = "https://2025.epusluh.id/api/v1/lcs?url=%2Flcs&page=1&per_page=10"
    
    # Ambil Cookie dari tab Network (Request Headers) seperti cara sebelumnya
    headers = {
        "Cookie": "MASUKKAN_COOKIE_ASLI_KAMU_DISINI",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            data_json = response.json()
            
            # Mengakses data: biasanya strukturnya data -> data -> list
            # Kita ambil item pertama [0]
            items = data_json.get('data', {}).get('data', [])
            
            if items:
                # Ambil field 'title' atau 'content' (sesuaikan dengan isi JSON-nya)
                item = items[0]
                judul = item.get('title', 'Tidak ada judul')
                # Misal kamu ingin format: "255 (Instagram...) Gerakan Tanam..."
                teks_final = f"{judul}" 
                
                with open("data.txt", "w", encoding="utf-8") as f:
                    f.write(teks_final)
                print(f"Berhasil menyimpan: {teks_final}")
            else:
                print("Data tidak ditemukan dalam JSON.")
        else:
            print(f"Gagal! Status code: {response.status_code}")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    ambil_data()
