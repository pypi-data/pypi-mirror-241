import unittest
from unittest.mock import MagicMock, Mock, patch

import gitlab
from decouple import config

from src.classes.dataClass import DataClass
from src.classes.jenkins import JenkinsInterface

USER_JENKINS = config("USER_JENKINS")
PASSWORD_JENKINS = config("PASSWORD_JENKINS")

TOKEN_GITLAB = config("TOKEN_GITLAB")
LINK_JENKINS = config("LINK_JENKINS")


class TestCreateRepo(unittest.TestCase):
    def setUp(self):
        self.jenkins = DataClass(
            User=USER_JENKINS,
            Password=PASSWORD_JENKINS,
            NameProject="test_jenkins",
            Login=False,
            Token=TOKEN_GITLAB,
            Link=LINK_JENKINS,
        )
        self.ProjectJenkins = JenkinsInterface(self.jenkins)

    def test_get_link_Login(self):
        inputUser = "j_username"
        inputPass = "/html/body/div/div/form/div[2]/input"
        btnLogin = "/html/body/div[1]/div/form/div[4]/button"
        mock_data = Mock(return_value=[inputUser, inputPass, btnLogin])
        result = self.ProjectJenkins.get_link_Login()
        mock_link = mock_data()
        print(mock_link)
        self.assertEqual(result, mock_link)

    def test_get_link_Create_Project(self):
        NamefolderProjectID = str("name")
        folderProject = """//*[@id="j-add-item-type-nested-projects"]/
                            ul/li[1]/div[1]"""
        CreateFolder = '//*[@id="ok-button"]'
        SaveProject = '//*[@id="bottom-sticker"]/div/button[1]'
        addProject = '//*[@id="tasks"]/div[3]/span/a'
        NameNewProject = "name"
        typeProject = """//*[@id="j-add-item-type-nested-projects"]/ul/
                        li[2]/label/span"""
        BtnOK = '//*[@id="ok-button"]'
        gitLabProject = """//*[@id="yui-gen1-button"]"""
        gitLabName = '//*[@id="yui-gen8"]/a'
        dropdownCredentials = """//*[@id="main-panel"]/form/div[1]/div[4]/
                                div[2]/div/div/div[1]/div/div[2]/div/div/
                                div[3]/div[2]/div/div/div[1]/select"""
        owner = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/div/div/
                    div[1]/div/div[2]/div/div/div[4]/div[2]/input"""
        btnInfo = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/div/
                    div/div[1]/div/div[2]/div/div/div[4]/div[1]/a"""
        projectName = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/
                    div/div/div[1]/div/div[2]/div/div/
                    div[5]/div[2]/div/select"""
        discoverBranch = """//*[@id="main-panel"]/form/div[1]/div[4]/
                        div[2]/div/div/div[1]/div/div[2]/div/div/div[6]/
                        div[2]/div/div[2]/div/div[3]/div[2]/div/select"""
        btnClose = """//*[@id="main-panel"]/form/div[1]/div[4]/div[2]/div/
                    div/div[1]/div/div[2]/div/div/div[6]/div[2]/div/div[6]/
                    div/div[11]/div/div/button"""
        maxBuild = """//*[@id="main-panel"]/form/div[1]/div[7]/div[3]/
                    div/div/div[3]/div[3]/div[2]/div[3]/input"""

        BtnSave = '//*[@id="bottom-sticker"]/div/button[1]'
        mock_data = Mock(
            return_value=[
                NamefolderProjectID,
                folderProject.replace("\n", "").replace(" ", ""),
                CreateFolder,
                SaveProject,
                addProject,
                NameNewProject,
                typeProject.replace("\n", "").replace(" ", ""),
                BtnOK,
                gitLabProject.replace("\n", "").replace(" ", ""),
                gitLabName.replace("\n", "").replace(" ", ""),
                dropdownCredentials.replace("\n", "").replace(" ", ""),
                owner.replace("\n", "").replace(" ", ""),
                btnInfo.replace("\n", "").replace(" ", ""),
                projectName.replace("\n", "").replace(" ", ""),
                discoverBranch.replace("\n", "").replace(" ", ""),
                btnClose.replace("\n", "").replace(" ", ""),
                maxBuild.replace("\n", "").replace(" ", ""),
                BtnSave,
            ]
        )

        result = self.ProjectJenkins.get_link_Create_Project()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)

    def test_get_link_Read_Project(self):
        Projects = '//*[@id="projectstatus"]/tbody/tr'
        ItemsProjects = """/html/body/div[3]/div[2]/div[3]/
                            div[2]/table/tbody/tr"""

        mock_data = Mock(
            return_value=[Projects, ItemsProjects.replace("\n", "").replace(" ", "")]
        )
        result = self.ProjectJenkins.get_link_Read_Project()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)

    def test_get_link_Delete_Project(self):
        Links = """/html/body/div[3]/div[2]/div[3]/div[2]/
                table/tbody/tr/td[3]/a"""
        btnDelete = '//*[@id="main-panel"]/form/button'
        mock_data = Mock(
            return_value=[
                Links.replace("\n", "").replace(" ", ""),
                btnDelete,
            ]
        )
        result = self.ProjectJenkins.get_link_Delete_Project()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)

    def test_get_link_Update_Project(self):
        Projects = """/html/body/div[3]/div[2]/div[3]/div[2]/
                        table/tbody/tr/td[3]/a"""
        inputRename = """//*[@id="main-panel"]/form/div[1]/
                            div[1]/div[2]/input"""
        btnSave = '//*[@id="bottom-sticker"]/div/button'

        mock_data = Mock(
            return_value=[
                Projects.replace("\n", "").replace(" ", ""),
                inputRename.replace("\n", "").replace(" ", ""),
                btnSave,
            ]
        )
        result = self.ProjectJenkins.get_link_Update_Project()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)

    '''def test_get_link_Configuration_Env(self):
        getEnv = """//*[@id="main-panel"]/form/div[1]/div[9]/
                            div[2]/div[2]/div[3]/div[3]/div/div[2]/div"""
        addEnv = '//*[@id="yui-gen32-button"]'
        xpathName = """//*[@id="main-panel"]/form/div[1]/div[9]/div[2]/
                        div[2]/div[3]/div[3]/div/div[2]/
                        div/div[1]/div[1]/div[2]/input"""
        xpathValue = """//*[@id="main-panel"]/form/div[1]/div[9]/div[2]
                        /div[2]/div[3]/div[3]/div/div[2]/
                        div/div[1]/div[2]/div[2]/input"""
        btnSave = '//*[@id="yui-gen49-button"]'
        mock_data = Mock(
            return_value=[
                getEnv.replace("\n", "").replace(" ", ""),
                addEnv,
                xpathName.replace("\n", "").replace(" ", ""),
                xpathValue.replace("\n", "").replace(" ", ""),
                btnSave,
            ]
        )
        result = self.ProjectJenkins.get_link_Configuration_Env()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)'''
