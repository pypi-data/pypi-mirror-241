import os
import sys
import argparse
from .core_functions import game_of_life, display_state

VERSION = '1.0'


def main():
    parser = argparse.ArgumentParser(description='Galsen Game of Life')

    parser.add_argument('--version', action='version', version='%(prog)s ' + VERSION)

    parser.add_argument('--input', help="Etat initial")

    parser.add_argument('--num-steps', type=int, default=10, help="Nombre d'etapes")

    parser.add_argument('--verbose', help="Print toutes les etapes")

    parser.add_argument('--output-file', default=os.path.join(os.path.dirname(__file__)), help="Repertoire de sortie")

    args = parser.parse_args()

    if args.input:
        # fichier etat initial
        initial_state_file = args.input
        # load the file content
        with open(initial_state_file) as f:
            initial_state = []
            lines = f.readlines()
            for line in lines:
                # remove the \n at the end
                line = line.rstrip()
                initial_state.append(list(map(lambda x: int(x), line.split())))
        display_state(initial_state, title="INITIAL")
        num_steps = args.num_steps
        final_state = None

        # executer l'algo:
        for _ in range(num_steps):
            final_state = game_of_life(initial_state)
            if args.verbose:
                display_state(final_state, title="INTERMEDIARY")
        # On sait que le jeu est theoriquement infini mais le final ici fais reference au dernier step
        display_state(final_state, title="FINAL")
        if args.output_file:
            with open(args.output_file, "a") as f:
                for line in final_state:
                    f.write(" ".join(map(str, line))+"\n")
            print("Resultat sauvegardé dans: " + args.output_file)

    else:
        print("Jeu de la vie de conway")
        print("\n================================")
        print("Arguments:")
        print("\t --input \t\t fichier contenant un etat initial de la matrice")
        print("\t --num-steps \t\t nombre d'etapes a executer")
        print("\t --output-file \t\t fichier de sortie")
        print("\t --verbose \t\t afficher les etats intermediaires")