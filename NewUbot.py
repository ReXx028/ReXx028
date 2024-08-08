from telethon import TelegramClient, events
import os


api_id = 'ipidlu'  
api_hash = 'iphashlu'  
phone_number = '+62nomorlu'  

session_file = 'session_name.session'


if os.path.exists(session_file):
    os.remove(session_file)

client = TelegramClient('session_name', api_id, api_hash)

async def main():
    await client.start(phone=phone_number)

    @client.on(events.NewMessage(pattern='/start'))
    async def start_handler(event):
        await event.respond('Halo! Saya adalah bot Telegram pribadi Anda.')

    @client.on(events.NewMessage(pattern='/cek'))
    async def cek_handler(event):
        args = event.message.message.split()
        if len(args) != 2:
            await event.respond('Gunakan format: /cek [nik]')
            return

        nik = args[1]
        info = check_nik(nik)
        await event.respond(info)

    @client.on(events.NewMessage(pattern='.gcas'))
    async def gcas_handler(event):
        message = event.message.message
        msg_to_send = message.split(' ', 1)[1] if ' ' in message else ''
        
        if not msg_to_send:
            await event.respond('Gunakan format: .gcas [pesan]')
            return

        
        async for dialog in client.iter_dialogs():
            if dialog.is_group or dialog.is_user:
                try:
                    await client.send_message(dialog.id, msg_to_send)
                except Exception as e:
                    print(f"Gagal mengirim pesan ke {dialog.name}: {e}")
        
        await event.respond('Pesan telah dikirim ke semua grup dan chat.')

    print("Bot sudah berjalan...")
    await client.run_until_disconnected()

def check_nik(nik):
    
    return f'Informasi untuk NIK {nik}: ...'

if __name__ == '__main__':
    with client:
        client.loop.run_until_complete(main())
