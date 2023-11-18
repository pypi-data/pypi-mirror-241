import re
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

from ..Interfaces.interfaces import BaseInterface
from ..utils.utils import init
from .dataClass import DataClass


class VercelInterface(BaseInterface):
    def __init__(self, data: DataClass):
        self.data = data

    def getTokenJenkins(self):
        pass

    def Login(self):
        session = init()
        driver = session.driver()
        driver.get(self.data.link % ("login"))
        driver.implicitly_wait(100)
        time.sleep(7)
        select = driver.find_element(
            "xpath",
            '//*[@id="__next"]/div/div/div[3]/div[1]/div[2]/div/div/span[1]/button',
        )
        select.click()
        WebDriverWait(driver, 100).until(EC.number_of_windows_to_be(2))
        child = driver.window_handles[1]
        driver.switch_to.window(child)
        print("child", child)
        time.sleep(5)

        user = driver.find_element("id", "login_field")
        user.send_keys(self.data.user)
        # user.submit()
        time.sleep(5)
        password = driver.find_element("id", "password")
        password.send_keys(self.data.password)
        password.submit()
        time.sleep(20)
        # checkAuth = self.checkAuth(driver)

        '''print("antes del url driver")
        if driver.current_url == "https://github.com/sessions/verified-device":
            print("entre")
            time.sleep(20)
            getCode = session.get_code_email()
            time.sleep(5)
            otp = driver.find_element("id", "otp")
            otp.send_keys(getCode)
            time.sleep(5)
            otp.submit()
            WebDriverWait(driver, 100).until(EC.number_of_windows_to_be(2))
            time.sleep(100)
            print("fin url")
            main_handle = driver.window_handles[0]
            #print(main_handle)
            driver.switch_to.window(main_handle)
        elif checkAuth(driver):
            print("auth")
            xpath="""/html/body/div[1]/div[6]/main/
                    div[2]/div[1]/div[2]/div[1]/
                    form/div/button[2]"""
            btnAuth = driver.find_element("xpath", 
                                        xpath.replace("\n", "").replace(" ", ""))
            btnAuth.submit()
            #main_handle = driver.window_handles[0]
            #driver.switch_to.window(main_handle)
        print("sali")'''
        main_handle = driver.window_handles[0]
        driver.switch_to.window(main_handle)
        try:
            SuccessLogin = driver.find_element(
                "xpath",
                '//*[@id="__next"]/div[2]/div/nav/div[1]/ol/li[3]/div/div/a/div/p',
            )
            if SuccessLogin:
                print("Login success")
                self.data.login = True
                return driver
        except Exception as err:
            failPass = driver.find_element(
                "xpath", "/html/body/div[1]/div[2]/div/div[1]/div/div/div"
            )
            if failPass:
                print(f"Invalid username or password {err=}")
                return driver

    def validateFramework(self, name):
        newName = name.lower()
        newName = newName.replace(" ", "-")
        return newName

    def checkAuth(driver):
        try:
            xpath = """/html/body/div[1]/div[6]/
                        main/div[1]/h2[1]"""
            auth = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            if auth:
                xpath = """'/html/body/div[1]/div[6]/main/div[2]/
                            div[1]/div[2]/div[1]/form/div/
                            button[2]'"""
                btnAuth = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                btnAuth.submit()
                return True
        except Exception as err:
            print(f"Error in Auth Request -> {err}")
            return False

    def configirationEnv(self, driver, data: dict):
        xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/
                div[2]/div/article[1]/div/div[2]/div[1]/div[4]/div"""
        envConfig = driver.find_element(
            "xpath",
            xpath.replace("\n", "").replace(" ", ""),
        )
        xpaths = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/
                  div/article[1]/div/div[2]/div[1]/div[4]/div/details"""
        envTarget = driver.find_element(
            "xpath",
            xpaths.replace("\n", "").replace(" ", ""),
        )
        driver.implicitly_wait(100)
        action_chains = ActionChains(driver)
        action_chains.drag_and_drop(envConfig, envTarget).perform()
        driver.implicitly_wait(100)
        for keys, values in data.items():
            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/
                    article[1]/div/div[2]/div[1]/div[4]/div/details/form/
                    div/div[1]/div[1]/label/div[2]/div/input"""
            inputEnvName = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            inputEnvName.send_keys(keys)
            driver.implicitly_wait(100)

            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/article[1]/
                    div/
                    div[2]/div[1]/div[4]/div/details/form/div/
                    div[1]/div[2]/label/div[2]/textarea"""
            inputEnvValue = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            inputEnvValue.send_keys(values)
            driver.implicitly_wait(100)

            xpaths = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/article[1]/
                        div/div[2]/div[1]/div[4]/div/details/form/div/
                        div[2]/div/button"""
            addVariEnv = driver.find_element(
                "xpath",
                xpaths.replace("\n", "").replace(" ", ""),
            )
            addVariEnv.click()

    def configirationBuild(self, driver, data: list, isUpdate: bool = False):
        if not isUpdate:
            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/
                      article[1]/div/div[2]/div[1]/div[3]"""
            elementConfig = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )

            xpaths = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/
                        article[1]/div/div[2]/div[1]/div[3]/div/details"""
            target = driver.find_element(
                "xpath",
                xpaths.replace("\n", "").replace(" ", ""),
            )
            driver.implicitly_wait(100)
            time.sleep(2)
            action_chains = ActionChains(driver)
            action_chains.drag_and_drop(elementConfig, target).perform()
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/article[1]/
                   div/div[2]/div[1]/div[3]/div/details/div[1]/
                   div[2]/div[2]/div[2]/label/span/div"""
            OverRideBuild = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            OverRideBuild.click()
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/article[1]/
                      div/div[2]/div[1]/div[3]/div/details/
                      div[1]/div[1]/div[2]/div/input"""
            inputBuildCommand = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            inputBuildCommand.send_keys(data[0])
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/article[1]/
                       div/div[2]/div[1]/div[3]/div/details/div[2]/
                       div[2]/div[2]/div[2]/label/span/div"""
            OverRideDirectory = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            OverRideDirectory.click()
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/article[1]/
                      div/div[2]/div[1]/div[3]/div/details/
                      div[2]/div[1]/div[2]/div/input"""
            inputOutputDirectory = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            inputOutputDirectory.send_keys(data[1])
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/article[1]/
                       div/div[2]/div[1]/div[3]/div/details/div[3]/
                       div[2]/div[2]/div[2]/label/span/div"""
            OverRideInstall = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            OverRideInstall.click()
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/div[2]/div/article[1]/
                       div/div[2]/div[1]/div[3]/div/details/
                       div[3]/div[1]/div[2]/div/input"""
            inputInstall = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            inputInstall.send_keys(data[2])
            driver.implicitly_wait(100)
            time.sleep(2)
        else:
            xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/
                       div[2]/div/div/div/div/div[1]/div[2]/div[2]/label/span"""

            OverRideBuild = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            OverRideBuild.click()

            xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/
                       div[2]/div/div/div/div/div[1]/div[1]/
                       div[2]/span/div/div/input"""
            inputBuildCommand = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            time.sleep(10)
            inputBuildCommand.clear()
            time.sleep(10)
            inputBuildCommand.send_keys(data[0])
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/
                       div[2]/div/div/div/div/div[2]/div[2]/
                       div[2]/label/span/div"""
            OverRideDirectory = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            OverRideDirectory.click()

            xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/
                       div[2]/div/div/div/div/div[2]/div[1]/
                       div[2]/span/div/div/input"""
            inputOutputDirectory = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            time.sleep(10)
            inputOutputDirectory.clear()
            time.sleep(10)
            inputOutputDirectory.send_keys(data[1])
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/
                       div[2]/div/div/div/div/div[3]/div[2]/
                       div[2]/label/span/div"""
            OverRideInstallCmd = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            OverRideInstallCmd.click()

            xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/
                       div[2]/div/div/div/div/div[3]/
                       div[1]/div[2]/span/div/div/input"""
            inputInstallCmd = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            time.sleep(10)
            inputInstallCmd.clear()
            time.sleep(10)
            inputInstallCmd.send_keys(data[2])
            driver.implicitly_wait(100)
            time.sleep(2)

            xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/
                      div[2]/div/div/div/div/div[4]/div[2]/div[2]/label/span/div"""
            OveriRideDevep = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            OveriRideDevep.click()

            xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/
                       div[2]/div/div/div/div/div[4]/div[1]/div[2]/span/div/div/input"""
            inputDevep = driver.find_element(
                "xpath",
                xpath.replace("\n", "").replace(" ", ""),
            )
            time.sleep(10)
            inputDevep.clear()
            time.sleep(10)
            inputDevep.send_keys(data[3])

    def CreateProject(self):
        try:
            driver = self.Login()
            if self.data.login:
                print("entre login")
                time.sleep(7)
                driver.implicitly_wait(100)
                driver.get(self.data.linkNewProject % (self.data.group))
                driver.implicitly_wait(100)
                time.sleep(7)
                content2 = driver.find_element(
                    By.CLASS_NAME, "select-git-repository_repoList__dhfLA"
                )
                LinkPage = content2.find_elements(By.CLASS_NAME, "button_base__BjwbK")
                getLink = ""
                driver.implicitly_wait(100)
                time.sleep(7)
                for i in range(0, len(LinkPage)):
                    xpath = f"""//*[@id="__next"]/div/div/div[3]/div[1]/div/div[3]/
                                div[1]/div/div[2]/div/div/div[2]/div/div[{i+1}]/
                                div/div/div[3]/div/a"""
                    el_hrefs = driver.find_element("xpath", xpath)
                    item = el_hrefs.get_attribute("href")
                    href = re.search(
                        r"project-name=(.+)\&framework",
                        item,
                    )
                    if self.data.nameProject.lower() == href.group(1):
                        getLink = el_hrefs.get_attribute("href")
                        break

                driver.implicitly_wait(100)
                time.sleep(5)
                driver.get(getLink)
                dropdown = Select(driver.find_element(By.NAME, "framework"))
                for option in dropdown.options:
                    if option.get_attribute("value") == self.data.framework.lower():
                        # if option.text == self.data.Framework:
                        NameFramework = self.validateFramework(self.data.framework)
                        driver.implicitly_wait(100)
                        time.sleep(5)
                        dropdown.select_by_value(NameFramework)
                        time.sleep(4)
                        break

                driver.implicitly_wait(100)
                time.sleep(10)

                if len(self.data.BuildOptions) > 0:
                    self.configirationBuild(driver, self.data.buildOptions)

                if len(self.data.Env) > 0:
                    self.configirationEnv(driver, self.data.env)

                driver.implicitly_wait(100)
                time.sleep(10)

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[3]/
                            div[2]/div/article[1]/div/div[2]/div[2]/
                            div/button"""
                Btn = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )
                Btn.click()

                driver.implicitly_wait(100)
                time.sleep(80)

                succes = driver.find_element(
                    "xpath",
                    '//*[@id="__next"]/div[2]/div/div[3]/div/div[1]/div[1]/div/h3',
                )
                if succes.is_displayed():
                    BtnSuccess = driver.find_element(
                        "xpath",
                        '//*[@id="__next"]/div[2]/div/div[3]/div/div[1]/div[2]/span/a',
                    ).get_attribute("href")

                    driver.get(BtnSuccess)
                    driver.implicitly_wait(100)
                    time.sleep(3)
                    titleProduction = driver.find_element(
                        "xpath",
                        '//*[@id="__next"]/div[2]/div/div[3]/div[2]/div[1]/div/div/h3',
                    )
                    if titleProduction.is_displayed():
                        xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div[2]/
                                    div/
                                    div/div/div[1]/div/div/div[2]/span/div/div[2]/
                                    dl/dd/span/div/a"""
                        LinkPage = driver.find_element(
                            "xpath",
                            xpath.replace("\n", "").replace(" ", ""),
                        ).get_attribute("href")
                        print(LinkPage)
                    print("Project Create")
                    return True
        except Exception as err:
            print(f"Error in Create Project -> {err}")
            return False

    def DeleteProject(self):
        try:
            driver = self.Login()
            if self.data.Login:
                driver.implicitly_wait(100)
                urlGroup = self.data.link % (self.data.group)
                url = urlGroup + "/%s" % (self.data.nameProject)
                driver.get(url)
                time.sleep(5)
                urlDel = url + "/settings"
                driver.get(urlDel)
                time.sleep(5)
                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/
                                    div[2]/div[8]/div/footer/div[2]/div/button"""
                DeleteBtn = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )
                DeleteBtn.click()
                time.sleep(5)
                driver.implicitly_wait(100)

                xpath = """/html/body/reach-portal[3]/div[2]/div/div/
                            form/div/div[1]/div/div[2]/div/label[1]/div/p/b"""

                title = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                xpath = """/html/body/reach-portal[3]/div[2]/div/div/form/div/
                            div[1]/div/div[2]/div/label[1]/div/div/input"""
                inputText = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )
                inputText.send_keys(title.text)

                driver.implicitly_wait(100)
                time.sleep(5)

                xpath = """/html/body/reach-portal[3]/div[2]/div/div/form/
                            div/div[1]/div/div[2]/div/label[2]/div/p/b"""
                textDel = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                xpath = """/html/body/reach-portal[3]/div[2]/div/div/
                            form/div/div[1]/div/div[2]/div/label[2]/
                            div/div/input"""
                inputDel = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )
                inputDel.send_keys(textDel.text)
                driver.implicitly_wait(100)
                time.sleep(5)

                xpath = """/html/body/reach-portal[3]/div[2]/div/
                        div/form/footer/button[2]"""
                BtnDel = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )
                BtnDel.click()
                time.sleep(10)
                driver.quit()
                return True
        except Exception as err:
            print(f"Error in delete the project -> {err}")
            return False

    def ReadProject(self):
        try:
            print("antes de login")
            driver = self.Login()
            print("despues login")
            nameProjects = []
            if self.data.login:
                time.sleep(10)
                print("hice login login")
                driver.implicitly_wait(100)
                driver.get(self.data.link % (self.data.group))
                time.sleep(5)
                ContentProject = driver.find_elements(
                    By.CLASS_NAME, "styles_projectCardWrapper__vds4q "
                )
                print(ContentProject)
                for i in range(0, len(ContentProject)):
                    xpath = f"""//*[@id="__next"]/div[2]/div/div[3]/div/
                                div/div/div[2]/div[{i+1}]/div/div/div/
                                div[1]/div/div/p[1]"""
                    el_hrefs = driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                    nameProjects.append(el_hrefs.text)
                driver.quit()
                return nameProjects
        except Exception as err:
            print(f"Error in Read the project -> {err}")
            return False

    def UpdateProject(self):
        try:
            driver = self.Login()
            if self.data.login:
                time.sleep(5)
                driver.implicitly_wait(100)
                driver.get(self.data.Link % (self.data.group))
                ContentProject = driver.find_elements(
                    By.CLASS_NAME, "styles_projectCardWrapper__vds4q "
                )
                for i in range(0, len(ContentProject)):
                    xpath = f"""//*[@id="__next"]/div[2]/div/div[3]/div/
                                div/div/div[2]/div[{i+1}]/div/div/div/
                                div[1]/div/div/p[1]"""
                    # //*[@id="__next"]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div/div[1]/div/div/p[1]
                    el_hrefs = driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                    if el_hrefs.text == self.data.nameProject.lower():
                        xpathProject = f"""//*[@id="__next"]/div[2]/div/div[3]/
                                            div/div/div/div[2]/div[{i+1}]/div/a"""
                        project = driver.find_element(
                            "xpath", xpathProject.replace("\n", "").replace(" ", "")
                        ).get_attribute("href")
                        driver.get(project)
                        time.sleep(5)
                        break

                driver.implicitly_wait(100)
                LinkSettings = driver.find_element(
                    "xpath",
                    '//*[@id="sub-menu-inner"]/div/div/a[7]',
                ).get_attribute("href")
                # //*[@id="sub-menu-inner"]/div/div/a[7]
                # /html/body/div[1]/div[2]/div/div[1]/nav/div/div/div/div/div/a[7]
                driver.get(LinkSettings)
                driver.implicitly_wait(100)
                time.sleep(10)

                if len(self.data.updateProject) > 1:
                    xpath = """//*[@id="__next"]/div[2]/div/div[3]/
                                div[2]/div/div[2]/div[1]/div/
                                div/div[1]/input"""
                    inputName = driver.find_element(
                        "xpath",
                        xpath.replace("\n", "").replace(" ", ""),
                    )
                    time.sleep(10)
                    inputName.clear()
                    time.sleep(10)
                    inputName.send_keys(self.data.updateProject)

                    xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/
                                div/div[2]/div[1]/div/footer/div[2]/div/button"""

                    btnSaveName = driver.find_element(
                        "xpath",
                        xpath.replace("\n", "").replace(" ", ""),
                    )
                    btnSaveName.click()

                if len(self.data.framework) > 0:
                    dropdown = Select(driver.find_element("name", "framework"))
                    for option in dropdown.options:
                        # if option.text == self.data.Framework:
                        if option.get_attribute("value") == self.data.framework:
                            NameFramework = self.validateFramework(self.data.framework)
                            dropdown.select_by_value(NameFramework)
                            time.sleep(5)
                            break

                if len(self.data.BuildOptions) > 0:
                    self.configirationBuild(driver, self.data.buildOptions, True)
                driver.implicitly_wait(100)
                time.sleep(10)

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/
                            div/div[2]/div[2]/div/footer/div[2]/div/button"""
                # //*[@id="__next"]/div[2]/div/div[3]/div[2]/div/div[2]/div[2]/div/footer/div[2]/div/button
                btnSaveConfig = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )
                btnSaveConfig.click()
                return True
        except Exception as err:
            print(f"Error in update the project -> {err}")
            return False

    def get_link_login(self):
        try:
            session = init()
            driver = session.driver()
            driver.get(self.data.link % ("login"))

            xpath = """//*[@id="__next"]/div/div/div[3]
                        /div[1]/div[2]/div/div/
                        span[1]/button"""
            linkGitlab = driver.find_element(
                "xpath", xpath.replace("\n", "").replace(" ", "")
            )
            if linkGitlab.is_displayed():
                self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

            linkGitlab.click()
            driver.implicitly_wait(100)
            time.sleep(7)
            WebDriverWait(driver, 100).until(EC.number_of_windows_to_be(2))
            child = driver.window_handles[1]
            driver.switch_to.window(child)
            driver.implicitly_wait(100)
            time.sleep(7)
            inputUser = driver.find_element("id", "login_field")
            if inputUser.is_displayed():
                self.data.checkList.append("login_field")

            inputPass = driver.find_element("id", "password")
            if inputPass.is_displayed():
                self.data.checkList.append("password")

            driver.quit()
            return self.data.checkList
        except Exception as err:
            print(f"Error in update the project -> {err}")
            return False

    def get_link_new_project(self):
        try:
            driver = self.Login()
            if self.data.login:
                driver.get(self.data.linkNewProject % (self.data.group))
                ##
                driver.implicitly_wait(100)
                time.sleep(7)
                content2 = driver.find_element(
                    By.CLASS_NAME, "select-git-repository_repoList__dhfLA"
                )

                if content2.is_displayed():
                    className = content2.get_attribute("class").split()
                    self.data.checkList.append(className[-1])

                LinkPage = content2.find_elements(By.CLASS_NAME, "button_base__BjwbK")
                if LinkPage:
                    self.data.checkList.append("button_base__BjwbK")

                time.sleep(5)

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[1]
                            /div/div[3]/div[1]/div/div[2]/div/div/
                            div[2]/div/div[1]/div/div/div[3]/div/a"""
                linkGitlab = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                ).get_attribute("href")

                if linkGitlab:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.implicitly_wait(100)
                time.sleep(5)
                driver.get(linkGitlab)

                #
                xpath = """//*[@id="__next"]/div/div/div[3]/
                            div[3]/div[2]/div/article[1]/div/
                            div[2]/div[1]/div[3]"""

                inputConfig = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if inputConfig:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """//*[@id="__next"]/div/div/div[3]/div[3]/
                div[2]/div/article[1]/div/div[2]/div[1]/div[4]/div"""

                inputEnv = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if inputEnv:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[3]/
                            div[2]/div/article[1]/div/div[2]/div[2]/
                            div/button/span"""

                deploy = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                if deploy:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                return self.data.checkList

        except Exception as err:
            print(f"Error in update the project -> {err}")
            return False

    def get_link_Read_Project(self):
        try:
            driver = self.Login()
            if self.data.login:
                time.sleep(10)
                driver.implicitly_wait(100)
                driver.get(self.data.Link % (self.data.group))
                time.sleep(5)
                ContentProject = driver.find_elements(
                    By.CLASS_NAME, "styles_projectCardWrapper__vds4q "
                )
                if ContentProject:
                    self.data.checkList.append("styles_projectCardWrapper__vds4q ")

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div/
                            div/div/div[2]/div/div/div/
                            div/div[1]/div/div/p[1]"""
                el_hrefs = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                if el_hrefs.is_displayed():
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))
                driver.quit()
                return self.data.checkList
        except Exception as err:
            print(f"Error in Read the project -> {err}")
            return False

    def get_link_Delete_Project(self):
        try:
            driver = self.Login()
            if self.data.login:
                time.sleep(5)
                driver.implicitly_wait(100)
                driver.get(self.data.link % (self.data.group))
                ContentProject = driver.find_elements(
                    By.CLASS_NAME, "styles_projectCardWrapper__vds4q "
                )

                if ContentProject:
                    self.data.checkList.append("styles_projectCardWrapper__vds4q ")

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div/div/
                            div/div[2]/div/div/a"""

                projects = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                ).get_attribute("href")
                time.sleep(5)

                if projects:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.get(projects)
                driver.implicitly_wait(100)

                xpath = """//*[@id="sub-menu-inner"]/div/div/a[7]"""
                LinkSettings = driver.find_element("xpath", xpath).get_attribute("href")

                driver.get(LinkSettings)

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/div/
                                    div[2]/div[8]/div/footer/div[2]/div/button"""
                DeleteBtn = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                DeleteBtn.click()
                if DeleteBtn:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                time.sleep(5)
                driver.implicitly_wait(100)

                xpath = """/html/body/reach-portal[3]/div[2]/div/div/
                            form/div/div[1]/div/div[2]/div/label[1]/div/p/b"""

                title = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if title:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """/html/body/reach-portal[3]/div[2]/div/div/form/div/
                            div[1]/div/div[2]/div/label[1]/div/div/input"""
                inputText = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if inputText:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.implicitly_wait(100)
                time.sleep(5)

                xpath = """/html/body/reach-portal[3]/div[2]/div/div/form/
                            div/div[1]/div/div[2]/div/label[2]/div/p/b"""
                textDel = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if textDel:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """/html/body/reach-portal[3]/div[2]/div/div/
                            form/div/div[1]/div/div[2]/div/label[2]/
                            div/div/input"""
                inputDel = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if inputDel:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.implicitly_wait(100)
                time.sleep(5)

                xpath = """/html/body/reach-portal[3]/div[2]/div/
                        div/form/footer/button[2]"""
                BtnDel = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if BtnDel:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.quit()
                return self.data.checkList
        except Exception as err:
            print(f"Error in delete the project -> {err}")
            return False

    def get_link_Update_Project(self):
        try:
            driver = self.Login()
            if self.data.login:
                time.sleep(5)
                driver.implicitly_wait(100)
                driver.get(self.data.link % (self.data.group))
                ContentProject = driver.find_elements(
                    By.CLASS_NAME, "styles_projectCardWrapper__vds4q "
                )

                if ContentProject:
                    self.data.checkList.append("styles_projectCardWrapper__vds4q ")

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div/
                            div/div/div[2]/div/div/a"""

                projects = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                ).get_attribute("href")
                time.sleep(5)

                if projects:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.get(projects)
                driver.implicitly_wait(100)

                xpath = """//*[@id="sub-menu-inner"]/div/div/a[7]"""
                LinkSettings = driver.find_element("xpath", xpath).get_attribute("href")

                if LinkSettings:
                    self.data.checkList.append(xpath)

                driver.get(LinkSettings)
                driver.implicitly_wait(100)
                time.sleep(10)

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/
                            div[2]/div/div[2]/div[1]/div/
                            div/div[1]/input"""
                inputName = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if inputName:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/
                            div/div[2]/div[1]/div/footer/div[2]/div/button"""

                btnSaveName = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if btnSaveName:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/
                            div/div[2]/div[2]/div/footer/div[2]/div/button"""

                btnSaveConfig = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )

                if btnSaveConfig:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                return self.data.checkList
        except Exception as err:
            print(f"Error in update the project -> {err}")
            return False
