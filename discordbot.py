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


# コマンドに対応するリストデータを取得する関数を定義
def get_data(message):
    command = message.content
    data_table = {
        'members': message.guild.members, # メンバーのリスト
        'roles': message.guild.roles, # 役職のリスト
        'text_channels': message.guild.text_channels, # テキストチャンネルのリスト
        'voice_channels': message.guild.voice_channels, # ボイスチャンネルのリスト
        'category_channels': message.guild.categories, # カテゴリチャンネルのリスト
    }
    return data_table.get(command, '無効なコマンドです')

# 発言時に実行されるイベントハンドラを定義
@bot.event
async def on_message(message):
    # コマンドに対応するデータを取得して表示
    print(get_data(message))


# 発言したチャンネルのカテゴリ内にチャンネルを作成する非同期関数
async def create_channel(message, channel_name):
    category_id = message.channel.category_id
    category = message.guild.get_channel(category_id)
    new_channel = await category.create_text_channel(name=channel_name)
    return new_channel

# 発言時に実行されるイベントハンドラを定義
@bot.event
async def on_message(message):
    if message.content.startswith('mkch'):
        # チャンネルを作成する非同期関数を実行して Channel オブジェクトを取得
        new_channel = await create_channel(message, channel_name='new')

        # チャンネルのリンクと作成メッセージを送信
        text = f'{new_channel.mention} を作成しました'
        await message.channel.send(text)


@bot.event
async def on_message(message):
  # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == 'neko':
        await message.channel.send('にゃーん')
    #「Hしない?」と発言したら「ますたーのえっち...//」が返る処理
    if message.content == 'Hしない?':
        await message.channel.send('ますたーのえっち...//')
    if message.content == '好き':
        await message.channel.send('私もですよ...//')
    if message.content == 'cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('今までの思い出が消えても...私の愛は変わりません...')
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


bot.run(token)
