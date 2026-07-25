import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

# Bot Setup
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix=os.getenv('PREFIX', '!'), intents=intents)

# Global ticket counter
ticket_counter = 0

@bot.event
async def on_ready():
    print(f'✅ Bot conectado como {bot.user}')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{os.getenv('PREFIX', '!')}help | Tickets"))

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    
    await bot.process_commands(message)

# Commands
@bot.command(name='create', help='Cria um novo ticket de suporte')
async def create_ticket(ctx):
    try:
        global ticket_counter
        ticket_counter += 1
        
        ticket_name = f"ticket-{ctx.author.name}-{ticket_counter}"
        
        # Create channel with permissions
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(view_channel=False),
            ctx.author: discord.PermissionOverwrite(
                view_channel=True,
                send_messages=True,
                read_message_history=True
            )
        }
        
        channel = await ctx.guild.create_text_channel(ticket_name, overwrites=overwrites)
        
        # Send embed
        embed = discord.Embed(
            title="🎫 Ticket Criado",
            description=f"Ticket #{ticket_counter} foi criado com sucesso!",
            color=discord.Color.green()
        )
        embed.add_field(name="Usuário", value=ctx.author.mention, inline=True)
        embed.add_field(name="Status", value="🟢 Aberto", inline=True)
        embed.add_field(
            name="Comandos",
            value="`!close` - Fechar ticket\n`!add <user>` - Adicionar usuário\n`!remove <user>` - Remover usuário",
            inline=False
        )
        embed.set_footer(text="Discord Ticket Bot")
        
        await channel.send(f"Bem-vindo {ctx.author.mention}! Este é seu ticket de suporte.")
        await channel.send(embed=embed)
        
        await ctx.reply(f"✅ Ticket criado! Acesse {channel.mention}")
        
    except Exception as e:
        print(f"Erro: {e}")
        await ctx.reply("❌ Erro ao criar ticket.")

@bot.command(name='close', help='Fecha o ticket atual')
async def close_ticket(ctx):
    try:
        if ctx.channel.name.startswith('ticket-'):
            embed = discord.Embed(
                title="🔒 Ticket Fechado",
                description="Este ticket será deletado em 5 segundos...",
                color=discord.Color.red()
            )
            embed.set_footer(text="Discord Ticket Bot")
            
            await ctx.send(embed=embed)
            
            import asyncio
            await asyncio.sleep(5)
            await ctx.channel.delete()
        else:
            await ctx.reply("❌ Este comando só funciona em tickets!")
    except Exception as e:
        print(f"Erro: {e}")
        await ctx.reply("❌ Erro ao fechar ticket.")

@bot.command(name='add', help='Adiciona um usuário ao ticket')
async def add_user(ctx, user: discord.Member = None):
    try:
        if user is None:
            await ctx.reply("❌ Mencione um usuário para adicionar!")
            return
        
        if not ctx.channel.name.startswith('ticket-'):
            await ctx.reply("❌ Este comando só funciona em tickets!")
            return
        
        await ctx.channel.set_permissions(
            user,
            view_channel=True,
            send_messages=True,
            read_message_history=True
        )
        
        await ctx.reply(f"✅ {user.mention} foi adicionado ao ticket!")
        
    except Exception as e:
        print(f"Erro: {e}")
        await ctx.reply("❌ Erro ao adicionar usuário.")

@bot.command(name='remove', help='Remove um usuário do ticket')
async def remove_user(ctx, user: discord.Member = None):
    try:
        if user is None:
            await ctx.reply("❌ Mencione um usuário para remover!")
            return
        
        if not ctx.channel.name.startswith('ticket-'):
            await ctx.reply("❌ Este comando só funciona em tickets!")
            return
        
        await ctx.channel.set_permissions(
            user,
            view_channel=False,
            send_messages=False
        )
        
        await ctx.reply(f"✅ {user.mention} foi removido do ticket!")
        
    except Exception as e:
        print(f"Erro: {e}")
        await ctx.reply("❌ Erro ao remover usuário.")

@bot.command(name='help', help='Mostra os comandos disponíveis')
async def help_command(ctx):
    embed = discord.Embed(
        title="📋 Comandos de Tickets",
        description="Lista de comandos disponíveis:",
        color=discord.Color.blue()
    )
    embed.add_field(name="!create", value="Cria um novo ticket", inline=False)
    embed.add_field(name="!close", value="Fecha o ticket atual", inline=False)
    embed.add_field(name="!add <user>", value="Adiciona um usuário ao ticket", inline=False)
    embed.add_field(name="!remove <user>", value="Remove um usuário do ticket", inline=False)
    embed.add_field(name="!help", value="Mostra esta mensagem", inline=False)
    embed.set_footer(text="Discord Ticket Bot")
    
    await ctx.reply(embed=embed)

# Run bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("❌ DISCORD_TOKEN não encontrado no .env!")
    else:
        bot.run(token)
