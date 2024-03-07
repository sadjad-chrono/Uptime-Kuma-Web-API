from typing import List, Optional
from pydantic import BaseModel
from uptime_kuma_api import NotificationType

class Notification(BaseModel):
    type: NotificationType
    name: str
    slackwebhookURL: str
    slackchannel: str
    slackchannelnotify: bool = True
    isDefault: bool = False
    applyExisting: bool = False