from direct.directnotify import DirectNotifyGlobal
from src.toontown.parties.DistributedPartyJukeboxActivityBaseAI import DistributedPartyJukeboxActivityBaseAI

class DistributedPartyJukebox40ActivityAI(DistributedPartyJukeboxActivityBaseAI):
    notify = DirectNotifyGlobal.directNotify.newCategory("DistributedPartyJukebox40ActivityAI")
