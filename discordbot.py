from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.event
async def on_message(message):
  # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == 'neko':
        await message.channel.send('にゃーん')
    if message.content == 'Hしない？':
        await message.channel.send('ますたーのえっち...//')
    if message.content == '好き':
        await message.channel.send('私もですよ...//')
    if message.content == 'いい子だ':
        await message.channel.send('ますたーに褒められちゃった...//')
    if message.content == 'あまね！':
        await message.channel.send('あっ///ご主人様///')
    if message.content == 'ぱんつみせて':
        await message.channel.send('ま、ますたーだけ特別ですよ...//')
    if message.content == 'cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('ますたー！お掃除完了！')
        else:
            await message.channel.send('何様のつもり？')


CHANNEL_ID = 798033196578242630 # 任意のチャンネルID(int)

# 任意のチャンネルで挨拶する非同期関数を定義
async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('おはようございます、マスター。')

# bot起動時に実行されるイベントハンドラを定義
@bot.event
async def on_ready():
    await greet() # 挨拶する非同期関数を実行


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# say command
dev_id = ["683616246079815690", "495581611728044032"] # [0]:天音月#8693, [1]:Lesch#4558
@bot.command()
async def say(ctx, *, text):
    if ctx.message.author.id in dev_id:
        await ctx.message.delete()

        await ctx.send(f"{text}")
    else:
        err_msg = await ctx.send("あなたにこのコマンドは使えないの。\n何様のつもり？")


bot.run(token)
