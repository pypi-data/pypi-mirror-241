from enum import Enum


class TransformationTemplateKind(str, Enum):
    CUSTOM = "Custom"
    DISCORD = "Discord"
    INNGEST = "Inngest"
    SEGMENT = "Segment"
    SLACK = "Slack"
    TEAMS = "Teams"

    def __str__(self) -> str:
        return str(self.value)
