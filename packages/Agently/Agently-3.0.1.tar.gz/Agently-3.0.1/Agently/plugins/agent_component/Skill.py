from .utils import ComponentABC

class Skill(ComponentABC):
    def __init__(self, agent):
        self.agent = agent

    def must_use(self, skill_name_list: (str, list)):
        plugin_manager = self.agent.plugin_manager

    def may_use(self, skill_name_list: (str, list)):
        pass

    def export(self):
        return {
            "prefix": None,
            "suffix": None,
            "alias": {},
        }

def export():
    return ("Skill", Skill)