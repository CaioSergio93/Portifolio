class ProjectController:
    @staticmethod
    def get_all_projects():
        # Lógica para obter todos os projetos
        github_link = "https://github.com/CaioSergio93/my-profiles-web-node/tree/master"
        hosting_link = "https://my-profiles-web-node.vercel.app/"
        return {"github_link": github_link, "hosting_link": hosting_link}
