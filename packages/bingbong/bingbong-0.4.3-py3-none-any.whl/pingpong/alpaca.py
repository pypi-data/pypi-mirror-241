from pingpong.pingpong import PPManager
from pingpong.pingpong import PromptFmt

class AlpacaPromptFmt(PromptFmt):
  @classmethod
  def ctx(cls, context):
    if context is None or context == "":
      return ""
    else:
      return f"""{context}

"""

  @classmethod
  def prompt(cls, pingpong, truncate_size):
    return f"""### Instruction:
{pingpong.ping[:truncate_size]}

### Response:
{"" if pingpong.pong is None else pingpong.pong[:truncate_size]}"""

class AlpacaChatPPManager(PPManager):
  def build_prompts(self, from_idx: int=0, to_idx: int=-1, fmt: PromptFmt=AlpacaPromptFmt, truncate_size: int=None):
    if to_idx == -1 or to_idx >= len(self.pingpongs):
      to_idx = len(self.pingpongs)

    results = fmt.ctx(self.ctx)

    for idx, pingpong in enumerate(self.pingpongs[from_idx:to_idx]):
      results += fmt.prompt(pingpong, truncate_size=truncate_size)

      if from_idx+idx != to_idx-1:
        results += """

"""

    return results

