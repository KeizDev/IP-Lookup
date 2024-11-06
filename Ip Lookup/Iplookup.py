# -*- coding: utf-8 -*-

try:
    from bs4 import BeautifulSoup
    import requests
except Exception as e:
    print(f"Error: {e}")

# Titre et bannières
def Title(name):
    print(f"\n{'='*10} {name} {'='*10}\n")

Title("OsintMx - IP Lookup")

# Variables de couleur personnalisées
VIOLET = "\033[38;5;93m"       # Violet
LIGHT_BLUE = "\033[38;5;117m"   # Bleu clair
WHITE = "\033[38;5;15m"         # Blanc
RESET = "\033[0m"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

# Fonction pour effectuer une recherche d'informations sur une adresse IP avec ipstack
def ipstack(ip):
    try:
        api_key = "YOUR_API_KEY"  # Remplacez par votre clé API personnelle
        url = f"http://api.ipstack.com/{ip}?access_key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "Service": "ipstack",
                "IP": data['ip'],
                "City": data['city'],
                "Country": data['country_name'],
                "Latitude": data['latitude'],
                "Longitude": data['longitude']
            }
        else:
            return {"Service": "ipstack", "Error": "IP non trouvée"}
    except Exception as e:
        return {"Service": "ipstack", "Error": str(e)}

# Fonction pour effectuer une recherche d'informations sur une adresse IP avec ipinfo
def ipinfo(ip):
    try:
        url = f"https://ipinfo.io/{ip}/json"
        response = requests.get(url, headers={'User-Agent': user_agent})
        if response.status_code == 200:
            data = response.json()
            return {
                "Service": "ipinfo",
                "IP": data['ip'],
                "City": data['city'],
                "Region": data['region'],
                "Country": data['country'],
                "Coordinates": data['loc']
            }
        else:
            return {"Service": "ipinfo", "Error": "IP non trouvée"}
    except Exception as e:
        return {"Service": "ipinfo", "Error": str(e)}

# Fonction pour effectuer une recherche d'informations sur une adresse IP avec ipapi
def ipapi(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return {
                "Service": "ip-api",
                "IP": data['query'],
                "City": data['city'],
                "Country": data['country'],
                "Latitude": data['lat'],
                "Longitude": data['lon']
            }
        else:
            return {"Service": "ip-api", "Error": "IP non trouvée"}
    except Exception as e:
        return {"Service": "ip-api", "Error": str(e)}

# Interface utilisateur
ip = input(f"{VIOLET}Entrez l'adresse IP à scanner : {RESET}")
print(f"{LIGHT_BLUE}\nRecherche en cours pour l'IP {ip}...{RESET}\n")

# Liste des services
services = [ipstack, ipinfo, ipapi]

# Exécution et affichage des résultats
for service in services:
    result = service(ip)
    print(f"{LIGHT_BLUE}{'-'*40}{RESET}")
    if "Error" in result:
        print(f"{VIOLET}⚠ {result['Service']}: {WHITE}{result['Error']}{RESET}")
    else:
        print(f"{WHITE}Service : {LIGHT_BLUE}{result['Service']}{RESET}")
        print(f"{WHITE}IP       : {LIGHT_BLUE}{result['IP']}{RESET}")
        print(f"{WHITE}Ville    : {LIGHT_BLUE}{result.get('City', 'N/A')}{RESET}")
        print(f"{WHITE}Région   : {LIGHT_BLUE}{result.get('Region', 'N/A')}{RESET}")
        print(f"{WHITE}Pays     : {LIGHT_BLUE}{result['Country']}{RESET}")
        print(f"{WHITE}Coordonnées : {LIGHT_BLUE}{result.get('Coordinates', f'Lat: {result.get('Latitude', 'N/A')}, Lon: {result.get('Longitude', 'N/A')}')}{RESET}")

# Résumé
print(f"\n{LIGHT_BLUE}{'='*40}{RESET}")
print(f"{VIOLET}Recherche terminée pour {ip}.{RESET}")