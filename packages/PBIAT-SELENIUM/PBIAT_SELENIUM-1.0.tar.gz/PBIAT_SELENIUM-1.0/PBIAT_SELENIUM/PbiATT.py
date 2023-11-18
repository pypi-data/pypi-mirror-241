from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Condicao
from selenium.common.exceptions import NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException,ElementClickInterceptedException,StaleElementReferenceException
from selenium.webdriver import ActionChains
from pathlib import Path
import time
import os

class AutomacaoLogin:
    @staticmethod
    def VerificarDiretorio():
        caminho = Path(os.path.expanduser('~')) / 'Documents'
        if Path(caminho / 'AutomacaoS').exists():

            if Path(caminho / 'AutomacaoS' / 'Imprimir').exists():
                return Path(caminho / 'AutomacaoS' / 'Imprimir')
            else:
                Path(caminho / 'AutomacaoS' / 'Imprimir').mkdir()
                return Path(caminho / 'AutomacaoS' / 'Imprimir')
        else:
            Path(caminho / 'AutomacaoS').mkdir()
            Path(caminho / 'AutomacaoS' / 'Imprimir').mkdir()
            return Path(caminho / 'AutomacaoS' / 'Imprimir')


    def __init__(self,login,senha,Argumentos=None,ArgumentosEx=None):
        self.login = login
        self.senha = senha
        self._Options(Argumentos,ArgumentosEx)
        print('Criando Navegador')
        self.servico = Service(ChromeDriverManager().install())
        self.navegador = webdriver.Chrome(options=self.options,service=self.servico)
        self.wait = WebDriverWait(
            driver=self.navegador,
            timeout=25,
            poll_frequency= 1 ,
            ignored_exceptions = [NoSuchElementException,ElementNotVisibleException,ElementNotSelectableException,ElementClickInterceptedException,StaleElementReferenceException]
        )
        print('Iniciando Automacao')
        self._iniciar()

    def _Options(self,Argumentos,ArgumentosEX):
        self.argumentos = Argumentos
        self.argumentosEx = ArgumentosEX
        self.options = Options()


        if self.argumentos is not None:
            for argumento in self.argumentos:
                self.options.add_argument(argumento)

        if self.argumentosEx is not None:
            for argumento in self.argumentosEx:
                self.options.add_experimental_option(*argumento)
        else:
            self.options.add_experimental_option("excludeSwitches", ['enable-automation'])

    def _iniciar(self):
        self.tempo_inicial = time.time()
        self.navegador.get('https://login.microsoftonline.com/')
        time.sleep(5)
        print('Entrando no Site')
        self.wait.until(Condicao.element_to_be_clickable((By.XPATH, '//*[@id="i0116"]'))).send_keys(self.login)
        print('Escrevendo E-Mail')
        self.wait.until(Condicao.element_to_be_clickable((By.XPATH,'//*[@id="idSIButton9"]')))
        self.navegador.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(self.senha)
        print('Digitando Senha')
        self.wait.until(Condicao.element_to_be_clickable((By.XPATH,'//*[@id="idSIButton9"]'))).click()
        self.wait.until(Condicao.element_to_be_clickable((By.XPATH,'//*[@id="idSIButton9"]'))).click()
        print('Login Realizado Com Sucesso')


class AtualizarWorkspace(AutomacaoLogin):
    def __init__(self,login,senha,workspace,Argumentos=None,ArgumentosEx=None):
        super().__init__(login,senha,Argumentos,ArgumentosEx)
        self.navegador.get(workspace)
        print('Filtrando Dados')
        self.wait.until(Condicao.element_to_be_clickable((By.XPATH,
                                                          "//button[@class='tri-filter-menu-trigger-button"
                                                          " tri-flex tri-justify-center tri-items-center tri-text-sm tri-border "
                                                        "tri-rounded tri-border-solid tri-bg-gray-white tri-border-gray-82 tri-h-32px"
                                                          " tri-text-gray-180 tri-box-border tri-filter-menu-state']"))).click()
        print('Conjunto de Dados')
        self.wait.until(Condicao.element_to_be_clickable((By.XPATH, "//div[@id='1'][@class='tri-flex tri-items-center "
                                                                    "tri-multiselect-list-item-label tri-w-full tri-h-32px tri-px-2']"))).click()

        actions = ActionChains(self.navegador)
        lista =  self.navegador.find_elements(By.XPATH, "//mat-icon[@data-mat-icon-name='pbi-glyph-refresh']")
        self.wait.until(Condicao.element_to_be_clickable(
            (By.XPATH, '//div[@class="mat-sort-header-container mat-focus-indicator ng-tns-c371-5"]')))
        try:
            for valor in range(len(lista)):
                print(f'Atualizando Relatorio {valor+1}')
                elemento = self.navegador.find_elements(By.XPATH, '//mat-icon[@fonticon="pbi-glyph-refresh"]')[valor]
                actions.move_to_element(elemento).perform()
                self.wait.until(Condicao.visibility_of(elemento)).click()
                actions.move_to_element(elemento).perform()
            print('Atualizado com sucesso')
        except:
            print('Aguarde atualização Agendada')

        print(f'Tempo Gasto total: {round((time.time() - self.tempo_inicial) / 60, 2)} minutos')

class BaixarRelatorio(AtualizarWorkspace):
    def __init__(self, login, senha, workspace,links,Argumentos=None,ArgumentosEx=None):
        super().__init__(login, senha,workspace,Argumentos,ArgumentosEx)
        time.sleep(15)
        for link in links:
            self.navegador.execute_script("window.open('', '_blank');")
            self.navegador.switch_to.window(self.navegador.window_handles[-1])
            self.navegador.get(link)
            print('Abrindo Relatorio')
            self.wait.until(Condicao.element_to_be_clickable((By.XPATH, '//button[(@id = "exportMenuBtn")]'))).click()
            self.wait.until(Condicao.element_to_be_clickable((By.XPATH, '//button[@data-testid="export-to-pdf-btn"]'))).click()
            self.wait.until(Condicao.element_to_be_clickable((By.XPATH, '//button[@id="okButton"]'))).click()
            print('Baixando Relatorio')
            time.sleep(50)
            print(f'Tempo Gasto total: {round((time.time() - self.tempo_inicial) / 60, 2)} minutos')

    def _Options(self,Argumentos,ArgumentosEx):
        diretorio_atual = self.VerificarDiretorio()
        self.options = Options()
        if Argumentos is not None:
            for argumento in lista:
                self.options.add_argument(argumento)

        self.options.add_experimental_option("prefs",
                    {"download.default_directory": f"{diretorio_atual}", "download.prompt_for_download": False,
                     "download.directory_upgrade": True, "safebrowsing.enabled": True})
        self.options.add_experimental_option("excludeSwitches", ['enable-automation'])


class VisualizarRelatorios(AtualizarWorkspace):
    def __init__(self, login, senha, workspace,intervalo,links,Argumentos=['--lang=pt-BR', '--disable-notifications','--kiosk'],ArgumentosEX=None):
        super().__init__(login, senha,workspace,Argumentos,ArgumentosEX)
        while True:
            for link in links:
                print('Abrindo Indicadores')
                self.navegador.execute_script("window.open('', '_blank');")
                self.navegador.switch_to.window(self.navegador.window_handles[-1])
                self.navegador.get(link + '&chromeless=True')
                self.wait.until(Condicao.element_to_be_clickable((By.XPATH, '//i[@aria-label="Avançar"]')))
                time.sleep(intervalo)
                while True:
                    try:
                        self.navegador.find_element(By.XPATH, '//i[@aria-label="Avançar"]').click()
                        elemento = self.navegador.find_element(By.XPATH, '//i[@aria-label="Avançar"]').get_attribute("class")
                        time.sleep(intervalo)
                        if 'inactive' in elemento:
                            break
                    except:
                        print('Proximo')
                        break
            for c in range(len(links)):
                self.navegador.execute_script("window.close()")
                self.navegador.switch_to.window(self.navegador.window_handles[-1])
