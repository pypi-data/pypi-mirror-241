import time
import json
from ..interfaces.Repository import RepoInterface
from ..service.src.Interfaces.git import RepoAPI
from .dataClass import Repository, TypeProjectTemplate


class Repo(RepoInterface):
    def __init__(
        self,
        repositoryClass: RepoAPI,
        dataRepo: Repository = None,
        cloneRepo: TypeProjectTemplate = None,
    ):
        self.Service = repositoryClass
        self.data = dataRepo
        self.cloneData = cloneRepo

    def create_repository(self):
        try:
            repo = self.Service.create_repo(self.data.name)
            time.sleep(5)
            if len(self.data.users) > 0:
                for id in self.data.users:
                    self.Service.add_users_to_repo(repo.id, id)
            return repo
        except Exception as err:
            raise Exception(f"Error creating repository: {err}")

    def update_repository(self):
        try:
            if(self.data.new_name_repo):
                repo = self.Service.update_repo(self.data.name, self.data.new_name_repo,
                                                self.data.new_description)
            if len(self.data.users) > 0:
                for id in self.data.users:
                    self.Service.add_users_to_repo(self.data.name, id)

            if len(self.data.users_del) > 0:
                for id in self.data.users_del:
                    self.Service.remove_users_from_repo(self.data.name, id)

            repo = self.Service.get_project(self.data.name)
            return repo
        except Exception as err:
            raise Exception(f"Error updating repository: {err}")

    def delete_repository(self):
        try:
            repo = self.Service.delete_repo(self.data.name)
            return repo
        except Exception as err:
            raise Exception(f"Error deleting repository: {err}")

    def get_repository(self):
        try:
            repo = self.Service.get_project(self.data.name)
            return repo
        except Exception as err:
            raise Exception(f"Error getting repository: {err}")

    def clone_repository(self):
        try:
            cloneProject = self.Service.clone_repo(
                projectId=self.cloneData.repo_template,
                branchName=self.cloneData.branch,
                user=self.cloneData.user,
                password=self.cloneData.password,
            )
            nameTemplate = self.Service.get_project(self.cloneData.repo_template)
            PushProject = self.Service.clone_and_push_repo(
                url=self.cloneData.cloneUrl,
                NewDirectory=self.cloneData.name,
                templateName=nameTemplate.path,
                isJenkins=self.cloneData.provider,
            )
            RemoveProject = self.Service.remove_to_folders(
                self.cloneData.name, nameTemplate.path
            )

            if not cloneProject:
                raise Exception("Cannot clone reference repository")

            if not nameTemplate:
                raise Exception("The Repository does not exist")

            if not PushProject:
                raise Exception("Cannot clone and pull")

            if not RemoveProject:
                raise Exception("Cannot delete folders")

            return True
        except Exception as err:
            raise Exception(f"Error cloning repository: {err}")

    def create_commit_and_push(self):
        try:
            repo = self.Service.create_commit_and_push(self.data.name, self.data.branch, self.data.nameZip ,self.data.is_zip)
            return repo
        except Exception as e:
            print(f"Error al cargar el archivo ZIP en S3: {e}")
            return False

    def clone_template(self):
        try:
            repo = self.Service.clone_and_push_repo(self.data.template, self.data.branch, self.data.name)
            return repo
        except Exception as e:
            print(f"Error al cargar el archivo ZIP en S3: {e}")
            return False

