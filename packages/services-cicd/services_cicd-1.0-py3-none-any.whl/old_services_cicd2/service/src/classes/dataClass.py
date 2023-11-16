from dataclasses import dataclass, field


@dataclass
class DataClass:
    user: str = field(default="")
    password: str = field(default="")
    gitUser: str = field(default="")
    gitPassword: str = field(default="")
    nameProject: str = field(default="")
    repoId: str = field(default="")
    projectID: str = field(default="")
    updateProject: str = field(default="")
    repoName: str = field(default="")
    login: bool = field(default=False)
    branch: str = field(default="")

    framework: str = field(default="")
    buildOptions: list[str] = field(default_factory=list)
    emails: list[str] = field(default_factory=list)
    env: dict = field(default_factory=dict)
    envAPI: list[str] = field(default_factory=list)
    group: str = field(default="")
    link: str = field(default="")
    linkNewProject: str = field(default="")
    link_Api_All: str = field(
        default="https://api.vercel.com/v12/projects/%s?teamId=%s"
    )
    link_Api_Del: str = field(default="https://api.vercel.com/v12/projects/%s")
    git: str = field(default="Gitlab")

    url: str = field(default="")
    url_Api: str = field(default="https://api.vercel.com/v12/projects?teamId=%s&s=44")
    cloneUrl: str = field(default="")
    token: str = field(default="")
    tokenAPI: str = field(default="")
    linkGit: str = field(default="https://%s:%s@gitlab.com/novateva/%s.git")
    linkGitClone: str = field(default="https://%s:%s@gitlab.com/%s/%s.git")
    linkConfig: str = field(default="")

    checkList: list[str] = field(default_factory=list)

    '''def __post_init__(self):
        self.url = self.linkGit % (self.gitUser, self.token, self.nameProject)
        self.cloneUrl = self.linkGitClone % (
            self.gitUser,
            self.gitPassword,
            self.gitUser,
            self.nameProject,
        )'''
