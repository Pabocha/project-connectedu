import requests
from django.db import connection
# from django_tenants.utils import schema_context
from getpass import getpass
import socket


endpoint = "http://localhost:8000/api/token/"
username = input("Veuillez saisir votre username \n")
password =getpass("Veuillez saisir votre password \n")
auth_response = requests.post(endpoint, json={'username':username, 'password':password})
print (auth_response.json())
access = auth_response.json().get('access')
refresh = auth_response.json().get('refresh')
user_info_endpoint = "http://localhost:8000/api/token/info/"

if auth_response.status_code == 200:
    headers = {
        'Authorization': f'Bearer {access}',    

    }
    user_info_response = requests.get(user_info_endpoint, headers=headers)
    user_data = user_info_response.json()
    print("Informations sur l'utilisateur :", user_data)
    headers = {
        'Authorization': f'Bearer {access}',
        'Host': f"{user_data['ecole'].replace('_', '-')}.localhost"

    }
    print(headers)
    if user_data['ecole'] is not None:
          endpoint_ecole = "http://localhost:8000/salle/"
        # try:
        #     ip_address = socket.gethostbyaddr(f"{user_data['ecole'].replace('_', '-')}.localhost")
        #     endpoint_ecole = f"http://{ip_address}:8000/salle/"
        #     print("§§§§§§§§§§")
        # except socket.gaierror as e:
        #     print("Erreur de résolution du nom d'hôte", e)
            # Gérer l'erreur selon vos besoins
    else:
            
        endpoint_ecole = "http://localhost:8000/inscription/ecole/"

    print("URL de l'école :", endpoint_ecole)
    response = requests.get(endpoint_ecole, headers=headers)
    print(response.json())
    print(response.status_code)





