##This code is created and developed by Atak-O ( Atakan Özden)##
#--------------------------------------
## Project Owner : Atak-O
#--------

import discord
from discord.ext import commands
import random
import string
import os
import requests

def gen_pass(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Tavsiyeler listesini tüm komutlarda kullanabilmek için en üstte tanımlıyoruz
cevre_icin_tavsiyeler = [
    "Tek kullanımlık plastik (pet şişe, pipet, poşet) kullanımını azaltın.",
    "Kullanmadığınız odalardaki ışıkları ve elektronik aletleri kapatarak enerji tasarrufu yapın.",
    "Kağıt, cam, plastik ve metal atıklarınızı ayrıştırarak geri dönüşüm kutularına atın.",
    "Ulaşım için mümkün olduğunca toplu taşıma araçlarını kullanın, yürüyün veya bisiklete binin.",
    "Diş fırçalarken veya bulaşık yıkarken suyu gereksiz yere açık bırakmayın.",
    "Alışverişlerinizde plastik poşet yerine kendi bez çantanızı veya filelerinizi kullanın.",
    "Karbon ayak izinizi düşürmek için yerel üreticileri destekleyin ve mevsiminde gıdalar tüketin.",
    "Evde enerji verimliliği yüksek (A sınıfı ve üzeri) cihazlar ve LED ampuller tercih edin.",
    "Kullanmadığınız kıyafetleri ve eşyaları atmak yerine bağışlayın veya ileri dönüşüm (upcycling) yapın.",
    "E-postaları ve belgeleri gerçekten gerekmedikçe yazdırmayarak kağıt israfını önleyin."
]

@bot.event
async def on_ready():
    # Bot aktifleştiğinde listeyi konsola yazdırır
    tavsiyeler_metni = '\n- '.join(cevre_icin_tavsiyeler)
    print(f'Bot başarıyla giriş yaptı: {bot.user}\n')
    print(f'Çevreyi Korumak İçin Tavsiyeler:\n- {tavsiyeler_metni}')

@bot.command()
async def recycle(ctx):
    embed = discord.Embed(
        title="♻️ Geri Dönüşüm Rehberi",
        description="Hangi atık hangi kutuya atılmalı?",
        color=discord.Color.green()
    )
    
    # Her madde için ayrı alanlar ve hangi kutuya gideceği bilgisi
    embed.add_field(name="📦 Kağıt & Karton", value="**Mavi Kutu**\n(Gazete, koli, defter)", inline=True)
    embed.add_field(name="🍼 Plastik", value="**Sarı Kutu**\n(Pet şişe, deterjan kutusu)", inline=True)
    embed.add_field(name="🍾 Cam", value="**Yeşil Kutu**\n(Şişe, kavanoz)", inline=True)
    
    embed.add_field(name="🥫 Metal", value="**Gri Kutu**\n(İçecek kutusu, konserve)", inline=True)
    embed.add_field(name="🔋 Atık Pil", value="**Pil Kutusu**\n(Marketlerdeki özel kutular)", inline=True)
    embed.add_field(name="🍎 Organik/Evsel", value="**Kahverengi/Siyah Kutu**\n(Yemek artıkları)", inline=True)

    # Görsel linkini gerçek bir görselle değiştirmeyi unutma
    embed.set_image(url="https://example.com") 
    embed.set_footer(text="Doğayı korumak bizim elimizde!")

    await ctx.send(embed=embed)

@bot.command() 
async def environmental_advice(ctx): 
    # Listeden rastgele bir tavsiye seçiyoruz
    rastgele_tavsiye = random.choice(cevre_icin_tavsiyeler)
    
    # Sunucuya daha şık görünmesi için Embed ile gönderiyoruz
    embed = discord.Embed(
        title="🌍 Çevreyi Korumak İçin Bir Tavsiye",
        description=f"**{rastgele_tavsiye}**",
        color=discord.Color.blue()
    )
    embed.set_footer(text="Küçük adımlar büyük farklar yaratır!")
    
    await ctx.send(cevre_icin_tavsiyeler)

# Buraya kendi bot token'ınızı yazın
bot.run("TOKEN")
