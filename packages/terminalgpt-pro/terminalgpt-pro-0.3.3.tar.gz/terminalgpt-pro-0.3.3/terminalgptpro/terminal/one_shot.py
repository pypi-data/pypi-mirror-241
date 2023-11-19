from terminalgptpro.chat import ChatManager
from terminalgptpro.encryption import EncryptionManager
from terminalgptpro.printer import Printer, PrintUtils
from terminalgptpro import config

def one_shot_message(ctx, question):
    chat_manager: ChatManager = ctx.obj["CHAT"]
    enc_manager: EncryptionManager = ctx.obj["ENC_MNGR"]
    printer: Printer = ctx.obj["PRINTER"]

    enc_manager.set_api_key()

    messages = [config.INIT_SYSTEM_MESSAGE]

    messages.append({"role": "user", "content": question})

    printer.printt("")
    answer = chat_manager.get_user_answer(messages=messages)
    message = answer["choices"][0]["message"]["content"]

    printer.print_assistant_message(message)
