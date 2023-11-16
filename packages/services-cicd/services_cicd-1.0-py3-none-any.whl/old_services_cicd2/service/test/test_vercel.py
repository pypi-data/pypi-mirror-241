import unittest
from unittest.mock import Mock

import gitlab
from decouple import config

from src.classes.dataClass import DataClass
from src.classes.vercel import VercelInterface

USER_VERCEL = config("USER_VERCEL")
PASSWORD_VERCEL = config("PASSWORD_VERCEL")


class TestCreateRepo(unittest.TestCase):
    def setUp(self):
        self.vercel = DataClass()
        self.ProjectVercel = VercelInterface(self.vercel)

    def test_get_link_login(self):
        mock_data = Mock(
            return_value=[
                '//*[@id="__next"]/div/div/div[3]/div[1]/div[2]/div/div/span[1]/button',
                "login_field",
                "password",
            ]
        )
        result = self.ProjectVercel.get_link_login()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)

    def test_get_link_Create_Project(self):
        ListGitClass = "select-git-repository_repoList__dhfLA"
        LinkPage = "button_base__BjwbK"
        linkGitlab = """//*[@id="__next"]/div[2]/div/div[3]/div[1]
                            /div/div[3]/div[1]/div/div[2]/div/div/
                            div[2]/div/div[1]/div/div/div[3]/div/a"""
        inputConfig = """//*[@id="__next"]/div/div/div[3]/
                            div[3]/div[2]/div/article[1]/div/
                            div[2]/div[1]/div[3]"""
        inputEnv = """//*[@id="__next"]/div/div/div[3]/
                        div[3]/div[2]/div/article[1]/
                        div/div[2]/div[1]/div[4]/div"""

        deploy = """//*[@id="__next"]/div[2]/div/div[3]/div[3]/
                            div[2]/div/article[1]/div/div[2]/div[2]/
                            div/button/span"""
        mock_list = Mock(
            return_value=[
                ListGitClass.replace("\n", "").replace(" ", ""),
                LinkPage.replace("\n", "").replace(" ", ""),
                linkGitlab.replace("\n", "").replace(" ", ""),
                inputConfig.replace("\n", "").replace(" ", ""),
                inputEnv.replace("\n", "").replace(" ", ""),
                deploy.replace("\n", "").replace(" ", ""),
            ]
        )
        checkLink = mock_list()
        result = self.ProjectVercel.get_link_new_project()
        self.assertEqual(result, checkLink)

    def test_get_link_Read_Project(self):
        link = """//*[@id="__next"]/div[2]/div/div[3]/div/
                div/div/div[2]/div/div/div/
                div/div[1]/div/div/p[1]"""
        mock_data = Mock(
            return_value=[
                "styles_projectCardWrapper__vds4q ",
                link.replace("\n", "").replace(" ", ""),
            ]
        )
        result = self.ProjectVercel.get_link_Read_Project()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)

    def test_get_link_Delete_Project(self):
        element = """styles_projectCardWrapper__vds4q """
        linkSettings = """//*[@id="__next"]/div[2]/div/div[3]
                /div/div/div/div[2]/div/div/a"""
        DeleteBtn = """//*[@id="__next"]/div[2]/div/div[3]/
                    div[2]/div/div[2]/div[8]/div/
                    footer/div[2]/div/button"""
        titleDelete = """/html/body/reach-portal[3]/div[2]/
                        div/div/form/div/div[1]/div/div[2]/
                        div/label[1]/div/p/b"""
        inputTextDel = """/html/body/reach-portal[3]/div[2]/
                        div/div/form/div/div[1]/div/div[2]/
                        div/label[1]/div/div/input"""
        textDel = """/html/body/reach-portal[3]/div[2]/div/
                    div/form/div/div[1]/div/div[2]/
                    div/label[2]/div/p/b"""
        inputDel = """/html/body/reach-portal[3]/div[2]/div/
                    div/form/div/div[1]/div/div[2]/div/
                    label[2]/div/div/input"""
        BtnDel = """/html/body/reach-portal[3]/div[2]/
                    div/div/form/footer/button[2]"""
        mock_data = Mock(
            return_value=[
                element,
                linkSettings.replace("\n", "").replace(" ", ""),
                DeleteBtn.replace("\n", "").replace(" ", ""),
                titleDelete.replace("\n", "").replace(" ", ""),
                inputTextDel.replace("\n", "").replace(" ", ""),
                textDel.replace("\n", "").replace(" ", ""),
                inputDel.replace("\n", "").replace(" ", ""),
                BtnDel.replace("\n", "").replace(" ", ""),
            ]
        )
        result = self.ProjectVercel.get_link_Delete_Project()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)

    def test_get_link_Update_Project(self):
        ContentProject = """styles_projectCardWrapper__vds4q """
        ProjectLink = """//*[@id="__next"]/div[2]/div/div[3]
                            /div/div/div/div[2]/div/div/a"""
        LinkSettings = """//*[@id="sub-menu-inner"]/div/div/a[7]"""
        inputName = """//*[@id="__next"]/div[2]/div/div[3]/
                            div[2]/div/div[2]/div[1]/div/
                            div/div[1]/input"""
        btnSaveName = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/
                            div/div[2]/div[1]/div/footer/div[2]/div/button"""
        btnSaveConfig = """//*[@id="__next"]/div[2]/div/div[3]/div[2]/
                            div/div[2]/div[2]/div/footer/div[2]/div/button"""

        mock_data = Mock(
            return_value=[
                ContentProject,
                ProjectLink.replace("\n", "").replace(" ", ""),
                LinkSettings.replace("\n", "").replace(" ", ""),
                inputName.replace("\n", "").replace(" ", ""),
                btnSaveName.replace("\n", "").replace(" ", ""),
                btnSaveConfig.replace("\n", "").replace(" ", ""),
            ]
        )
        result = self.ProjectVercel.get_link_Update_Project()
        mock_link = mock_data()
        self.assertEqual(result, mock_link)
