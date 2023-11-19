from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

import click
from rich import print as rp

from hk_horn import HornAPI
from hk_horn.enums import ModAttrs
from hk_horn.models import Mod

if TYPE_CHECKING:
	from typing import Any


CONTEXT_SETTINGS = {'help_option_names': ['-h', '--help']}


def get_version_from_pyproject_toml(fp: str | Path = Path('pyproject.toml')) -> str:
	fp = Path(fp)
	if not fp.exists():
		return '-'

	with open(fp, 'r') as ppt:
		for line in ppt.readlines():
			if 'version = ' in line:
				sv = line.split()[-1]
				if '"' in sv:
					sv = sv[1:-1]
				return sv

	return '--'


horn: HornAPI = HornAPI  # type: ignore


@click.group(context_settings=CONTEXT_SETTINGS)
@click.version_option(version=get_version_from_pyproject_toml())
def cli():
	global horn
	# TODO: Handle update command(s) before init..
	horn.update_repo()
	horn = horn()


# TODO: (Auto) Check & Update modlinks repo
# TODO: ...
# TODO: Mod/Package remove command..
# TODO: Mod/Package disable command..
# TODO: Command to manage & install HKMA..
# TODO: Command to set/download/manage repo list
# TODO: Configs..


def parse_opts(
	opts: dict[str, Any],
	*,
	name_equal: bool = True,
) -> None:
	_re_eq = lambda s: f'^{s}$'  # noqa: E731
	if ModAttrs.name in opts:
		if 'case' in opts:
			if opts['case']:
				opts[ModAttrs.name] = f'(?i){opts[ModAttrs.name]}'
			del opts['case']
		if name_equal:  # TODO: More things..
			opts[ModAttrs.name] = _re_eq(opts[ModAttrs.name])


@cli.command()
@click.option('--name', help='Mod name')
@click.option('--case', is_flag=True, default=True, help="Don't ignore case on search")
@click.option('--version', default='*', help='Set version search for..')
def find(**options: str) -> None:
	# TODO: Flex versions search..
	parse_opts(options, name_equal=False)
	mods = horn.find_mod_by(fields=options)
	if not mods:  # FIXME: Duplicate..
		rp('No results found..')
		return

	if isinstance(mods, Mod):  # FIXME: Duplicate..
		mods = (mods,)

	for mod in mods:
		rp(f"'{mod.name}'", mod.version)


@cli.command()
@click.argument('name')
@click.option('--version', default='*', help='Set version info about..')
def info(*, name: str, version: str) -> None:
	# TODO: Flex versions search..

	fields = {ModAttrs.name: name, ModAttrs.version: version}

	parse_opts(fields)

	mod = horn.find_mod_by(
		fields=fields,
		stop=1,  # TODO: raise/print/log Error or etc. handling here on more results..
	)
	if not mod:  # FIXME: Duplicate..
		rp('No results found..')
		return

	# if isinstance(mods, Mod):  # FIXME: Duplicate..
	# 	mods = (mods,)

	# TODO: Better format info..
	rp(mod)


# TODO: Game paths groups with config..
@cli.command()
@click.argument('name')
@click.option('--path', help='Path to install mod', required=True)
@click.option('--version', default='*', help='Set version install for..')
def install(*, name: str, version: str, path: str) -> None:
	# TODO: Install multiple packages.
	# TODO: Multiple async & parallel installation XD
	# TODO: Flex versions search..

	status = horn.install(
		name=name,
		version=version,
		path=Path(path),
	)
	if not status:
		rp('Status: ', '[red]Fail')
		return

	# if isinstance(mods, Mod):  # FIXME: Duplicate..
	# 	mods = (mods,)

	# TODO: Better format info..
	rp('Status: ', '[green]OK')


if __name__ == '__main__':
	cli()
