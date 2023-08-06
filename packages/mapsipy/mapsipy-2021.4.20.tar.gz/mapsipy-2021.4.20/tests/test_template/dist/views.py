# -*- coding: utf-8 -*-
from mapsi import Mapsi, Component, DataStore

@Mapsi.register("counter-app")
class Counter(Component):
    template = """
<div id="app">
        <p>{count}</p>
        <button :click="count_up">+</button>
        <button :click="count_down">-</button>
    </div>
    <style>
counter-app>div>button {
    color: white;
}
</style>"""

    def __init__(self):
        super().__init__()

    def data():
        return {
            "count": 0
        }

    @Component.method
    def count_up(self, event):
        self.count += 1

    @Component.method
    def count_down(self, event):
        if self.count > 0:
            self.count -= 1

@Mapsi.register("hello-app")
class Hello(Component):
    template = """
<div>
        <input type="text" :model="{name}" :input="update_name">
        <p>{name}</p>
    </div>
    """

    def __init__(self):
        super().__init__()

    def data():
        return {
            "name": "eseunghwan"
        }

    @Component.method
    def update_name(self, event):
        self.name = event.target.value

@Mapsi.register("home-app")
class Home(Component):
    template = """
<div>
        <img src="./assets/mapsi_big.png" style="width:500px;">
        <helloworld message="Mapsi App installed!"></helloworld>
    </div>
    """

    def __init__(self):
        super().__init__()
