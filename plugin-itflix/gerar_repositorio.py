"""
gerar_repositorio.py
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Execute esse script TODA VEZ que lançar versão nova do addon.
Ele atualiza o addons.xml e gera o md5 automaticamente.

Como usar:
1. Mude a versão na variável VERSAO abaixo
2. Execute: python gerar_repositorio.py
3. Suba os arquivos gerados no GitHub
"""

import hashlib

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# MUDE A VERSÃO AQUI A CADA ATUALIZAÇÃO
VERSAO = "1.0.1+matrix.1"
NOVIDADES = "- Descrição do que mudou nessa versão"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

addons_xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<addons>
    <addon id="plugin.video.itflix.matrix" name="ITFLIX" version="{VERSAO}" provider-name="Itamar">
        <requires>
            <import addon="xbmc.python" version="3.0.0"/>
            <import addon="script.module.requests"/>
            <import addon="script.module.simplejson"/>
            <import addon="script.module.kodi-six"/>
        </requires>
        <extension point="xbmc.python.pluginsource" library="default.py">
            <provides>video</provides>
        </extension>
        <extension point="xbmc.addon.metadata">
            <summary lang="en">ITFLIX Addon</summary>
            <summary lang="pt">ITFLIX Addon</summary>
            <description lang="en">Movies, Series, Live TV and more.</description>
            <description lang="pt">Filmes, Series, Canais ao vivo e muito mais.</description>
            <platform>all</platform>
            <assets>
                <icon>icon.png</icon>
                <fanart>fanart.png</fanart>
            </assets>
            <news>
v{VERSAO}
{NOVIDADES}
            </news>
        </extension>
    </addon>
    <addon id="repository.itflix" name="Repositorio ITFLIX" version="1.0.0" provider-name="Itamar">
        <requires>
            <import addon="xbmc.python" version="3.0.0"/>
        </requires>
        <extension point="xbmc.addon.repository" name="Repositorio ITFLIX">
            <info compressed="false">https://raw.githubusercontent.com/itflixhd/Itflix/main/plugin-itflix/addons.xml</info>
            <checksum>https://raw.githubusercontent.com/itflixhd/Itflix/main/plugin-itflix/addons.xml.md5</checksum>
            <datadir zip="true">https://github.com/itflixhd/Itflix/raw/main/plugin-itflix/plugin.video.itflix.matrix/</datadir>
        </extension>
        <extension point="xbmc.addon.metadata">
            <summary lang="pt">Repositorio oficial do ITFLIX</summary>
            <description lang="pt">Instale e atualize o ITFLIX automaticamente.</description>
            <platform>all</platform>
        </extension>
    </addon>
</addons>'''

# Gera o MD5
md5 = hashlib.md5(addons_xml.encode('utf-8')).hexdigest()

# Salva os arquivos
with open('addons.xml', 'w', encoding='utf-8') as f:
    f.write(addons_xml)

with open('addons.xml.md5', 'w') as f:
    f.write(md5)

print("=" * 40)
print(f"✅ addons.xml gerado - versão {VERSAO}")
print(f"✅ addons.xml.md5 gerado - {md5}")
print("=" * 40)
print("Agora suba os 2 arquivos no GitHub!")