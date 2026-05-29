from plataforma import Plataforma
from video import Video
from podcast import Podcast
from texto_narrado import TextoNarrado

if __name__ == "__main__":
    minha_plataforma = Plataforma("UFAM Play")

    v1 = Video("Aula de POO sobre Polimorfismo", 45, "1080p")
    p1 = Podcast("Tech Talk UFAM - Episódio 3", 60, "Prof. Alternei")
    t1 = TextoNarrado("Artigo sobre Engenharia de Software", 15, "Português-BR")

    minha_plataforma.adicionar_midia(v1)
    minha_plataforma.adicionar_midia(p1)
    minha_plataforma.adicionar_midia(t1)

    minha_plataforma.listar_midias()
    minha_plataforma.reproduzir_todas()
