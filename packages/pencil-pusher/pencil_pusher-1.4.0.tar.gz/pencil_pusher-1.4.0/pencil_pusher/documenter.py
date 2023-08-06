from typing import Dict, List, Set
from pencil_pusher.process_util import ProcessUtil


class Documenter:
    @staticmethod
    def install():
        """
        installs the correct pydoc-markdown package
        to the python version being used to execute
        the commands
        """
        ProcessUtil.execute(
            ["python3", "-m", "pip", "install", "pydoc-markdown"]
        )

    @staticmethod
    def generate(module: str, title: str = "", output_dir: str = "./"):
        """
        Generates markdown documentation for a given
        module (.py file) and creates a file with the
        name title as the documentation output

        Args:
            module (str): the name of the module the file is being
                imported from
            title (str): the title of the document file to output
            output_dir (str): the directory to write the output file to
        """
        options = '{renderer: {type: markdown,descriptive_class_title: false,render_toc: true, header_level_by_type: {"Module": 1,"Class": 2,"Method": 3,"Function": 2,"Data": 2}}}'
        if not output_dir.endswith("/"):
            output_dir += "/"

        fp = open(f"{output_dir}{title}.md", "w")
        ProcessUtil.execute(
            ["pydoc-markdown", "-m", f"{module}", options], stdout=fp
        )
        fp.close()

    @staticmethod
    def build_toc(file_list: List[str]) -> Dict[str, str]:
        """
        Builds the table of contents from a file list
        assumes that the files are in python import notation

        Args:
            file_list (List[str]): the list of files to include
                the in the toc

        Returns:
            Dict[str, str]: the table of contents ordered as a
                dictionary

        """
        hierarchy = {}
        for file_path in file_list:
            parts = file_path.split(".")

            sub_heirarchy = hierarchy

            # exclude file extension
            for part in parts[:-1]:
                if part not in sub_heirarchy:
                    sub_heirarchy[part] = {}
                sub_heirarchy = sub_heirarchy[part]

        return hierarchy

    @staticmethod
    def generate_sidebar(
        toc: Dict[str, str], file_map: Dict[str, str], output_dir: str = "./"
    ):
        """

        The Sidebar takes the following format

        -- user-defined toc (not implemented)

        -- References
        -- custom TOC
        """
        fp = open(f"{output_dir}_Sidebar.md", "w")
        Documenter.sidebar_helper("", toc, file_map, fp, output_dir)

        fp.close()

    @staticmethod
    def sidebar_helper(
        prefix: str,
        toc: Dict[str, str],
        file_map: Dict[str, str],
        fp,
        output_dir: str = "./",
        level: int = 0,
    ):
        """
        """
        included = []
        for entry, value in toc.items():
            path = entry if prefix == "" else f"{prefix}.{entry}"
            if value == {}:
                # no sub entries, write to TOC
                fp.write(
                    Documenter.toc_entry(
                        entry, f"{output_dir}{file_map[path]}.md", level
                    )
                    + "\n"
                )
            else:
                # TODO make this generate a header page
                if entry not in included:
                    included.append(entry)
                    fp.write(Documenter.toc_header(entry, level) + "\n")
                Documenter.sidebar_helper(
                    path, value, file_map, fp, output_dir, level + 1
                )

    @staticmethod
    def toc_entry(title: str, path: str, level: int = 0):
        """
        """
        initial_spacing = " " * level * 2

        return f"{initial_spacing}- **[{title}]({path})**"

    @staticmethod
    def toc_header(title: str, level: int = 0):
        """
        """
        initial_spacing = " " * level * 2

        # TODO add header page link
        return f"{initial_spacing}- **[{title}]()**"
