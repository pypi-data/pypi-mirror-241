import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from ..Interfaces.interfaces import BaseInterface
from ..utils.utils import init
from .dataClass import DataClass


class JenkinsInterface(BaseInterface):
    def __init__(self, data: DataClass):
        self.data = data

    def getTokenJenkins(self):
        pass

    def Login(self):
        session = init()
        driver = session.driver()
        driver.get(self.data.link)
        driver.implicitly_wait(100)
        time.sleep(3)
        username = driver.find_element("xpath", '//*[@id="j_username"]')
        username.send_keys(self.data.user)
        password = driver.find_element("xpath", "/html/body/div/div/form/div[2]/input")
        password.send_keys(self.data.password)
        path = "/html/body/div[1]/div/form/div[4]/button"
        btnLogin = driver.find_element("xpath", path)
        btnLogin.click()
        driver.implicitly_wait(100)
        time.sleep(3)
        try:
            path = '//*[@id="breadcrumbs"]/li[1]/a'
            SuccessLogin = driver.find_element("xpath", path)
            if SuccessLogin:
                self.data.login = True
                return driver
        except Exception as err:
            failPass = driver.find_element("xpath", "/html/body/div/div/form/div[1]")
            if failPass:
                print("Invalid username or password")
                return driver
            print(f"Error in login Jenkins {err}")

        try:
            driver = self.Login()
            if self.data.login:
                path = '//*[@id="projectstatus"]/tbody/tr'
                Projects = driver.find_elements("xpath", path)
                for row in range(0, len(Projects)):
                    xpath = f"""/html/body/div[3]/div[2]/div[2]/div[2]/table/
                                tbody/tr[{row+1}]/td[3]/a/span"""
                    project = driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                    if project.text == "Projects":
                        project.click()
                        break
                newItem = driver.find_element("xpath", '//*[@id="tasks"]/div[3]/span/a')
                newItem.click()
                time.sleep(3)
                NamefolderProject = driver.find_element("id", "name")
                NamefolderProject.send_keys(self.data.nameProject)
                xpath = '//*[@id="j-add-item-type-nested-projects"]/ul/li[1]/div[1]'
                folderProject = driver.find_element("xpath", xpath)
                folderProject.click()
                CreateFolder = driver.find_element("xpath", '//*[@id="ok-button"]')
                CreateFolder.click()
                time.sleep(2)
                SaveProject = driver.find_element(
                    "xpath", '//*[@id="bottom-sticker"]/div/button[1]'
                )
                SaveProject.click()
                time.sleep(2)
                addProject = driver.find_element(
                    "xpath", '//*[@id="tasks"]/div[3]/span/a'
                )
                addProject.click()
                NameNewProject = driver.find_element("id", "name")
                NameNewProject.send_keys(self.data.nameProject)
                driver.implicitly_wait(100)
                time.sleep(3)
                xpath = '//*[@id="j-add-item-type-standalone-projects"]/ul/li[2]/div[1]'
                typeProject = driver.find_element("xpath", xpath)
                typeProject.click()
                BtnOK = driver.find_element("xpath", '//*[@id="ok-button"]')
                BtnOK.click()
                driver.implicitly_wait(100)
                time.sleep(6)

                xpath = """//*[@id="main-panel"]/form/div[1]/div[3]/div[2]/div[4]/
                            div[2]/div[1]/div/span/label"""
                discardBuild = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                discardBuild.click()
                driver.implicitly_wait(100)
                time.sleep(5)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[3]/div[2]/div[4]/
                            div[2]/div[4]/div[2]/div/div/div[3]/div[3]/input"""
                maxBuild = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                maxBuild.send_keys("3")
                driver.implicitly_wait(100)
                time.sleep(5)
                element = driver.find_element(
                    By.NAME, "com-dabsquared-gitlabjenkins-GitLabPushTrigger"
                )
                driver.execute_script("arguments[0].click();", element)
                time.sleep(3)
                xpath = (
                    """//*[@id="main-panel"]/form/div[1]/div[7]/div[2]/div[2]/select"""
                )
                dropdown = Select(driver.find_element("xpath", xpath))
                for option in dropdown.options:
                    if option.text == "Pipeline script from SCM":
                        dropdown.select_by_visible_text("Pipeline script from SCM")
                        time.sleep(4)
                        break

                driver.implicitly_wait(100)
                time.sleep(5)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[7]/div[3]/
                              div/div/div[8]/div[3]/select"""
                dropdownGit = Select(
                    driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                )
                for option in dropdownGit.options:
                    if option.text == "Git":
                        dropdownGit.select_by_visible_text("Git")
                        time.sleep(4)
                        break

                driver.implicitly_wait(100)
                time.sleep(5)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[7]/div[3]/
                            div/div/div[9]/div/div/div[6]/div[2]/
                            div/div[1]/div/div[1]/div[2]/input"""
                inputUrl = driver.find_element(
                    "xpath",
                    xpath.replace("\n", "").replace(" ", ""),
                )
                inputUrl.send_keys(self.data.url)

                driver.implicitly_wait(100)
                time.sleep(5)

                xpath = """//*[@id="main-panel"]/form/div[1]/div[7]/div[3]/div/div/
                            div[9]/div/div/div[6]/div[2]/div/div[1]/
                            div/div[2]/div[2]/div/div/div[1]/select"""
                dropdownCredentials = Select(
                    driver.find_element(
                        "xpath",
                        xpath.replace("\n", "").replace(" ", ""),
                    )
                )
                for option in dropdownCredentials.options:
                    if option.text == "novateva (Gitlab SSH)":
                        dropdownCredentials.select_by_visible_text(
                            "novateva (Gitlab SSH)"
                        )
                        time.sleep(4)
                        break
                print("estoy aqui")
                driver.implicitly_wait(100)
                time.sleep(5)
                # save = driver.find_element("xpath", '//*[@id="yui-gen10-button"]')
                save = driver.find_element(
                    "xpath", '//*[@id="bottom-sticker"]/div/button[1]'
                )
                save.click()
                print("Project Create")
                return True
        except Exception as err:
            print(f"Error in Create Project -> {err}")
            return False

    def CreateProject(self):
        try:
            driver = self.Login()
            if self.data.login:
                url = "http://jenkins.novateva.tech/job/Projects/newJob"
                driver.get(url)
                time.sleep(3)
                NamefolderProject = driver.find_element("id", "name")
                NamefolderProject.send_keys(self.data.nameProject)
                xpath = '//*[@id="j-add-item-type-nested-projects"]/ul/li[1]/div[1]'
                folderProject = driver.find_element("xpath", xpath)
                folderProject.click()
                CreateFolder = driver.find_element("xpath", '//*[@id="ok-button"]')
                CreateFolder.click()
                time.sleep(2)
                SaveProject = driver.find_element(
                    "xpath", '//*[@id="bottom-sticker"]/div/button[1]'
                )
                SaveProject.click()
                time.sleep(2)
                addProject = driver.find_element(
                    "xpath", '//*[@id="tasks"]/div[3]/span/a'
                )
                addProject.click()
                NameNewProject = driver.find_element("id", "name")
                NameNewProject.send_keys(self.data.nameProject)
                driver.implicitly_wait(100)
                time.sleep(3)
                xpath = '//*[@id="j-add-item-type-nested-projects"]/ul/li[2]/label/span'
                typeProject = driver.find_element("xpath", xpath)
                typeProject.click()
                BtnOK = driver.find_element("xpath", '//*[@id="ok-button"]')
                BtnOK.click()
                driver.implicitly_wait(100)
                time.sleep(6)
                ##

                searchGit = driver.find_element("xpath", '//*[@id="yui-gen1-button"]')
                searchGit.click()

                git = driver.find_element("xpath", '//*[@id="yui-gen8"]/a')
                git.click()
                time.sleep(5)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/
                        div/div/div[1]/div/div[2]/div/div/div[3]/div[2]/
                        div/div/div[1]/select"""
                dropdown = Select(
                    driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                )
                for option in dropdown.options:
                    if option.text == "Novateva (Ec2)":
                        dropdown.select_by_visible_text("Novateva (Ec2)")
                        time.sleep(4)
                        break
                time.sleep(10)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/
                    div/div/div[1]/div/div[2]/div/div/div[4]/div[2]/input"""
                owner = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                owner.send_keys("novateva")
                time.sleep(5)

                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/
                            div[2]/div/div/div[1]/div/div[2]/
                            div/div/div[4]/div[1]/a"""
                clickInfo = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                clickInfo.click()
                time.sleep(15)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/div/div/
                    div[1]/div/div[2]/div/div/div[5]/div[2]/div/select"""
                dropdownProjects = Select(
                    driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                )
                for option in dropdownProjects.options:
                    name = "novateva/%s" % self.data.nameProject.lower()
                    if option.text == name:
                        dropdownProjects.select_by_visible_text(name)
                        time.sleep(4)
                        break
                time.sleep(5)

                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/
                        div[2]/div/div/div[1]/div/div[2]/div/
                        div/div[6]/div[2]/div/div[2]/div/div[3]/
                        div[2]/div/select"""
                dropdownBranches = Select(
                    driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                )
                for option in dropdownBranches.options:
                    if option.text == "All branches":
                        dropdownBranches.select_by_visible_text("All branches")
                        time.sleep(4)
                        break
                time.sleep(5)

                xpath = """//*[@id="main-panel"]/form/div[1]/div[7]/
                            div[3]/div/div/div[3]/div[3]/div[2]/
                            div[3]/input"""
                discardBuild = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                discardBuild.send_keys("3")

                save = driver.find_element(
                    "xpath", '//*[@id="bottom-sticker"]/div/button[1]'
                )
                save.click()
                time.sleep(5)
                driver.quit()
                return True
        except Exception as err:
            raise Exception(f"Error in Create Project: {err}")

    def UpdateProject(self):
        try:
            driver = self.Login()
            if self.data.login:
                url = (
                    "http://jenkins.novateva.tech/job/Projects/job/%s/confirm-rename"
                    % self.data.nameProject
                )
                driver.get(url)
                rename = driver.find_element(
                    "xpath", '//*[@id="main-panel"]/form/div[1]/div[1]/div[2]/input'
                )
                time.sleep(3)
                rename.clear()
                time.sleep(3)
                rename.send_keys(self.data.updateProject)
                btnSave = driver.find_element(
                    "xpath", '//*[@id="bottom-sticker"]/div/button'
                )
                btnSave.click()
                time.sleep(10)
                Urlpath = """http://jenkins.novateva.tech/job/Projects/
                            job/%s/job/%s/confirm-rename"""
                url = Urlpath.replace("\n", "").replace(" ", "") % (
                    self.data.updateProject,
                    self.data.nameProject,
                )
                driver.get(url)

                rename = driver.find_element(
                    "xpath", '//*[@id="main-panel"]/form/div[1]/div[1]/div[2]/input'
                )
                time.sleep(3)
                rename.clear()
                time.sleep(3)
                rename.send_keys(self.data.updateProject)
                btnSave = driver.find_element(
                    "xpath", '//*[@id="bottom-sticker"]/div/button'
                )
                btnSave.click()
                driver.quit()
                return True
        except Exception as err:
            raise Exception(f"Error in update the project: {err}")

    def DeleteProject(self):
        try:
            driver = self.Login()
            if self.data.login:
                url = "http://jenkins.novateva.tech/job/Projects/job/%s/delete" % (
                    self.data.nameProject
                )
                driver.get(url)

                btnDelete = driver.find_element(
                    "xpath", '//*[@id="main-panel"]/form/button'
                )
                btnDelete.click()
                time.sleep(5)
                driver.quit()
                return True
        except Exception as err:
            raise Exception(f"Error in delete the project: {err}")

    def ReadProject(self):
        try:
            driver = self.Login()
            if self.data.login:
                nameProjects = []
                url = "http://jenkins.novateva.tech/job/Projects/"
                driver.get(url)
                projects = driver.find_elements(
                    "xpath", '//*[@id="projectstatus"]/tbody/tr'
                )
                for rows in range(0, len(projects)):
                    if len(projects) == 1:
                        xpaths = """/html/body/div[3]/div[2]/div[3]/div[2]/
                                    table/tbody/tr/td[3]/a/span"""
                    else:
                        xpaths = f"""/html/body/div[3]/div[2]/div[3]/div[2]/table/tbody
                                    /tr[{rows+1}]/td[3]/a/span"""
                    itemProjects = driver.find_element(
                        "xpath", xpaths.replace("\n", "").replace(" ", "")
                    )
                    nameProjects.append(itemProjects.text)
                driver.quit()
                return nameProjects
        except Exception as err:
            raise Exception(f"Error in Read the project: {err}")

    def ConfigurationEnv(self):
        try:
            driver = self.Login()
            if self.data.login:
                driver.get(self.data.linkConfig)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[9]/
                            div[2]/div[2]/div[3]/div[3]/div/div[2]/div"""
                listEnv = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                driver.execute_script("arguments[0].scrollIntoView(true);", listEnv)
                add = driver.find_element("xpath", '//*[@id="yui-gen32-button"]')
                driver.execute_script("arguments[0].click();", add)
                driver.implicitly_wait(100)
                time.sleep(3)
                if len(self.data.Env) > 0:
                    i = 0
                    for keys, values in self.data.env.items():
                        list2 = driver.find_elements(By.NAME, "env")
                        count = len(list2)
                        item = count + 1
                        add = driver.find_element(By.CLASS_NAME, "repeatable-add")
                        driver.execute_script("arguments[0].click();", add)
                        driver.implicitly_wait(100)
                        time.sleep(3)
                        xpathNa = f"""//*[@id="main-panel"]/form/div[1]/div[9]/div[2]/
                                        div[2]/div[3]/div[3]/div/div[2]/div/div[{item}]/
                                        div[2]/div[2]/input"""
                        xpathName = driver.find_element(
                            "xpath", xpathNa.replace("\n", "").replace(" ", "")
                        )
                        xpathName.send_keys(keys)
                        driver.implicitly_wait(100)
                        time.sleep(3)
                        xpathVal = f"""//*[@id="main-panel"]/form/div[1]/div[9]/div[2]/
                                      div[2]/div[3]/div[3]/div/div[2]/div/
                                      div[{item}]/div[3]/div[2]/input"""
                        xpathValue = driver.find_element("xpath", xpathVal)
                        xpathValue.send_keys(values)
                        i += 1
                    time.sleep(5)
                    btnSave = driver.find_element(
                        "xpath", '//*[@id="yui-gen49-button"]'
                    )
                    btnSave.click()
                return True
        except Exception as err:
            raise Exception(f"Error in Configuration Env: {err}")

    def get_link_Login(self):
        try:
            session = init()
            driver = session.driver()
            driver.get(self.data.link)
            driver.implicitly_wait(100)
            time.sleep(3)
            username = driver.find_element("xpath", '//*[@id="j_username"]')
            if username.is_displayed():
                self.data.checkList.append(username.get_attribute("id"))

            xpath = """/html/body/div/div/form/div[2]/input"""
            password = driver.find_element("xpath", xpath)
            if password.is_displayed():
                self.data.checkList.append("/html/body/div/div/form/div[2]/input")

            path = "/html/body/div[1]/div/form/div[4]/button"
            btnLogin = driver.find_element("xpath", path)
            if btnLogin.is_displayed():
                self.data.checkList.append("/html/body/div[1]/div/form/div[4]/button")

            driver.quit()
            return self.data.checkList
        except Exception as err:
            raise Exception(f"Error in login Jenkins: {err}")

    def get_link_Create_Project(self):
        try:
            driver = self.Login()
            if self.data.login:
                url = "http://jenkins.novateva.tech/job/Projects/newJob"
                driver.get(url)

                NamefolderProject = driver.find_element("id", "name")
                NamefolderProject.send_keys(self.data.nameProject)
                if NamefolderProject:
                    self.data.checkList.append("name")
                time.sleep(3)

                xpath = '//*[@id="j-add-item-type-nested-projects"]/ul/li[1]/div[1]'
                folderProject = driver.find_element("xpath", xpath)
                if folderProject.is_displayed():
                    self.data.checkList.append(xpath)
                    folderProject.click()
                time.sleep(3)

                xpath = '//*[@id="ok-button"]'
                CreateFolder = driver.find_element("xpath", xpath)
                if CreateFolder:
                    self.data.checkList.append(xpath)
                    CreateFolder.click()

                time.sleep(3)

                xpath = '//*[@id="bottom-sticker"]/div/button[1]'
                SaveProject = driver.find_element("xpath", xpath)
                if SaveProject:
                    self.data.checkList.append(xpath)
                    SaveProject.click()

                time.sleep(2)
                xpath = '//*[@id="tasks"]/div[3]/span/a'
                addProject = driver.find_element("xpath", xpath)
                if addProject:
                    self.data.checkList.append(xpath)
                    addProject.click()

                NameNewProject = driver.find_element("id", "name")
                if NameNewProject:
                    self.data.checkList.append("name")
                    NameNewProject.send_keys(self.data.nameProject)

                driver.implicitly_wait(100)
                time.sleep(3)
                xpath = '//*[@id="j-add-item-type-nested-projects"]/ul/li[2]/label/span'
                typeProject = driver.find_element("xpath", xpath)
                if typeProject:
                    self.data.checkList.append(xpath)
                    typeProject.click()

                time.sleep(3)

                xpath = '//*[@id="ok-button"]'
                BtnOK = driver.find_element("xpath", xpath)
                if BtnOK:
                    self.data.checkList.append(xpath)
                    BtnOK.click()

                driver.implicitly_wait(100)
                time.sleep(6)

                xpath = '//*[@id="yui-gen1-button"]'
                searchGit = driver.find_element("xpath", xpath)
                if searchGit:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))
                    searchGit.click()

                xpath = '//*[@id="yui-gen8"]/a'
                git = driver.find_element("xpath", xpath)
                if git:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))
                    git.click()

                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/
                        div/div/div[1]/div/div[2]/div/div/div[3]/div[2]/
                        div/div/div[1]/select"""

                dropdown = Select(
                    driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                )

                if dropdown:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                time.sleep(10)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/
                    div/div/div[1]/div/div[2]/div/div/div[4]/div[2]/input"""
                owner = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                if owner:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/
                            div/div/div[1]/div/div[2]/div/
                            div/div[4]/div[1]/a"""
                clickInfo = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                if clickInfo.is_displayed():
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/div/div/
                    div[1]/div/div[2]/div/div/div[5]/div[2]/div/select"""

                dropdownProjects = Select(
                    driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                )
                if dropdownProjects:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))
                time.sleep(5)

                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/
                        div[2]/div/div/div[1]/div/div[2]/div/
                        div/div[6]/div[2]/div/div[2]/div/div[3]/
                        div[2]/div/select"""
                dropdownBranches = Select(
                    driver.find_element(
                        "xpath", xpath.replace("\n", "").replace(" ", "")
                    )
                )
                if dropdownBranches:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/
                            div/div/div[1]/div/div[2]/div/div/div[6]/
                            div[2]/div/div[6]/div/div[11]/div/div/button"""
                closeWebHooks = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                if closeWebHooks.is_displayed():
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = """//*[@id="main-panel"]/form/div[1]/div[7]/div[3]/
                            div/div/div[3]/div[3]/div[2]/div[3]/input"""
                discardBuild = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                if discardBuild:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = '//*[@id="bottom-sticker"]/div/button[1]'
                save = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )
                save.click()
                if save:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))
                time.sleep(5)
                driver.back()
                time.sleep(5)
                url = "http://jenkins.novateva.tech/job/Projects/job/%s/delete" % (
                    self.data.nameProject
                )
                driver.get(url)

                btnDelete = driver.find_element(
                    "xpath", '//*[@id="main-panel"]/form/button'
                )
                btnDelete.click()
                driver.quit()
                return self.data.checkList
        except Exception as err:
            raise Exception(f"Error in get link Project: {err}")

    def get_link_Read_Project(self):
        try:
            driver = self.Login()
            if self.data.Login:
                url = "http://jenkins.novateva.tech/job/Projects/"
                driver.get(url)
                xpath = '//*[@id="projectstatus"]/tbody/tr'
                projects = driver.find_elements("xpath", xpath)
                if projects:
                    self.data.checkList.append(xpath)
                    xpath = """/html/body/div[3]/div[2]/div[3]/
                            div[2]/table/tbody/tr"""
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.quit()
                return self.data.checkList
        except Exception as err:
            raise Exception(f"Error in get link Read the project: {err}")

    def get_link_Delete_Project(self):
        try:
            driver = self.Login()
            if self.data.login:
                url = "http://jenkins.novateva.tech/job/Projects/"
                driver.get(url)
                time.sleep(5)

                xpath = """/html/body/div[3]/div[2]/div[3]/div[2]/
                        table/tbody/tr/td[3]/a"""
                Link = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                ).get_attribute("href")

                if Link:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.get(Link + "/delete")
                driver.implicitly_wait(100)
                time.sleep(3)

                xpath = '//*[@id="main-panel"]/form/button'
                btnDelete = driver.find_element("xpath", xpath)

                if btnDelete:
                    self.data.checkList.append(xpath)

                driver.quit()
                return self.data.checkList
        except Exception as err:
            raise Exception(f"Error in get link delete the project: {err}")

    def get_link_Update_Project(self):
        try:
            driver = self.Login()
            if self.data.login:
                url = "http://jenkins.novateva.tech/job/Projects/"
                driver.get(url)
                time.sleep(5)

                xpath = """/html/body/div[3]/div[2]/div[3]/div[2]/
                        table/tbody/tr/td[3]/a"""
                Link = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                ).get_attribute("href")

                if Link:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                url = Link + "confirm-rename"
                driver.get(url)

                xpath = """//*[@id="main-panel"]/form/div[1]/
                            div[1]/div[2]/input"""
                inputRename = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )

                if inputRename:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = '//*[@id="bottom-sticker"]/div/button'
                btnSave = driver.find_element("xpath", xpath)

                if btnSave:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                time.sleep(3)
                driver.quit()
                return self.data.checkList
        except Exception as err:
            raise Exception(f"Error in get link update the project: {err}")

    '''def get_link_Configuration_Env(self):
        try:
            driver = self.Login()
            if self.data.Login:
                driver.get(self.data.LinkConfig)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[9]/
                            div[2]/div[2]/div[3]/div[3]/div/div[2]/div"""
                listEnv = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )

                if listEnv:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.execute_script("arguments[0].scrollIntoView(true);", listEnv)

                xpath = '//*[@id="yui-gen32-button"]'
                addEnv = driver.find_element("xpath", xpath)

                if addEnv:
                    self.data.checkList.append(xpath)

                driver.execute_script("arguments[0].click();", addEnv)
                driver.implicitly_wait(100)
                time.sleep(3)

                xpath = """//*[@id="main-panel"]/form/div[1]/div[9]/div[2]/div[2]
                            /div[3]/div[3]/div/div[2]/div/div[1]
                            /div[1]/div[2]/input"""
                xpathName = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )

                if xpathName:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                driver.implicitly_wait(100)
                time.sleep(3)
                xpath = """//*[@id="main-panel"]/form/div[1]/div[9]/div[2]/
                                div[2]/div[3]/div[3]/div/div[2]/div/
                                div[1]/div[2]/div[2]/input"""
                xpathValue = driver.find_element(
                    "xpath", xpath.replace("\n", "").replace(" ", "")
                )

                if xpathValue:
                    self.data.checkList.append(xpath.replace("\n", "").replace(" ", ""))

                xpath = '//*[@id="yui-gen49-button"]'
                btnSave = driver.find_element("xpath", xpath)

                if btnSave:
                    self.data.checkList.append(xpath)

                driver.quit()
                return self.data.checkList
        except Exception as err:
            print(f"Error in Configuration Env -> {err}")
            return False'''
