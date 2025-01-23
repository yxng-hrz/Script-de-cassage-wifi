# Script de Cassage WiFi

Ce script Python permet d'automatiser certaines tâches de cassage de réseaux WiFi en utilisant des outils comme `aircrack-ng`, `airodump-ng` et `reaver`. Il supporte les attaques sur les protocoles WEP, WPA2 et WPS, ainsi que la déconnexion forcée de clients.

## Prérequis

- Système d'exploitation basé sur Linux
- Python 3.x
- Outils nécessaires installés :
  - `aircrack-ng`
  - `reaver`
  - `aireplay-ng`
- Permissions administrateur (sudo)
- Interface WiFi compatible avec le mode moniteur

## Fonctionnalités

1. **Mode manuel** : Permet de choisir une cible et d'exécuter des attaques spécifiques (WEP, WPA2, WPS).
2. **Mode automatique** : Recherche des réseaux WiFi disponibles et propose des attaques en fonction du type de chiffrement.
3. **Déconnexion forcée** : Permet de déconnecter un client spécifique d'un réseau ciblé.

## Utilisation

1. Clonez ou téléchargez ce dépôt.
2. Assurez-vous que les prérequis sont satisfaits.
3. Exécutez le script avec des privilèges administrateur :

   ```bash
   sudo python3 wifi_cracking_automation.py
   ```

4. Suivez les instructions affichées pour sélectionner l'opération souhaitée :
   - **(1)** Cassage manuel
   - **(2)** Recherche et cassage automatique
   - **(3)** Déconnexion forcée

## Avertissement

Ce script est conçu uniquement à des fins éducatives.

## Authors

Guillaume Houriez 3si2
Mohamed Hassan 3si2
