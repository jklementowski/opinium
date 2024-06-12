# conftest.py

import pytest

def pytest_collection_modifyitems(config, items):
    if config.option.suite:
        selected_suite = config.option.suite
        selected_items = []
        deselected_items = []

        for item in items:
            if getattr(item.function, 'suite', None) == selected_suite:
                selected_items.append(item)
            else:
                deselected_items.append(item)

        items[:] = selected_items
        config.hook.pytest_deselected(item=deselected_items)

def pytest_addoption(parser):
    parser.addoption("--suite", action="store", default=None, help="Specify the test suite to run")
    