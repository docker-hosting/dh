import click
from commands.create import create
from commands.cd import cd
from commands.backup import backup
from commands.restore import restore
from commands.daemon import daemon

@click.group()
@click.option('--basedir', default='/var/www', help='Defines the base directory of your websites.')
@click.pass_context
def cli(ctx, basedir):
    ctx.obj['BASEDIR'] = basedir

if __name__ == '__main__':
    cli.add_command(create)
    cli.add_command(cd)
    cli.add_command(backup)
    cli.add_command(restore)
    cli.add_command(daemon)
    cli(obj={})
