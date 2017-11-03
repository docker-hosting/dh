import click
import os
import glob
import shutil
import zipfile
from urllib.request import urlretrieve

@click.command()
@click.argument('template_name')
@click.argument('website_name', type=click.Path())
@click.pass_context
def create(ctx, template_name, website_name):
    """Creates a new website based on a template.

Usage:

    dh create <template_name> <website_name>

Arguments:

    <TEMPLATE_NAME>

        One of the template repositories on the docker hosting github account, but without the -template suffix.

    <WEBSITE_NAME>

        The name of the website.

"""
    try:
        # Check if the destination directory already exists
        path = os.path.join(ctx.obj['BASEDIR'], website_name)
        if os.path.exists(path):
            answer = input('Do you want to delete the existing directory? [Y] ')
            if answer.lower() == 'y' or answer == '':
                shutil.rmtree(path)

        # Generate github repo string
        github_name = template_name
        if '/' not in template_name:
            github_name = 'docker-hosting/%s-template' % template_name
        
        # Try to download repository
        link = 'https://github.com/%s/archive/master.zip' % github_name
        urlretrieve(link, 'master.zip')

        # Unzip downloaded file to destination directory
        zip_ref = zipfile.ZipFile('master.zip', 'r')
        zip_ref.extractall(path)
        zip_ref.close()

        # The destination folder contains another folder named [github-repo-name]-master.
        # We need to move all files within this directory and delete it afterwards.
        repo_name = github_name.split('/')[1]
        master_dir = os.path.join(path, repo_name + '-master')
        for file in os.listdir(master_dir):
            shutil.move(os.path.join(master_dir, file), path)
        os.rmdir(os.path.join(path, repo_name + '-master'))

        # Now remove the file master.zip
        os.remove('master.zip')
    except PermissionError as e:
        # TODO: handle and log exceptions
        print('%s\n%s' % (e, 'Note: Try to running this program as Administrator.'))
    except Exception as e:
        # TODO: handle and log exceptions
        print(e)
