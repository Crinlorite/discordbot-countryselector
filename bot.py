import discord
import json
import os

with open('config.json') as f:
    config = json.load(f)

with open('countries.json') as f:
    countries = json.load(f)

TOKEN = config["discord_token"]
GUILD_ID = int(config["guild_id"])
CHANNEL_ID = int(config["channel_id"])

MESSAGE_RECORD_FILE = 'published.json'

intents = discord.Intents.default()
intents.reactions = True
intents.guilds = True
intents.members = True

client = discord.Client(intents=intents)

# Cargar mensajes previamente guardados
if os.path.exists(MESSAGE_RECORD_FILE):
    with open(MESSAGE_RECORD_FILE) as f:
        published_messages = json.load(f)
else:
    published_messages = {}

@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")
    guild = client.get_guild(GUILD_ID)
    channel = guild.get_channel(CHANNEL_ID)

    for region, emoji_map in countries.items():
        # Si ya tenemos message_id guardado, comprobar si existe
        message_id = published_messages.get(region)
        message = None
        if message_id:
            try:
                message = await channel.fetch_message(message_id)
                print(f"Mensaje existente encontrado para {region}")
            except discord.NotFound:
                print(f"Mensaje para {region} no encontrado, se creará uno nuevo")

        if not message:
            embed = discord.Embed(title=f"🌍 {region}",
                                  description=config["message"],
                                  color=0x00ff00)
            message = await channel.send(embed=embed)
            published_messages[region] = message.id
            print(f"Mensaje creado para {region}")
            for emoji in emoji_map.keys():
                await message.add_reaction(emoji)

    # Guardar los message_ids actualizados
    with open(MESSAGE_RECORD_FILE, 'w') as f:
        json.dump(published_messages, f, indent=4)

@client.event
async def on_raw_reaction_add(payload):
    if payload.member.bot:
        return

    guild = client.get_guild(payload.guild_id)

    for region, emoji_map in countries.items():
        if payload.emoji.name in emoji_map:
            role_name = emoji_map[payload.emoji.name]
            role = discord.utils.get(guild.roles, name=role_name)
            if role is None:
                role = await guild.create_role(name=role_name, hoist=True)
            member = guild.get_member(payload.user_id)
            await member.add_roles(role)
            print(f"Rol '{role_name}' asignado a {member.display_name}")

@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)

    for region, emoji_map in countries.items():
        if payload.emoji.name in emoji_map:
            role_name = emoji_map[payload.emoji.name]
            role = discord.utils.get(guild.roles, name=role_name)
            if role:
                await member.remove_roles(role)
                print(f"Rol '{role_name}' removido de {member.display_name}")

client.run(TOKEN)