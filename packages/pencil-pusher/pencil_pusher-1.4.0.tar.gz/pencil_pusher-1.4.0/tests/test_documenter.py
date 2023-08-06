from pencil_pusher.documenter import Documenter
import os


def test_gen_local():
    """
    Tests generating a doc with a
    local file
    """
    Documenter.generate("pencil_pusher.documenter", "test")
    assert os.path.isfile("./test.md")
    os.remove("./test.md")


def test_toc():
    """
    Tests that toc is generated correctly
    """

    test_files = [
        "pencil_pusher.configs.base.py",
        "pencil_pusher.configs.manager.py",
        "pencil_pusher.configs.python_lang.py",
        "pencil_pusher.documenter.py",
        "pencil_pusher.input.py",
    ]

    test_file_map = {
        ".".join(i.split(".")[:-1]): ".".join(i.split(".")[:-1])
        for i in test_files
    }
    toc_tree = Documenter.build_toc(test_files)

    assert toc_tree == {
        "pencil_pusher": {
            "configs": {"base": {}, "manager": {}, "python_lang": {}},
            "documenter": {},
            "input": {},
        }
    }

    Documenter.generate_sidebar(toc_tree, test_file_map)

    os.remove("./_Sidebar.md")
