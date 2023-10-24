import csv

# List of dictionaries containing website information
websites = [
    {"Website Name": "NDTV", "Language": "English", "URL": "https://www.ndtv.com/"},
    {"Website Name": "The Times of India", "Language": "English", "URL": "https://timesofindia.indiatimes.com/"},
    {"Website Name": "The Indian Express", "Language": "English", "URL": "https://indianexpress.com/"},
    {"Website Name": "Amar Ujala", "Language": "Hindi", "URL": "https://www.amarujala.com/"},
    {"Website Name": "Dainik Bhaskar", "Language": "Hindi", "URL": "https://www.bhaskar.com/"},
    {"Website Name": "Dainik Jagran", "Language": "Hindi", "URL": "https://www.jagran.com/"},
    {"Website Name": "Inquilab", "Language": "Urdu", "URL": "https://www.inquilab.com/"},
    {"Website Name": "Jagran Post", "Language": "Urdu", "URL": "https://www.jagranpost.com/"},
    {"Website Name": "Punjab Kesari", "Language": "Punjabi", "URL": "https://www.punjabkesari.in/"},
    {"Website Name": "Ajit Jalandhar", "Language": "Punjabi", "URL": "https://www.ajitjalandhar.com/"},
    {"Website Name": "Divya Bhaskar", "Language": "Gujarati", "URL": "https://www.divyabhaskar.co.in/"},
    {"Website Name": "Gujarat Samachar", "Language": "Gujarati", "URL": "https://www.gujaratsamachar.com/"},
    {"Website Name": "Lokmat", "Language": "Marathi", "URL": "https://www.lokmat.com/"},
    {"Website Name": "Saamana", "Language": "Marathi", "URL": "https://www.saamana.com/"},
    {"Website Name": "Eenadu", "Language": "Telugu", "URL": "https://www.eenadu.net/"},
    {"Website Name": "Sakshi", "Language": "Telugu", "URL": "https://www.sakshi.com/"},
    {"Website Name": "Vijaya Karnataka", "Language": "Kannada", "URL": "https://vijaykarnataka.com/"},
    {"Website Name": "Udayavani", "Language": "Kannada", "URL": "https://www.udayavani.com/"},
    {"Website Name": "Manorama Online", "Language": "Malayalam", "URL": "https://www.manoramaonline.com/"},
    {"Website Name": "Mathrubhumi", "Language": "Malayalam", "URL": "https://www.mathrubhumi.com/"},
    {"Website Name": "Dinamalar", "Language": "Tamil", "URL": "https://www.dinamalar.com/"},
    {"Website Name": "Dinakaran", "Language": "Tamil", "URL": "https://www.dinakaran.com/"},
    {"Website Name": "Sambad", "Language": "Odia", "URL": "https://sambad.in/"},
    {"Website Name": "Pragativadi", "Language": "Odia", "URL": "https://pragativadi.com/"},
    {"Website Name": "Anandabazar Patrika", "Language": "Bengali", "URL": "https://www.anandabazar.com/"},
    {"Website Name": "Bartaman", "Language": "Bengali", "URL": "https://www.bartamanpatrika.com/"},
    {"Website Name": "Dainik Agradoot", "Language": "Assamese", "URL": "https://agradoot.com/"},
    {"Website Name": "Asomiya Pratidin", "Language": "Assamese", "URL": "https://www.asomiyapratidin.in/"},
    {"Website Name": "Hueiyen Lanpao", "Language": "Manipuri", "URL": "https://www.hueiyenlanpao.com/"},
    {"Website Name": "Imphal Free Press", "Language": "Manipuri", "URL": "https://www.ifp.co.in/"},
]

# CSV file name
csv_file = 'Indian_Regional_News_Websites.csv'

# Write website information to the CSV file
with open(csv_file, mode='w', newline='') as csv_file:
    fieldnames = ['Website Name', 'Language', 'URL']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(websites)

print(f"Websites data saved to {csv_file}")
