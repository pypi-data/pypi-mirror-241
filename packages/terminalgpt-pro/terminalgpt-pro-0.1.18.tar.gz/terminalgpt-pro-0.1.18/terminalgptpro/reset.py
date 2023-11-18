# reset.py

import click
import os
import json
from terminalgptpro.printer import PrinterFactory
from terminalgptpro.printer import Printer
from terminalgptpro import config

@click.command(help="Reset all configuration files.")
def run_reset():
    printer: Printer = PrinterFactory.get_printer("plain")

    try:
        # Удаление файлов конфигурации
        os.remove(config.SECRET_PATH)
        os.remove(config.DEFAULTS_PATH)
        os.remove(config.CONVERSATIONS_PATH)

        # Создание папок и файлов заново
        if not os.path.exists(os.path.dirname(config.SECRET_PATH)):
            os.makedirs(os.path.dirname(config.SECRET_PATH))

        if not os.path.exists(config.CONVERSATIONS_PATH):
            os.mkdir(config.CONVERSATIONS_PATH)

        # Сохранение начальных значений в файлы конфигурации
        initial_model = config.get_default_config().get("model", "gpt-3.5-turbo")
        initial_style = config.get_default_config().get("style", "markdown")

        with open(config.DEFAULTS_PATH, "w", encoding="utf-8") as file:
            json.dump({"model": initial_model, "style": initial_style}, file)

        printer.printt("Configuration files have been reset successfully.")

    except Exception as e:
        printer.printt(f"An error occurred while resetting configuration: {e}.")


run_reset()
