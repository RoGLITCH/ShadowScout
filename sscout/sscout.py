import click
from rich.console import Console

console = Console()

# Your ASCII logo (keep it short for clean CLI output)
LOGO = r"""

  ▄▄▄▄  █                 █                 ▄▄▄▄                         ▄
 █▀   ▀ █ ▄▄    ▄▄▄    ▄▄▄█   ▄▄▄  ▄     ▄ █▀   ▀  ▄▄▄    ▄▄▄   ▄   ▄  ▄▄█▄▄
 ▀█▄▄▄  █▀  █  ▀   █  █▀ ▀█  █▀ ▀█ ▀▄ ▄ ▄▀ ▀█▄▄▄  █▀  ▀  █▀ ▀█  █   █    █
     ▀█ █   █  ▄▀▀▀█  █   █  █   █  █▄█▄█      ▀█ █      █   █  █   █    █
 ▀▄▄▄█▀ █   █  ▀▄▄▀█  ▀█▄██  ▀█▄█▀   █ █   ▀▄▄▄█▀ ▀█▄▄▀  ▀█▄█▀  ▀▄▄▀█    ▀▄▄


"""


@click.group(invoke_without_command=True)
@click.option('--version', is_flag=True, help='Show version and exit.')
@click.pass_context
def main(ctx, version):
    """ShadowScout - Active Directory Reconnaissance Framework."""
    if ctx.invoked_subcommand is None:
        console.print(f"[bold red]{LOGO}[/bold red]")
        console.print("[cyan]Welcome to ShadowScout v1.0[/cyan]\n")
        console.print("[yellow]Use 'sscout --help' to see available commands.[/yellow]")
    if version:
        console.print("[green]ShadowScout v1.0[/green]")


@main.command()
@click.argument("ip_range", required=False)
@click.pass_context
def enum_hosts(ctx, ip_range):
    print(ip_range or "Hello World")

if __name__ == "__main__":
    main()
