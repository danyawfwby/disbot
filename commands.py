import with_db
import discord

def get_last_user(): # autorole when join
    return with_db.exec_sql("SELECT * FROM users ORDER BY id DESC LIMIT 1")

def get_user_by_discord_id(id): # autorole when join and when verify
    return with_db.exec_sql("SELECT * FROM users WHERE discord_id=?", (id,))

def add_new_user(args): # autorole when join
    with_db.exec_sql("INSERT INTO users(id, discord_id, coins, warns, name, is_verify, lvl, referer, cps) VALUES( ?, ?, ?, ?, ?, ?, ?, ?, ?)", (args))

def delete_user(id): # ban
    with_db.exec_sql("DELETE from users where discord_id = ?", (id,))

def set_verify(id):
    with_db.exec_sql("Update users set is_verify = 1 where discord_id = ?", (id,))

def plus_warn_user(id): # warn
    with_db.exec_sql("Update users set warns = warns + 1 where discord_id = ?", (id,))
    row = get_user_by_discord_id(id)
    if(len(row[1])):
        name_cell = row[0].index("warns")
        count_warns = row[1][0][name_cell]
        return count_warns

async def warn(ctx, id):
    try:
        id = int(id)
        is_admin = ctx.message.author.guild_permissions.administrator
        author_id = ctx.message.author.id
        if(is_admin and author_id != id):
            count_warns = plus_warn_user(id)
            color=discord.Colour.from_str("#ff0000")
            embed=discord.Embed(colour=color)
            if(count_warns >= 3):
                await ctx.guild.get_member(id).ban()
                embed.description = "Пользователь заблокирован, т.к. получил 3 предупреждение."
            else:
                embed.description = f"Пользователю выдано {count_warns}/3 предупреждений."

            await ctx.send(embed=embed)
    except Exception as e:
        print(f"Произошла ошибка: {e}")

async def set_referer(ctx, id):
    try:
        id = int(id)
        author_id = ctx.message.author.id
        row = get_user_by_discord_id(author_id)
        if(len(row[1])):
            name_cell = row[0].index("referer")
            referer = row[1][0][name_cell]
            if(not referer):
                with_db.exec_sql("Update users set referer = ? where discord_id = ?", ( id, author_id, ))
                color=discord.Colour.from_str("#0aff00")
                embed=discord.Embed(colour=color)
                embed.description = f"Вы успешно указали своего реферера."
                await ctx.send(embed=embed)
    except Exception as e:
        print(f"Произошла ошибка: {e}")