import commands

async def when_join(member):
    row = commands.get_last_user()
    discord_id = member.id
    id = row[1][0][0]+1

    is_added = commands.get_user_by_discord_id(discord_id)
    if(not len(is_added[1])):
        will_name = f"ПОМИДОР {id}";
        commands.add_new_user((id, discord_id, 0, 0, will_name, 0, 0, 0, 1))
    else:
        row = commands.get_user_by_discord_id(discord_id)
        name_cell = row[0].index("name")
        will_name = row[1][0][name_cell]
    
    await member.edit(nick=will_name)
    role = member.guild.get_role(1044643847717789716)
    await member.add_roles(role)

async def when_verify(member):
    discord_id = member.id
    name = member.name
    row = commands.get_user_by_discord_id(discord_id)
    if(len(row[1])):
        name_cell = row[0].index("name")
        need_name = row[1][0][name_cell]
        if(name == need_name):
            commands.set_verify(discord_id)
            role = member.guild.get_role(1044643847717789716)
            await member.remove_roles(role)