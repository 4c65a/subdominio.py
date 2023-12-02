import os
import requests
from pathlib import Path
import argparse


def target(subdominios):
    args = parse_args()
    results = []
    if subdominios:
        for subdominio in subdominios:
            url_http = f"http://{subdominio}.{args.target}"
            print(f"|+| Sitio: {url_http} |+| HTTP: {requests.codes.ok}")
             
            url_https = f"http://{subdominio}.{args.target}"
            print(f"|+| Sitio {url_https} |+| HTTPS: {requests.codes.ok}")

    return results

   
def cargar_wordlists(wordlists_file):
    if os.path.exists(wordlists_file):
        with open(wordlists_file, "r") as file:
            wordlists_content = file.read()
            wordlists_lines = wordlists_content.split("\n")
            return wordlists_lines
    else:
        print("El archivo no existe en la ruta proporcionada.")
        return []


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--target", help="Agregar el objetivo.")
    parser.add_argument("-w", "--wordlists", help="Lista de subdominios.")

    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if args.target and args.wordlists:
        target_print = target(cargar_wordlists(args.wordlists))
        print("target: ", target_print)


if __name__ == "__main__":
    main()
