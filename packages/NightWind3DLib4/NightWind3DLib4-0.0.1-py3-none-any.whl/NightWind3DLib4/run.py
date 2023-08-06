from direct.directbase.DirectStart import base
from direct.task.TaskManagerGlobal import taskMgr
from panda3d.core import *
from NightWind3DLib4.Actor import Character


class Window:
    def __init__(self):
        # 窗体初始化
        self.base = base
        self.window = WindowProperties()
        self.window.setTitle("Run")
        self.window.setSize(600, 800)
        self.base.win.requestProperties(self.window)
        self.base.disableMouse()
        self.base.setBackgroundColor(0 / 255, 128 / 255, 255 / 255)

        # 设置地面
        self.floor = loader.loadModel("ground")
        self.floor.reparentTo(render)

        # 调整角度
        self.base.cam.setPos(0, -10015, 45)
        self.base.cam.setHpr(0, -30, -2)

        # 设置障碍物
        self.board = loader.loadModel("roadblock121_forbidden")
        self.jump1 = loader.loadModel("roadblock111_up")
        self.jump2 = loader.loadModel("roadblock211_up")
        self.roll = loader.loadModel("roadblock121_down")

        # 设置玩家
        self.player = Character(ModelName="actor",
                                AnimsName={"jump": "actor_jump",
                                           "down": "actor_down"},
                                pos=(0, -9960, 5),
                                ColliderName="player")

        # 设置键盘状态
        self.KeyStates = {"right": False, "left": False, "middle": True,
                          "changing_right": False, "changing_left": False,
                          "jump": False, "roll": False}

        # 更新界面
        self.KeyEvent()

    def KeyEvent(self):
        # 捆绑和捕捉键盘事件
        self.base.accept("w", self.ChangeKeyState, ["jump", True])
        self.base.accept("w-up", self.ChangeKeyState, ["jump", False])
        self.base.accept("s", self.ChangeKeyState, ["roll", True])
        self.base.accept("s-up", self.ChangeKeyState, ["roll", False])
        self.base.accept("a", self.ChangeKeyState, ["changing_left", True])
        # self.base.accept("a-up", self.ChangeKeyState, ["changing_left", False])
        self.base.accept("d", self.ChangeKeyState, ["changing_right", True])
        # self.base.accept("d-up", self.ChangeKeyState, ["changing_right", False])

    def ChangeKeyState(self, action, state):
        self.KeyStates[action] = state
        taskMgr.add(self.change_road)
        print(self.KeyStates)

    def change_road(self, task):
        if self.KeyStates["changing_left"]:
            # 玩家试图向左切换跑道
            self.KeyStates["changing_left"] = False

            if self.KeyStates["left"] and \
                    not self.KeyStates["middle"] and \
                    not self.KeyStates["right"]:

                # 玩家位于左边的跑道
                pass

            elif not self.KeyStates["left"] and \
                    self.KeyStates["middle"] and \
                    not self.KeyStates["right"]:

                # 玩家位于中间的跑道
                self.KeyStates["left"] = True
                self.KeyStates["middle"] = False

            elif not self.KeyStates["left"] and \
                    not self.KeyStates["middle"] and \
                    self.KeyStates["right"]:

                # 玩家位于右边的跑道
                self.KeyStates["middle"] = True
                self.KeyStates["right"] = False

        if self.KeyStates["changing_right"]:
            # 玩家试图向右切换跑道
            self.KeyStates["changing_right"] = False

            if self.KeyStates["left"] and \
                    not self.KeyStates["middle"] and \
                    not self.KeyStates["right"]:

                # 玩家位于左边的跑道
                self.KeyStates["middle"] = True
                self.KeyStates["left"] = False

            elif not self.KeyStates["left"] and \
                    self.KeyStates["middle"] and \
                    not self.KeyStates["right"]:

                # 玩家位于中间的跑道
                self.KeyStates["right"] = True
                self.KeyStates["middle"] = False

            elif not self.KeyStates["left"] and \
                    not self.KeyStates["middle"] and \
                    self.KeyStates["right"]:

                # 玩家位于右边的跑道
                pass

        if self.KeyStates["left"]:
            self.player.actor.setPos((-9, -9960, 5))
        elif self.KeyStates["middle"]:
            self.player.actor.setPos((0, -9960, 5))
        elif self.KeyStates["right"]:
            self.player.actor.setPos((9, -9960, 5))

        return task.done


if __name__ == "__main__":
    window = Window()
    window.base.run()
