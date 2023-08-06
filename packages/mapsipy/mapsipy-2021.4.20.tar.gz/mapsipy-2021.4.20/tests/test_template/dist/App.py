# -*- coding: utf-8 -*-
from mapsi import Mapsi, Component, DataStore


class App(Component):
    template = """
<div id="app">
        <div style="margin-bottom:10px;">
            <router-link to="Home">home</router-link> |
            <router-link to="Counter">counter</router-link> |
            <router-link to="Hello">hello</router-link>
        </div>
        <router-view></router-view>
    </div>
    <style>
body {
    margin: 0px auto;
    /*user-select: none;*/
}

main-app {
    margin: 10px;
    color: black;
    text-align: center;
}
</style>"""

    def __init__(self):
        super().__init__()
