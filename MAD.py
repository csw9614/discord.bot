
import discord 
import random 
import youtube_dl
from youtube_dl import YoutubeDL


intents = discord.Intents.default()
app = discord.Client(intents=intents)

token = "ODM4ODExODg0MzQxNDI4Mjg0.YJAicQ.7gkZjtTcP12O6slFD3TUND7cBJM"

@app.event 
async def on_ready():
    print("다음으로 로그인합니다 : ")
    print(app.user.name)
    print(app.user.id)
    print("==========")
    game = discord.Game("앙 제라스 버프띠")
    await app.change_presence(status=discord.Status.online, activity=game)



@app.event
async def on_message(message):
    if message.author.bot:
        return None
    if message.content == "안녕":
        await message.channel.send("안녕하세요.")
    if message.content.startswith("최성우전적"):
        embed=discord.Embed(title="제라스 엄마", description="제라스 엄마의 전적", color=0x00ff56)
        embed.set_author(name="OP.GG", url="https://www.op.gg/summoner/userName=%EC%A0%9C%EB%9D%BC%EC%8A%A4+%EC%97%84%EB%A7%88", icon_url="https://opgg-static.akamaized.net/images/lol/champion/Xerath.png?image=c_scale,q_auto,w_45&v=1619585878")
        await message.channel.send(embed=embed)
    if message.content == "롤":
        await message.channel.send("잘하시네요")
    if message.content == "내전ㄱ":
        await message.channel.send("@everyone")
    if message.content == "최성우":
        await message.channel.send("ㄹㅇ 너무 잘생김 ㄷㄷ")
    if message.content == "제라스":
        await message.channel.send("갓챔")
    if message.content == "띵언":
        await message.channel.send("빈 마음, 그것을 무심이라고 한다. 빈 마음이 곧 우리들의 본 마음이다. 무엇인가 채워져 있으면 본 마음이 아니다. 텅 비우고 있어야 거기 울림이 있다. 울림이 있어야 삶이 신선 하고 활기 있는 것이다.")
    if message.content == "장민혁":
        await message.channel.send('''병
        신''')
    if message.content == "ㅗ":
        await message.channel.send(":middle_finger: ")
    if message.content == "ㅂㅂ":
        await message.channel.send("잘가 애들아 제라스 하는 꿈꾸길 바래 <3")
    if message.content == "김창연":
        await message.channel.send("세마고 1탑 파이선 장인 해결사 등장")
    if message.content == "선물":
        await message.channel.send(random.choice(['응니똥','ㅗ','응 니얼굴',':heartpulse: ',':hamburger: ',':middle_finger: ']))  
    if message.content == "벨코즈":
        await message.channel.send("제라스보다 안좋은 똥챔입니다 쓰지 마세요")
    if message.content.startswith("ㅈㄱ"):
        embed=discord.Embed(title="ㅈㄱㅊㅇ", color=0x00ff56)
        embed.set_author(name="정글차이", url="https://youtu.be/S4qZVzCaenQ" )
        await message.channel.send(embed=embed)   
    if message.content.startswith("문학"):
        embed=discord.Embed(title="문학", color=0x00ff56)
        embed.set_author(name="수업", url="https://meet.google.com/lookup/apylw2nacs?authuser=7&hs=179" )
        await message.channel.send(embed=embed)  
    if message.content == "김경영":
        await message.channel.send("경영베인은 ㄹㅇ 신인가 가슴이 웅장해진다...이것이 nd teddy??")
    if message.content == "-메-":
        await message.channel.send("머가리 봉합수술 대기실")
    if message.content == "블루는":
        await message.channel.send("미드꺼!!!")  
    if message.content == "레드는":
        await message.channel.send("원딜꺼!!!")
    if message.content == "와드는":
        await message.channel.send("서폿꺼!!!")
    if message.content == "정글은":
        await message.channel.send("그건 뭐야..?")
    if message.content == "한예성":
        await message.channel.send("개똥멍청이") 
    if message.content == "송준혁":
        await message.channel.send("학교에서 인정해버린 인간 콴다 이게 전설인가..?") 
    if message.content == "김정현":
        await message.channel.send('''간                                    첩 
         라고 할뻔~~''') 
    if message.content == "강승수":
        await message.channel.send("승수승수강승수") 
    if message.content == "?":
        await message.channel.send("????????????????????????????????????????????????????????????????????????????????????") 
    if message.content == "ㅅㅂ":
        await message.channel.send(" :regional_indicator_s: :regional_indicator_i:   :regional_indicator_b: :regional_indicator_a: :regional_indicator_l:") 
    if message.content == "자랭":
        await message.channel.send("@everyone 자랭 5인 구합니다") 
    if message.content == "박성현":
        await message.channel.send(":shark: ")
    if message.content == "격전":
        await message.channel.send("@everyone (경영,준혁,성우) 격전 2인 구합니다")
    if message.content == "이경윤":
        await message.channel.send("카타리나는 스킬을 사용하면 떨어지는 단검을 대상으로 순보를 계속해서 사용하며 상대를 농락할 수 있는 챔피언입니다. 이동과 공격이 합쳐져 테크니컬한 전투를 펼치는 카타리나는 숙련되면 숙련될수록 강력해집니다. 특히 적 챔피언이 사망하면 스킬 쿨타임이 줄어들어 더욱더 폭발적인 위력을 발휘합니다.")
    if message.content == "격전":
        await message.channel.send("@everyone (경영,준혁,성우) 격전 2인 구합니다") 
    if message.content == "감사":
        await message.channel.send("응 니얼굴")  
    if message.content == "박경민":
        await message.channel.send("풉ㅋ 그거 머임??") 
    if message.content == "이지원":
        await message.channel.send("경민이 여친 (라고 할뻔~)[우리반 최지원 아님]        ")  
    if message.content == "얘들아":
        await message.channel.send("@everyone")
    if message.content == "뭐해":
        await message.channel.send("안물")   
    if message.content == "데헷":
        await message.channel.send(":stuck_out_tongue_closed_eyes: :stuck_out_tongue_closed_eyes: ")
    if message.content == "야":
        await message.channel.send("뭐")    
    if message.content == "서영준":
        embed=discord.Embed(title="나와라 영준몬",color=0x00FFFF)
        embed.set_image( url="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTAzMTNfMTg1%2FMDAxNjE1NjE3ODI4MDg4.sg2vHK1GCTC7Byim-cHGkiBSoIDzuV-jwjU1F2BSOskg.pKdZhkPOAgOgHnSt-gJvKlWJ_yp7-9XZ6i3Ac8_KPlIg.JPEG.pasris2355%2F1.jpg&type=sc960_832" )
        await message.channel.send(embed=embed)  
app.run(token)    
