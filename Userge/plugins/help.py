from pyrogram import Message
from Userge import userge

log = userge.getLogger(__name__)


@userge.on_message(userge.cmd("help"))
async def helpme(_, message: Message):
    out_str = ""
    for cmd in userge.get_help():
        out_str += f".{cmd} : {userge.get_help(cmd)}\n"
    await message.edit(out_str)


userge.add_help(
    command="help",
    about="to know how to use this"
)