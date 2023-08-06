from panda3d.core import *
from direct.actor.Actor import Actor


class Character(Actor):
    def __init__(self, ModelName, AnimsName, pos, ColliderName):
        super().__init__()
        self.actor = Actor(ModelName, AnimsName)
        self.actor.reparentTo(render)
        self.actor.setPos(pos)
        capsule = CollisionSphere(0, -12, 10, 5)
        ColliderNode = CollisionNode(ColliderName)
        ColliderNode.addSolid(capsule)
        self.collider = self.actor.attachNewNode(ColliderNode)
        # self.collider.show()
