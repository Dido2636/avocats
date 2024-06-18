import json, sys



# try: 
#     page = sys.argv[1]
# except:
#     page = '1'

print(page)

avocat_page = scraping_acovat(n_page=page)
print(avocat_page)

# Déplacer l'ouverture du fichier JSON en dehors de la boucle for
with open('avocat.json', 'w') as json_file:
    json.dump(avocat_page, json_file, ensure_ascii=False, indent=4)