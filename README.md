# projet_IOT
Le projet est composé de :
1. Partie batch
2. Partie streaming

## Execution
Exécuter le docker-compose :
```bash
docker-compose up -d 
```

## Partie batch :
Le répertoire elasticsearch comprend :
- `Dockerfile` :
Il va éxécuter elastic_init.py 

- `elastic_init.py` :
Le code va initialiser un shéma (en format json) pour pouvoir être déposé dans elasticsearch
- `requirements.txt` :
Ce fichier permet d'importer les dépendances requises pour permettre l'éxecution de elastic_init.py

Le répertoire hdfs :
Ce répertoire permet de simuler un hdfs

Le répertoire shared-workspace comprends :
- `etl.py` :
Il permet de récupérer les données des CSV dans Spark pour être envoyé dans élasticsearch
-  `elasticsearch-spark-20_2.11-7.6.2.jar` :
Est une librairie qui permet d'éxécuter l'etl.py dans spark

## Partie streaming :
non finalisé

