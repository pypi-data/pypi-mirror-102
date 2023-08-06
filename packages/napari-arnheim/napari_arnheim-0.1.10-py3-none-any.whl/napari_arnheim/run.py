from grunnlag.schema import Representation
from bergen.console import console
from napari_arnheim.context import gui_qt
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('--config', help='Which config file to use', default="bergen.yaml", type=str)
args = parser.parse_args()


def main():
    print(args)

    bergen_params = {
        "config_path": args.config
    }

    with gui_qt(bergen_params=bergen_params) as interface:

        @interface.client.enable()
        async def show(rep: Representation) -> Representation:
            """Show

            Shows an image of an astronaut

            Args:
                rep (Representation): The displayable Representation

            Returns:
                Representation: Passthrough
            """
            try:
                interface.helper.openRepresentationAsLayer(rep=rep)
            except:
                console.print_exception()
            return rep

        interface.client.provide()


if __name__ == "__main__":
    main()