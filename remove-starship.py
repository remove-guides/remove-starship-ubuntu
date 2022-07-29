#!/bin/python3

import os
import sys

USER = os.environ.get("SUDO_USER")
HOME = f'/home/{USER}'
RED = "\033[31m"


def remove_files():
    try:
        os.system(f'rm -rf {HOME}/.config/starship.toml')
        os.system('rm -rf $STARSHIP_CONFIG')
        os.system(f'rm -rf {HOME}/.cache/starship')
        os.system('rm -rf $STARSHIP_CACHE')
        os.system('rm -rf /usr/local/bin/starship')
    except:
        print(f"\n{RED} Failed on remove files! \n")


def update_files():
    try:
        os.system(
            f"""sed -i -e '/eval "$(starship init bash)"/d' {HOME}/.bashrc""")
        os.system(
            f"""sed -i -e '/eval (starship init elvish)/d' {HOME}/.elvish/rc.elv""")
        os.system(
            f"""sed -i -e '/starship init fish | source/d' {HOME}/.config/fish/config.fish""")
        os.system(
            f"""sed -i -e '/eval $(starship init ion)/d' {HOME}/.config/ion/initrc""")
        os.system(
            f"""sed -i -e '/eval `starship init tcsh`/d' {HOME}/.tcshrc""")
        os.system(
            f"""sed -i -e '/execx($(starship init xonsh))/d' {HOME}/.xonshrc""")
        os.system(
            f"""sed -i -e '/eval "$(starship init zsh)"/d' {HOME}/.zshrc""")
    except:
        print(f"\n{RED} Failed on update files! \n")


def main():
    remove_files()
    update_files()


if __name__ == '__main__':
    user_type = os.getuid()

    if(user_type != 0):
        print(f"\n{RED} Please Run as Root! \n")
        sys.exit(1)

    main()
