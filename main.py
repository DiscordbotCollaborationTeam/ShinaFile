@bot.command()
async def sendlevels(ctx,name=None,ct:int=-1):
    if name==None:
        await ctx.send("中の引数には まみ か りんご が入ります。1Level=1(それぞれの通貨)です。")
    with open("level/level.json", 'r') as lu:
        dlu = json.load(lu)
    if dlu[str(ctx.message.author.id)]["level"] < ct:
        await ctx.send(f"エラー:レベル不足{l}<{ct}")
    elif ct<0:
        await ctx.send(f"エラー:不適切な送信レベル{ct}")
    elif name=="まみ":
        if str(bot.get_guild(536025319963099165).get_member(479506436142006282).status)=="offline":
            await ctx.send("エラー:相手がオフライン")
        else:
            c = bot.get_channel(536362774050242601)
            e = discord.Embed(title=ctx.message.author.id, description=ct, color=0x42bcf4)
            await c.send(embed=e)
            dlu[str(ctx.message.author.id)]["level"] = dlu[str(ctx.message.author.id)]["level"] - ct
            dlu[str(ctx.message.author.id)]["exp"] = 0
            with open("level/level.json", 'w') as fs:
                json.dump(dlu,fs)
            with open("level/level.json","rb")as mm:
                db.files_upload(mm.read(), "/level/level.json" ,mode=dropbox.files.WriteMode('overwrite', None))
            await ctx.send("送信済み")
    elif name=="りんご":
        if str(bot.get_guild(536025319963099165).get_member(479964847912648705).status)=="offline":
            await ctx.send("エラー:相手がオフライン")
        else:
            c = bot.get_channel(536364233034694666)
            e = discord.Embed(title=ctx.message.author.id, description=ct, color=0x42bcf4)
            await c.send(embed=e)
            dlu[str(ctx.message.author.id)]["level"] = dlu[str(ctx.message.author.id)]["level"] - ct
            dlu[str(ctx.message.author.id)]["exp"] = 0
            with open("level/level.json", 'w') as fs:
                json.dump(dlu,fs)
            with open("level/level.json","rb")as mm:
                db.files_upload(mm.read(), "/level/level.json" ,mode=dropbox.files.WriteMode('overwrite', None))
            await ctx.send("送信済み")
    elif name=="たく":
        if str(bot.get_guild(536025319963099165).get_member(476012428170362880).status)=="offline":
            await ctx.send("エラー:相手がオフライン")
        else:
            c = bot.get_channel(536171566011252746)
            e = discord.Embed(title=ctx.message.author.id, description=ct, color=0x42bcf4)
            await c.send(embed=e)
            dlu[str(ctx.message.author.id)]["level"] = dlu[str(ctx.message.author.id)]["level"] - ct
            dlu[str(ctx.message.author.id)]["exp"] = 0
            with open("level/level.json", 'w') as fs:
                json.dump(dlu,fs)
            with open("level/level.json","rb")as mm:
                db.files_upload(mm.read(), "/level/level.json" ,mode=dropbox.files.WriteMode('overwrite', None))
            await ctx.send("送信済み")
