#!/usr/bin/env python3
import click
import sys
import os
import platform
import json
from os.path import abspath, expanduser, normpath, exists, basename

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
config = dict()

def choose(win, unix):
    return win if platform.system() == 'Windows' else unix

def texpath():
    return abspath(expanduser(f"{config['path']}/texpj-template")) 

def destroyTemplate(dir):
    if not os.path.isdir(dir):
        os.remove(dir)
        return

    if dir[-1] == os.sep: dir = dir[:-1]
    files = os.listdir(dir)
    for file in files:
        if file == '.' or file == '..': continue
        path = dir + os.sep + file
        if os.path.isdir(path):
            destroyTemplate(path)
        else:
            os.unlink(path)
    os.rmdir(dir)

LN=choose('mklink /D', 'ln -s')


@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    """
    Utilidad para manejo de plantillas de latex por consola.

    Utilice:

    $ texpj comando -h

    Para obtener una mayor información sobre el comando.
    """
    global config

    config['path'] = choose('c:\\data\\documents', '~/Documents')

    pconf = f"{click.get_app_dir('texpj')}/config.json"
    

    if not exists(pconf):
        print('Como primer paso complete la configuración')
        print(f'\n\tPuede consultar las configuraciones en {click.get_app_dir("texpj")}/config.json')
        print('')
        print('En el directorio ingresado se creará el directorio "texpj-template"')
        response = config['path']
        while True:
            response = input(f'Directorio (default {config["path"]}): ')
            if exists(abspath(expanduser(response))):
                config['path'] = normpath(response)
                if not exists(texpath()): 
                    os.mkdir(f"{texpath()}")
                break;
            print(f'El directorio {response} no existe!')

        if not exists(click.get_app_dir('texpj')):
            os.mkdir(click.get_app_dir('texpj'))

    
        with open(pconf, 'w') as fconf:
            json.dump(config, fconf, indent=2)

    with open(pconf, 'r') as fconf:
        config = json.load(fconf)


@main.command()
@click.argument('template')
@click.argument('alias')
@click.option('--url/--no-url', default=False, help="indica si es un url")
def install(template, alias, url):
    """
    Instala el TEMPLATE de forma local y lo regitra como ALIAS.

    Descarga un repositorio con el comando git. 'user/repo-name' bastará si es un 
    repositorio de Github sino
    puede utilizar un url activando la opción --url.
    
    \b
    Ejemplo:
    $ texpj install BenyaminGaleano/report
    $ texpj install https://github.com/BenyaminGaleano/report.git --url
    """
    print(f'Falta implementación, {template} {alias} url:{url}')


@main.command()
@click.argument('alias')
def update(alias):
    """
    Actualiza el template identificado con el ALIAS.
    """
    print(f'Falta implementación, {alias}')


@main.command()
@click.argument('directory')
@click.argument('alias')
def add(directory, alias):
    """
    Registra DIRECTORY como una plantilla de latex y lo identifica con ALIAS.

    \b
    $ texpj add . elec_doc
    $ texpj add reporte report
    """
    print(f"{LN} {abspath(expanduser(directory))} {texpath()}/{alias}")
    os.system(f"{LN} {abspath(expanduser(directory))} {texpath()}/{alias}")


@main.command()
@click.argument('alias')
def remove(alias):
    """
    Elimina la plantilla identificada como ALIAS, si es un enlace simbólico, no elimina
    el contenido (si fue agregado con texpj add ...).
    """
    if alias == None:
        return

    destroyTemplate(f"{texpath()}/{alias}")

@main.command()
def list():
    print("Plantillas en el directorio:")
    for template in os.listdir(texpath()):
        if not os.path.isdir(f"{texpath()}/{template}"):
            continue
        print(f'\t{template}')

@main.command()
@click.argument('alias')
@click.argument('name')
@click.option('--directory', '-d', help="directorio base")
def create(alias, name, directory):
    """
    Crea una copia del template registrado como ALIAS en la posición actual o en 
    el directorio indicado con -d con el nombre NAME.

    \b
    $ texpj create report lab1
    $ texpj create report lab1 -d ~/documentos/latex
    """
    print(f'Falta implementación, {alias}, {name}, {directory}')

if __name__ == "__main__":
    main()

