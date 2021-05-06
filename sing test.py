import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from discord.utils import get
from discord import FFmpegPCMAudio
import asyncio
import time

bot = commands.Bot(command_prefix='')
token = "ODM4ODExODg0MzQxNDI4Mjg0.YJAicQ.7gkZjtTcP12O6slFD3TUND7cBJM"

@bot.event
async def on_ready():
    print('다음으로 로그인 합니다: ')
    print(bot.user.name)
    print('connection was succesful')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command()  
async def 들어와(ctx):
    try:
        global vc
        vc = await ctx.message.author.voice.channel.connect()
        await ctx.send("ㄷㄷㄷㅈ")
    except:
        try:
            await vc.move_to(ctx.message.author.voice.channel)
        except:
            await ctx.send("너먼저 들어가 멍청아 :middle_finger:  ")

@bot.command()
async def 나가(ctx):
    try:
        await vc.disconnect()
        await ctx.send("나 간다 ㅂㅂ")
    except:
        await ctx.send("이미 나감 ㅅㄱ")

@bot.command()
async def 트러(ctx, *, url):
    YDL_OPTIONS = {'format': 'bestaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}

    if not vc.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        await ctx.send(embed = discord.Embed(title= "귀찮다", description = "" + url + " 이거나 들어", color = 0x00ff00))
    else:
        await ctx.send("이미 듣고 있는게 그거야 멍청아")

@bot.command()
async def 틀어(ctx, *, msg):
    if not vc.is_playing():
        
        await ctx.send("좀만 기다려 시벌 ㅈㄴ 바쁨 지금")
        options = webdriver.ChromeOptions()
        options.add_argument("headless")
         
        global entireText
        YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}
        FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            
        chromedriver_dir = "F:\동영상\Documents\chromedriver.exe"
        driver = webdriver.Chrome(chromedriver_dir, options = options)
        driver.get("https://www.youtube.com/results?search_query="+msg+"+lyrics")
        source = driver.page_source
        bs = bs4.BeautifulSoup(source, 'lxml')
        entire = bs.find_all('a', {'id': 'video-title'})
        entireNum = entire[0]
        entireText = entireNum.text.strip()
        musicurl = entireNum.get('href')
        url = 'https://www.youtube.com'+musicurl 

        driver.quit()

        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        await ctx.send(embed = discord.Embed(title= "귀찮다", description = "" + entireText + "  이거나 들어", color = 0x00ff00))
        vc.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
    else:
        await ctx.send("이미 트는중 건들ㄴㄴ")

@bot.command()
async def 멈춰(ctx):
    if vc.is_playing():
        vc.pause()
        await ctx.send(embed = discord.Embed(title= "멈춰!!", description = entireText + "", color = 0x00ff00))
    else:
        await ctx.send("멈출게 없어!!!")

@bot.command()
async def 다시틀어(ctx):
    try:
        vc.resume()
    except:
         await ctx.send("다시 틀만한게 없는데??")
    else:
         await ctx.send(embed = discord.Embed(title= "멈추지마", description = entireText  + "", color = 0x00ff00))

@bot.command()
async def 그만(ctx):
    if vc.is_playing():
        vc.stop()
        await ctx.send(embed = discord.Embed(title= "그만", description = entireText  + "...ㅇㅋ", color = 0x00ff00))
    else:
        await ctx.send("노래 안틀꺼 ㅅㄱ")

bot.run(token)     