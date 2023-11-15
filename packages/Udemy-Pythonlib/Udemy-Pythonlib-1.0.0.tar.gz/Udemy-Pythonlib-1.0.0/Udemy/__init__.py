import json
import colorama
import requests


class Udemy:

    def __init__(self, cookiesDeSecao: str):
        """
        :param cookiesDeSeão necessario ao instanciar a class


        """

        self.__headers = {
            "accept": "*/*",
            "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "no-cache",
            "Content-Type": "text/plain",
            "pragma": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "cross-site",
            "Cookie": cookiesDeSecao,
            "Referer": "https://www.udemy.com/",
        }

    def __exibir_saida(self, mensagem, tipo, ao_lado=False):
        reset = colorama.Style.RESET_ALL
        cores = {
            "vermelho": colorama.Fore.RED,
            "magneta": colorama.Fore.MAGENTA,
            "sucess": colorama.Fore.GREEN,
            "amarelo": colorama.Fore.YELLOW,
            "logo": colorama.Fore.LIGHTMAGENTA_EX,
            "azul": colorama.Fore.BLUE
        }

        cor = cores.get(tipo, "")
        mensagem_formatada = f"{cor}{colorama.Style.BRIGHT}{mensagem}{reset}"

        if ao_lado:
            print(mensagem_formatada, end="")
        else:
            print(mensagem_formatada)

    def obter_files(self, Id_curso, Id_lecture, Id_asset, exibir=False):
        url = f"https://www.udemy.com/api-2.0/users/me/subscribed-courses/{Id_curso}/lectures/{Id_lecture}/supplementary-assets/{Id_asset}/?fields[asset]=download_urls"
        resposta = requests.get(url, headers=self.__headers)
        if resposta.status_code == 200 and exibir == True:
            resposta = json.loads(resposta.text)
            self.__exibir_saida(resposta, '')
        elif resposta.status_code == 200 and exibir == False:
            resposta = json.loads(resposta.text)
            return resposta
        else:
            results = resposta.text

            self.__exibir_saida("Erro: ", "amarelo", ao_lado=True)
            self.__exibir_saida(f" {resposta.status_code} --> ", "vermelho", ao_lado=True)
            self.__exibir_saida(f" {results} ", "", ao_lado=True)

    def obter_links_de_midias(self, ID_Curso, ID_lecture, exibir=False, filtro=None):

        get = f"https://www.udemy.com/api-2.0//users/me/subscribed-courses/{ID_Curso}/lectures/{ID_lecture}/?fields[lecture]=asset,description,download_url,is_free,last_watched_second&fields[asset]=asset_type,length,media_license_token,course_is_drmed,media_sources,captions,thumbnail_sprite,slides,slide_urls,download_urls,external_url&q=0.3108014137011559/?fields[asset]=download_urls"

        # Faz a solicitação GET com os cabeçalhos
        response = requests.get(get, headers=self.__headers)

        # Exibe o código de status
        if response.status_code == 200 and exibir == True and filtro == 'files':
            # Exibe o conteúdo
            a = json.loads(response.text)
            # a = self.__json_pretty_print(content)
            ######'description'
            description = a.get('description').replace("<p>", "").replace("</p>", "")  # descrição do video

            ######asset
            asset = a.get('asset')  # dicionario asset
            asset_type = asset.get('asset_type')  # tipo de midia

            ####legendas
            captions = asset.get('captions')  # legendas list
            captions_dict = captions[0]  # dicionario de legendas
            titulo_legenda = captions_dict.get('title')  # titulo da legenda
            url_legenda = captions_dict.get('url')  # url da legenda

            # midias
            media_sources = asset.get('media_sources')  # midias video etc.. list
            media_sources_dict = media_sources[0]  # dicionario midias
            type_midia = media_sources_dict.get('type')  # formato url  do video
            src = media_sources_dict.get('src')  # link

            ######thumbnail_sprite

            thumbnail_sprite = asset.get('thumbnail_sprite')  # thumbnail_sprite
            vtt_url = thumbnail_sprite.get('vtt_url')
            img_url = thumbnail_sprite.get('img_url')

            #########printar##############
            self.__exibir_saida(f"Midia : ", "amarelo", ao_lado=True)
            self.__exibir_saida(asset_type, "sucess")
            self.__exibir_saida(f"Formato de mídia : ", "amarelo", ao_lado=True)
            self.__exibir_saida(type_midia, "sucess")

            self.__exibir_saida(f"Url do video : ", "amarelo", ao_lado=True)
            self.__exibir_saida(src, "sucess")

            self.__exibir_saida(f"Legenda : ", "amarelo", ao_lado=True)
            self.__exibir_saida(titulo_legenda, 'sucess')
            self.__exibir_saida(f"Url da legenda : ", "amarelo", ao_lado=True)
            self.__exibir_saida(f'{url_legenda}', "sucess")

            self.__exibir_saida(f"Descrição : ", "amarelo", ao_lado=True)
            self.__exibir_saida(description, "sucess")
            if asset_type == 'Article':
                self.__exibir_saida("Este é um arquivo....", 'vermelho')

            # self.__exibir_saida(content,'')
        elif response.status_code == 200 and exibir == False:
            content = json.loads(response.text)
            return content
        else:
            results = response.text

            self.__exibir_saida("Erro: ", "amarelo", ao_lado=True)
            self.__exibir_saida(f" {response.status_code} --> ", "vermelho", ao_lado=True)
            self.__exibir_saida(f" {results} ", "", ao_lado=True)

    def __filtrar(self, FILTRO, results):
        results = results.get('results')

        for dictionary in results:
            cond = dictionary.get('_class')
            asset = dictionary.get('asset')
            if FILTRO == "files":
                _class = dictionary.get('_class')
                if _class == 'lecture':
                    lecture_id = dictionary.get('id')
                    supplementary_assets = dictionary.get('supplementary_assets')
                    for asset in supplementary_assets:
                        titulo = asset.get('title')
                        asset_id = asset.get('id')
                        self.__exibir_saida('Titulo : ', '', ao_lado=True)
                        self.__exibir_saida(titulo, 'sucess', ao_lado=True)
                        self.__exibir_saida(' ID de lecture : ', '', ao_lado=True)
                        self.__exibir_saida(f'{lecture_id} ', 'sucess', ao_lado=True)
                        self.__exibir_saida(' ID de asset : ', '', ao_lado=True)
                        self.__exibir_saida(f' {asset_id}', 'sucess')
            if FILTRO == "Capitulo":
                chapter = dictionary.get('object_index')
                if dictionary.get('_class') == 'chapter':
                    id_ = dictionary.get('id')
                    title = dictionary.get('title')
                    self.__exibir_saida(f'Capitulo {chapter}', 'amarelo', ao_lado=True)

                    self.__exibir_saida(f' - ', '', ao_lado=True)
                    self.__exibir_saida(f'{title} ', 'sucess')


            elif FILTRO == "title" and cond == 'lecture' and asset:

                id_ = dictionary.get('id')
                chapter = dictionary.get('object_index')
                title = asset.get('title', )
                if title != '':
                    self.__exibir_saida(f' Video Titulo : ', 'vermelho', ao_lado=True)
                    self.__exibir_saida(f'{chapter}.{title}', 'sucess', ao_lado=True)
                    self.__exibir_saida(f' ID -> ', 'vermelho', ao_lado=True)
                    self.__exibir_saida(id_, '')
            elif FILTRO == "id" and cond != 'chapter':
                id_ = dictionary.get('id')
                self.__exibir_saida('ID :', '', ao_lado=True)
                self.__exibir_saida(id_, 'vermelho')
            else:
                pass

    def obter_detalhes_curso(self, id_do_curso, exibir=False, Filter_capitulos=False, Filter_video_titles=False,
                             Filter_id=False, Filter_id_files=False):

        """

        :param id_do_curso: o id do curso que po ser obtdio em ObterId
        :return: detalhes do curso passado como parametro
        """

        response = requests.get(
            f"https://www.udemy.com/api-2.0/courses/{id_do_curso}/subscriber-curriculum-items/?caching_intent=True&fields%5Basset%5D=title%2Cfilename%2Casset_type%2Cstatus%2Ctime_estimation%2Cis_external&fields%5Bchapter%5D=title%2Cobject_index%2Cis_published%2Csort_order&fields%5Blecture%5D=title%2Cobject_index%2Cis_published%2Csort_order%2Ccreated%2Casset%2Csupplementary_assets%2Cis_free&fields%5Bpractice%5D=title%2Cobject_index%2Cis_published%2Csort_order&fields%5Bquiz%5D=title%2Cobject_index%2Cis_published%2Csort_order%2Ctype&pages&page_size=400&fields[lecture]=asset,description,download_url,is_free,last_watched_second&fields[asset]=asset_type,length,media_license_token,course_is_drmed,external_url&q=0.3108014137011559",
            headers=self.__headers)

        if response.status_code == 200:
            if Filter_capitulos == True:
                resposta = json.loads(response.text)
                self.__filtrar('Capitulo', resposta)
            if Filter_video_titles == True:
                resposta = json.loads(response.text)
                self.__filtrar('title', resposta)
            if Filter_id == True:
                resposta = json.loads(response.text)
                self.__filtrar('id', resposta)
            if Filter_id_files == True:
                resposta = json.loads(response.text)
                self.__filtrar('files', resposta)
            if exibir == True:
                resposta = json.loads(response.text)
                self.__exibir_saida(resposta, "")


        elif response.status_code == 200 and exibir == False:
            resposta = json.loads(response.text)
            return resposta


        else:
            r = json.loads(response.text)
            results = r.get("detail")
            self.__exibir_saida("Erro: ", "amarelo", ao_lado=True)
            self.__exibir_saida(f" {response.status_code} --> ", "vermelho", ao_lado=True)
            self.__exibir_saida(f" {results} ", "", ao_lado=True)

    def obter_meu_id(self, exibir=False):

        response = requests.get(f"https://www.udemy.com/api-2.0/contexts/me/?header=true", headers=self.__headers)
        if response.status_code == 200 and exibir == True:
            r = json.loads(response.text)
            login_ = r.get('header')
            login_is = login_.get('isLoggedIn')

            if not login_is:
                self.__exibir_saida(
                    "você não estar logado,ou seja para conseguir obter o seu id de usuario necessita estar logado...",
                    "vermelho")
                self.__exibir_saida(f'Pagina login: ', 'amarelo', ao_lado=True)
                self.__exibir_saida(
                    'https://www.udemy.com/join/login-popup/?locale=pt_BR&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F',
                    'azul')

            else:
                id_ = login_.get('user')
                id__ = id_.get('id')
                self.__exibir_saida(id__, "")
                return id__
        elif response.status_code == 200 and exibir == False:
            r = json.loads(response.text)
            login_ = r.get('header')
            login_is = login_.get('isLoggedIn')

            if not login_is:
                self.__exibir_saida(
                    "você não estar logado,ou seja para conseguir obter o seu id de usuario necessita estar logado...",
                    "vermelho")
                self.__exibir_saida(f'Pagina login: ', 'amarelo', ao_lado=True)
                self.__exibir_saida(
                    'https://www.udemy.com/join/login-popup/?locale=pt_BR&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fmobile%2Fipad%2F',
                    'azul')

            else:
                id_ = login_.get('user')
                id__ = id_.get('id')

                return id__
        else:
            r = json.loads(response.text)
            results = r.get("detail")
            self.__exibir_saida("Erro: ", "amarelo", ao_lado=True)
            self.__exibir_saida(f" {response.status_code} --> ", "vermelho", ao_lado=True)
            self.__exibir_saida(f" {results} ", "")

    def meus_cursos_que_estou_inscrito(self, exibir=False):
        response = requests.get(
            f"https://www.udemy.com/api-2.0/users/me/subscribed-courses/?page_size=100&ordering=-last_accessed"
            f"&fields[course]=image_240x135,title,completion_ratio&is_archived=false",
            headers=self.__headers)
        if response.status_code == 200 and exibir == True:
            r = json.loads(response.text)
            results = r.get("results")
            for item in results:
                id_ = item['id']
                title = item['title']
                image_240x135 = item['image_240x135']
                completion_ratio = item['completion_ratio']
                ##TITLE###33
                self.__exibir_saida(f"Curso", "amarelo", ao_lado=True)
                self.__exibir_saida(":", "", ao_lado=True)
                self.__exibir_saida(f"{title}", "magneta")
                ## ID ####
                self.__exibir_saida(f"id", "amarelo", ao_lado=True)
                self.__exibir_saida(":", "", ao_lado=True)
                self.__exibir_saida(f"{id_}", "magneta")

                self.__exibir_saida(f"thumbnail", "amarelo", ao_lado=True)
                self.__exibir_saida(":", "", ao_lado=True)
                self.__exibir_saida(f"{image_240x135}", "magneta")

                self.__exibir_saida(f"modulos completos", "amarelo", ao_lado=True)
                self.__exibir_saida(":", "", ao_lado=True)
                self.__exibir_saida(f"{completion_ratio}\n", "magneta")


        elif response.status_code == 200 and not exibir:
            r = json.loads(response.text)
            results = r.get("results")
            return results
        else:
            r = json.loads(response.text)
            results = r.get("detail")
            self.__exibir_saida("Erro: ", "amarelo", ao_lado=True)
            self.__exibir_saida(f" {response.status_code} --> ", "vermelho", ao_lado=True)
            self.__exibir_saida(f" {results} ", "", ao_lado=True)

    @staticmethod
    def __json_pretty_print(jsones):
        return str(jsones).replace(",", ",\n").replace("{\"", "{\"\n")


