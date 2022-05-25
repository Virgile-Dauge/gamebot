# Licence

# [[file:readme.org::*Licence][Licence:1]]
# This file is part of Invabot.

# Invabot is free software: you can redistribute it
# and/or modify it under the terms of the GNU General
# Public License as published by the Free Software
# Foundation, either version 3 of the License, or
# any later version.

# Invabot is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the
# implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE. See the GNU General Public License
# for more details.

# You should have received a copy of the GNU General
# Public License along with Invabot. If not, see
# <https://www.gnu.org/licenses/>
# Licence:1 ends here

# Dépendances

# [[file:readme.org::*Dépendances][Dépendances:1]]
import disnake
from disnake.ext import commands
from disnake import Embed, Emoji

from tinydb import TinyDB, Query

import requests

import pprint
# Dépendances:1 ends here

# Déclaration du bot :

# [[file:readme.org::*Déclaration du bot :][Déclaration du bot ::1]]
bot = commands.Bot(
            intents=disnake.Intents().all(),
            test_guilds=[955171411780046859], # Optional
            sync_commands_debug=True
        )
# Déclaration du bot ::1 ends here

# Déclaration de la Base de données


# [[file:readme.org::*Déclaration de la Base de données][Déclaration de la Base de données:1]]

# Déclaration de la Base de données:1 ends here

# Récupération du token Rawg

# [[file:readme.org::*Récupération du token Rawg][Récupération du token Rawg:1]]
with open('rawg.token', 'r') as datafile:
    token = datafile.read().replace('\n', '')
# Récupération du token Rawg:1 ends here

# Ajouter un jeu

# [[file:readme.org::*Ajouter un jeu][Ajouter un jeu:1]]
@bot.slash_command()
async def ajouter(ctx: disnake.ApplicationCommandInteraction, nom: str):
    """Liste les jeux de la commu

        Parameters
        ----------
        nom: Nom du jeu
    """
    await ctx.response.defer()
    payload = {'key': token, 'search': nom,
               'search_exact': True,
               'exclude_additions': True,
               'platforms': '4'}
    response = requests.get('https://api.rawg.io/api/games', params=payload)
    l = response.json()['results']

    if len(l) != 1:
        # Mécanisme de séléction par l'utilisateur à implémenter
        propositions = [g['name'] for g in l]
        await ctx.edit_original_message(content=propositions)

    id = l[0]['id']
    payload = {'key': token}
    response = requests.get(f'https://api.rawg.io/api/games/{id}', params=payload)
    l = response.json()
    pprint.pprint(l)
# Ajouter un jeu:1 ends here

# Lister les jeux dispos

# [[file:readme.org::*Lister les jeux dispos][Lister les jeux dispos:1]]
@bot.slash_command()
async def list(ctx: disnake.ApplicationCommandInteraction):
    """Liste les jeux de la commu

        Parameters
        ----------
    """
    print('coucou')
# Lister les jeux dispos:1 ends here

# Point de départ du script

# [[file:readme.org::*Point de départ du script][Point de départ du script:1]]
def main():
    bot.run(token=open("bot.token").read().replace('\n', ''))
if __name__ == "__main__":
    main()
# Point de départ du script:1 ends here
