"""
Scripts do console
"""
from kt_cambio import app
import click


@click.command()
@click.argument("brl", type=float)
@click.option("--cambio", "-c", type=float, default=5.5)
def brlusd(brl, cambio):
    usd = brl / cambio
    click.echo("%.2f" % usd)
    return 0


@click.command()
@click.argument("usd", type=float)
@click.option("--cambio", "-c", type=float, default=5.5)
def usdbrl(usd, cambio):
    brl = usd * cambio
    click.echo("%.2f" % brl)
    return 0
